from dronekit import connect, VehicleMode, LocationGlobalRelative
import time
import RPi.GPIO as GPIO
import os, re
import pyrebase
import firebase_admin
from firebase_admin import credentials
from google.cloud import firestore
import board
import adafruit_hcsr04

def arm_and_takeoff(aTargetAltitude):
    """
    Arms vehicle and fly to aTargetAltitude.
    """

    print("Basic pre-arm checks")
    # Don't try to arm until autopilot is ready
    while not vehicle.is_armable:
        print(" Waiting for vehicle to initialise...")
        time.sleep(1)

    print("Arming motors")
    # Copter should arm in GUIDED mode
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    # Confirm vehicle armed before attempting to take off
    while not vehicle.armed:
        print(" Waiting for arming...")
        time.sleep(1)

    print("Taking off!")
    vehicle.simple_takeoff(aTargetAltitude)  # Take off to target altitude

    # Wait until the vehicle reaches a safe height before processing the goto
    #  (otherwise the command after Vehicle.simple_takeoff will execute
    #   immediately).
    while True:
        print(" Altitude: ", vehicle.location.global_relative_frame.alt)
        # Break and return from function just below target altitude.
        if vehicle.location.global_relative_frame.alt >= aTargetAltitude * 0.95:
            print("Reached target altitude")
            break
        time.sleep(3)

def change_alt (altitude):
    print ("Changing Altitude")
    if vehicle.armed :
        location = vehicle.location.global_relative_frame
        final_alt = location.alt + altitude
        location.alt = final_alt
        vehicle.simple_goto(location)
        while True:
            print(" Altitude: ", vehicle.location.global_relative_frame.alt)
            # Break and return from function just below target altitude.
            if vehicle.location.global_relative_frame.alt >= final_alt - 0.02 and vehicle.location.global_relative_frame.alt <= final_alt + 0.02 :
                print("Reached target altitude")
                break
            time.sleep(1)
    
    else:
        print ("Vehicule is not Armed")

def go_to (relative_coord):
    if vehicle.armed :
        vehicle.simple_goto (relative_coord, groundspeed = 10)
        while True :
            print(" Vehicule is at: ", vehicle.location.global_relative_frame)
            if (vehicle.location.global_relative_frame.lon >= relative_coord.lon - 0.00001 and vehicle.location.global_relative_frame.lon <= relative_coord.lon + 0.00001) and (vehicle.location.global_relative_frame.lat >= relative_coord.lat - 0.00001 and vehicle.location.global_relative_frame.lat <= relative_coord.lat + 0.00001) :
                print("Target Reached")
                break
            time.sleep(3)
    else:
        print ("Vehicule is not Armed")

def rtl (alt):
    if vehicle.armed :
        go_to(alt)
    else:
        print ("Vehicule is not Armed")

def land (alt):
    altitude = alt
    alt_initial = vehicle.location.global_relative_frame.alt
    for i in range (1,int((alt+0.5)*2)):
        detect1 = distance (GPIO_TRIGGER1,GPIO_ECHO1)
        detect2 = distance (GPIO_TRIGGER2,GPIO_ECHO2)
        if detect1 == True or detect2 == True :
            move_up(altitude)
        else :
            print ("Landing")
            change_alt (-0.5)
            altitude -= 0.5

def move_up (alt):
    # 1 degree -> 111,111 km
    # 1m = 0,000009 degree
    print ("Move Up")
    gps = vehicle.location.global_relative_frame
    gps.lon += 0.000009
    go_to(gps)
    detect1 = distance (GPIO_TRIGGER1,GPIO_ECHO1)
    detect2 = distance (GPIO_TRIGGER2,GPIO_ECHO2)
    if detect1 == True or detect2 == True : 
        move_down (alt)
    else :
        land (alt)

def move_down (alt) :
    print ("Move Down")
    gps = vehicle.location.global_relative_frame
    gps.lon -= 0.000009 *2
    go_to(gps)
    detect1 = distance (GPIO_TRIGGER1,GPIO_ECHO1)
    detect2 = distance (GPIO_TRIGGER2,GPIO_ECHO2)
    if detect1 == True or detect2 == True : 
        move_left (alt)
    else :
        land (alt)

def move_left (alt) :
    print ("Move Left")
    gps = vehicle.location.global_relative_frame
    gps.lon += 0.000009
    gps.lat -= 0.000009
    go_to(gps)
    detect1 = distance (GPIO_TRIGGER1,GPIO_ECHO1)
    detect2 = distance (GPIO_TRIGGER2,GPIO_ECHO2)
    if detect1 == True or detect2 == True : 
        move_right (alt)
    else :
        land (alt)

def move_right (alt) :
    print ("Move Right")
    gps = vehicle.location.global_relative_frame
    gps.lat += 0.000009 *2
    go_to(gps)
    detect1 = distance (GPIO_TRIGGER1,GPIO_ECHO1)
    detect2 = distance (GPIO_TRIGGER2,GPIO_ECHO2)
    if detect1 == True or detect2 == True : 
        print ("No possibility")
    else :
        land (alt)

def distance(TRIGGER, ECHO):
    sonar = adafruit_hcsr04.HCSR04(trigger_pin=TRIGGER, echo_pin=ECHO)
    while sonar.distance == 0 :
        try:
            print(sonar.distance)
        except:
            print("Retrying!")
        
        time.sleep (0.5)
    
    print (str(sonar.distance) + " cm")

    if sonar.distance <= 20 :
        return True
    else :
        return False

def armed_off():
    if vehicle.armed :
        vehicle.armed = False

