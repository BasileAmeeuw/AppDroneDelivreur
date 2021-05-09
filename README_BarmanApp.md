# Explication application Barman

Cette application est composé en 4 vues principales, l'accueil, la liste des commandes en attente, la préparation en elle-même et la confirmation, mais en plus de celles-ci viennent s'ajouter une vue pour voir toutes les commandes ainsi qu'une liste de reprise de commande si il y a eu un problème avec une commande en cours.

## Téléchargement et code
* Lien .aia (ouvrir dans Kodular) [ici](https://github.com/BasileAmeeuw/DroneDelivreur/tree/main/Applications.aia)
* Lien .apk (téléchargement app) [ici](https://github.com/BasileAmeeuw/DroneDelivreur/tree/main/Applications.apk)

## Explication
Toutes ces vues se retrouvent donc dans Kodular:
<img src="https://github.com/BasileAmeeuw/AppDroneDelivreur/blob/main/Image%20github/Vues/BarmanApp/VuePrincipaleBarman.png" width="20%"/>

Voici les 4 vues principales 
* L'accueil : <img src="https://github.com/BasileAmeeuw/AppDroneDelivreur/blob/main/Image%20github/Vues/BarmanApp/Accueil.png " width="20%"/>
* Liste de commandes en attente: <img src="https://github.com/BasileAmeeuw/AppDroneDelivreur/blob/main/Image%20github/Vues/BarmanApp/VuePrepa.png" width="20%"/>
  Cette vue peut egalement etre vide <img src="https://github.com/BasileAmeeuw/AppDroneDelivreur/blob/main/Image%20github/Vues/BarmanApp/Preparation.png" width="20%"/>
* La préparation de la commande <img src="https://github.com/BasileAmeeuw/AppDroneDelivreur/blob/main/Image%20github/Vues/BarmanApp/commande.png" width="20%"/>
* La confirmation <img src="https://github.com/BasileAmeeuw/AppDroneDelivreur/blob/main/Image%20github/Vues/BarmanApp/Confirmation.png" width="20%"/>

## Kodular étant été utilisé voici quelques blocs méritant ou nécessitant une explication:

1. L'intégration de la base de donnée: 

<img src="https://github.com/BasileAmeeuw/DroneDelivreur/blob/main/Image%20github/BlockKodular/BarmanApp/InkedintegrationDB.jpg" width="50%"/>

2. Affichage des commandes dans l'ordre de celles qui doivent etre préparé

<img src="https://github.com/BasileAmeeuw/DroneDelivreur/blob/main/Image%20github/BlockKodular/BarmanApp/PreparationBlock.png" width="50%"/>

3. Affichage de toutes les commandes (à préparé ou non)

<img src="https://github.com/BasileAmeeuw/DroneDelivreur/blob/main/Image%20github/BlockKodular/BarmanApp/commandeVisualView.png"/>

4. Envoie préparation si on a récupérer les coordonnées GPS

<img src="https://github.com/BasileAmeeuw/DroneDelivreur/blob/main/Image%20github/BlockKodular/BarmanApp/EnvoieIfGPS.png" width="50%"/>


4. 
