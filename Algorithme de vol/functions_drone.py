from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

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
        time.sleep(1)

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
            if vehicle.location.global_relative_frame.alt >= final_alt * 0.95:
                print("Reached target altitude")
                break
            time.sleep(1)
    
    else:
        print ("Vehicule is not Armed")

def go_to (relative_coord):
    if vehicle.armed :
        vehicle.simple_goto (relative_coord, groundspeed = 10)
    else:
        print ("Vehicule is not Armed")

def rtl ():
    if vehicle.armed :
        vehicle.mode = VehicleMode("RTL")
    else:
        print ("Vehicule is not Armed")
    
def armed_off():
    if vehicle.armed :
        vehicle.armed = False

vehicle = connect('udp:127.0.0.1:14550', wait_ready=True, baud=57600)
print('Connecting to vehicle : %s' % vehicle)

try :
    while True:
        choice = input("Choose a function :\n1: Armed & TakeOff\n2: Change Altitude\n3: Go To a GPS coord\n4: Return to Launch\n5: Exit\n")
        if choice == '1':
            alt = input ("Specifie an Altitude to TakeOff\n")
            arm_and_takeoff(float(alt))
        elif choice == '2':
            alt = input ("Specifie an Atltitude to Reached\n")
            change_alt (alt)
        
        elif choice == '3':
            lat = input ("Specifie a Latitude to Reached\n") 
            lon = input ("Specifie a Longitude to Reached\n")
            alt = input ("Specifie an Atltitude to Reached\n")
            go_to (LocationGlobalRelative(float(lat), float(lon), float(alt)))
        elif choice == '4':
            rtl()
        elif choice == '5':
            break

except KeyboardInterrupt:
    rtl()
    armed_off()

vehicle.close()