# Reconnaissance faciale

Pour ce qui est de l'algorithme de reconnaissance faciale. Voici le lien github de la librairie utilisée. [Reconnaissance_faciale](https://github.com/ageitgey/face_recognition) Cependant ici après sont expliquées quelques cas d'utilisation dans notre cas.

Vous pouvez suivre leur github pour l'installation qui est très bien expliquée.
Ensuite dans notre Use Case on utilise la base de donnée d'une facon particulière pour l'algorithme de reconnaissance.

## Intégration de la base de donnée

![Intégration base de donnée](https://github.com/BasileAmeeuw/AppDroneDelivreur/blob/main/Image%20github/BDDetRECO/IntegrationBDD.png)

## Comment on récupère la bonne commande (ici pour drone 5)

![Recupération BDD](https://github.com/BasileAmeeuw/AppDroneDelivreur/blob/main/Image%20github/BDDetRECO/RecupBDD.png)

## Essaie d'intégration de la photo dans l'algorithme
Etant donné qu'on ne peut pas prédéfinir le sens de la photo que l'utilisateur va prendre, on essaye de retourner la photo dans tous les sens jusqu'a ce que ca fonctionne

Solution pour rendre la photo lisible par l'algorithme:

``` python
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
```
## Algorithme en tant que tel
Pour plus d'info aller voir sur leur repo github

![reco_algo](https://github.com/BasileAmeeuw/AppDroneDelivreur/blob/main/Image%20github/BDDetRECO/reco_algo.png)

## Suppression des données après livraison
En effet pour ne pas etre soumis a une obligation d'inscription et une signature de droit d'utilisation, aucune donnée n'est gardée afin de respecter les RGPD

![RGPD](https://github.com/BasileAmeeuw/AppDroneDelivreur/blob/main/Image%20github/BDDetRECO/suppressionBDD.png)

### Référence
[https://github.com/ageitgey/face_recognition](https://github.com/ageitgey/face_recognitionhttps://github.com/ageitgey/face_recognition)

[https://www.youtube.com/watch?v=QxtIBQPIhjs](https://www.youtube.com/watch?v=QxtIBQPIhjs)

[https://www.youtube.com/watch?v=UVzBQ0LkO28](https://www.youtube.com/watch?v=UVzBQ0LkO28)