def db_connection (config):
    firebase=pyrebase.initialize_app(firebaseConfig)
    storage=firebase.storage()
    try:
        firebase_admin.get_app()
        print('firebase intialized.')

    except ValueError as e:
        print('firebase not initialized. initialize.')
        cred = credentials.Certificate("serviceAccountKey.json")
        firebase_admin.initialize_app(cred)

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="serviceAccountKey.json"
    
    return firestore.Client()

firebaseConfig = {
  "apiKey": "AIzaSyDyRZKc3IhpvvXUdV9qs3Hu_EMvN_JjEMY",
  "authDomain": "delivreapp-5221e.firebaseapp.com",
  "projectId": "delivreapp-5221e",
  "databaseURL": "https://del-ivre-default-rtdb.europe-west1.firebasedatabase.app",
  "storageBucket": "delivreapp-5221e.appspot.com",
  "messagingSenderId": "661920641786",
  "appId": "1:661920641786:web:dca2c085b5ff60f1b18f43",
  "measurementId": "G-CLR5PFH3G4"

}

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BOARD)
 
#set GPIO Pins
GPIO_TRIGGER1 = board.D14
GPIO_ECHO1 = board.D15

GPIO_TRIGGER2 = board.D17
GPIO_ECHO2 = board.D27

vehicle = connect('udp:127.0.0.1:14550', wait_ready=True)
print('Connecting to vehicle : %s' % vehicle)
print ("Simulation Location : \n%s" % vehicle.location.global_relative_frame)
init = vehicle.location.global_relative_frame


while True:
    nbImg=[];
    go=True
    while True: 
        try:
            doc=db.collection('Users').where("Drone","==",nDrone).get()[0]
            break
        except:
            continue

    nom=doc.get("Nom")
    prenom=doc.get("Prenom")
    coord=doc.get("GPS")
    image=nom+"#"+prenom+".jpg"
    print(nom,end=' ')
    print(prenom,end="\n")
    print(doc.get("Commande"),end="\n")
    print(coord)
    
    #téléchargement image
    storage.child(image).download(image)

    ###variables d'initiation reconnaissance faciale
    known_face_encodings = []
    known_face_names = []
    face_locations = []
    face_encodings = []
    process_this_frame = True

    #Image enregistrée dans la base de donnée
    try:
        new_image=face_recognition.load_image_file(image)
        new_face_encoding = face_recognition.face_encodings(new_image)[0]
        known_face_encodings.append(new_face_encoding)
        known_face_names.append(prenom + " " + nom)
        print("photo", " dans reconaissance faciale")
    except:
        img1 = Image.open(image)
        img1.save("img1.jpg","JPEG")
        try:
            time.sleep(0.001)
            img1.save("img1.jpg","JPEG")
            time.sleep(0.001)
            img2=img1.rotate(90)
            img2.show()
            time.sleep(0.001)
            img2.save("img2.jpg","JPEG")
            img3=img2.rotate(90)
            time.sleep(0.001)
            img3.save("img3.jpg","JPEG")
            img4=img3.rotate(90)
            time.sleep(0.001)
            img4.save("img4.jpg","JPEG")
            #os.remove(image)
            print("image enregistrée")
        except:
            print("probleme dans le téléchargement de l'image")
        for i in range(1,5):
            try:
                new_image=face_recognition.load_image_file("img"+ str(nbImg) + ".jpg")
                new_face_encoding = face_recognition.face_encodings(new_image)[0]
                known_face_encodings.append(new_face_encoding)
                known_face_names.append(prenom + " " + nom)
                nbImg=i
                print("photo" , str(i) , " dans reconaissance faciale")
            except:
                os.remove("img"+ str(i) + ".jpg")
                print("photo ", str(i) , "non prise en compte")
    

    ###Décolage, jusqu'a reconaissance
    print("décolage jusque coordonnée gps et arrivée à 1m50")
    arm_and_takeoff (10)
    print("go_to position: ", coord)
    time.sleep(2)
    # go_to (LocationGlobalRelative(float(-35.3633), float(149.1652294), float(10)))
    #go_to (LocationGlobalRelative(float(coord["Latitude"]), float(coord["Longitude"]), float(50)))
    land (8.5)
    #Face recognition
    #change_alt (-48.5)
    print("descendre")
    time.sleep(2)
    Reco=True
    #algo reconnaissance faciale
    print("lancement algorithme de reconnaissance faciale")
    while Reco:
        # Grab a single frame of video
        ret, frame = cv2.VideoCapture(0).read()

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Only process every other frame of video to save time
        if process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"

                # If a match was found in known_face_encodings, just use the first one.
                if True in matches:
                    first_match_index = matches.index(True)
                    name = known_face_names[first_match_index]

                if name==prenom+" "+nom:
                    print(name, end=' ')
                    print("a bien été reconnu, on procède donc a l'attérissage.")
                    Reco=False

        process_this_frame = not process_this_frame

    #Attérissage et déposage paquet
    print("attérissage sur .... pour que la personne récupère sa commande")
    '''land (48.5)'''
    time.sleep(2)
    print("land successfull: alt: 0")

    #Attente de 1 minute avant de redémarrer
    print("attente de 1 minute avant de redémarrer")
    time.sleep(5)
    #suppression image du PC
    print("image supprimé de la mémoire du rpi")
    for i in range(len(nbImg)):
        os.remove("img"+ str(nbImg[i]) + ".jpg")

    #retour à la base
    print("retour à la base pour une nouvelle commande")
    rtl()
    armed_off()
    print("suppression de la commande si pas encore fait")

    try:
        id=str(int(doc.get("Id")))
        db.collection('Users').document(id).delete()
        print("la commande a été supprimée")
        storage.delete_blob(image)
        storage.delete()
    except:
        print("la commande était déja supprimée")

vehicle.close()