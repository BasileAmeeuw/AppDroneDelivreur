<style>
.aligncenter {
    text-align: center;
}
</style>


# Explication application client

Cette application est composé en 6 vues principales, l'accueil, la page pour faire la photo, la commande, le payement, l'envoie de ses coordonnées GPS et la confirmation, mais en plus de celles-ci viennent s'ajouter une vue pour voir toutes les commandes ainsi qu'une liste de reprise de commande si il y a eu un problème avec une commande en cours.

## Téléchargement et code
* Lien .aia (ouvrir dans Kodular) [ici](https://github.com/BasileAmeeuw/DroneDelivreur/tree/main/Applications.aia)
* Lien .apk (téléchargement app) [ici](https://github.com/BasileAmeeuw/DroneDelivreur/tree/main/Applications.apk)

## Explication
Toutes ces vues se retrouvent donc dans Kodular : <img src="https://github.com/BasileAmeeuw/AppDroneDelivreur/blob/main/Image%20github/Vues/DelIvreApp/Vues.png" width="20%"/>

Voici donc les 6 vues principales :

1. L'accueil: <img src="https://github.com/BasileAmeeuw/AppDroneDelivreur/blob/main/Image%20github/Vues/DelIvreApp/accueil.png" width="20%"/>

2. La page photo: <img src="https://github.com/BasileAmeeuw/AppDroneDelivreur/blob/main/Image%20github/Vues/DelIvreApp/photo.png" width="20%"/>

3. La commande: <img src="https://github.com/BasileAmeeuw/AppDroneDelivreur/blob/main/Image%20github/Vues/DelIvreApp/commande.png" width="20%"/>

4. Le payement: <img src="https://github.com/BasileAmeeuw/AppDroneDelivreur/blob/main/Image%20github/Vues/DelIvreApp/payement.png" width="20%"/>

5. Les coordonnées <img src="https://github.com/BasileAmeeuw/AppDroneDelivreur/blob/main/Image%20github/Vues/DelIvreApp/GPS.png" width="20%"/>

6. La confirmation: <img src="https://github.com/BasileAmeeuw/AppDroneDelivreur/blob/main/Image%20github/Vues/DelIvreApp/Confirmation.png" width="20%"/>

## Kodular étant été utilisé voici quelques blocs méritant ou nécessitant une explication:

1. L'intégration de la base de donnée:

<img src="https://github.com/BasileAmeeuw/DroneDelivreur/blob/main/Image%20github/BlockKodular/DelIvreApp/InkedintegrationDB.jpg" width="50%"/>

2. Pour l'accueil, le bloc suivant  sert a controler si le nom et prénom sont correct afin de passer à la page suivante

<img src="https://github.com/BasileAmeeuw/DroneDelivreur/blob/main/Image%20github/BlockKodular/DelIvreApp/CheckNameSurnameValid.png" width="50%"/>

3. Pour la page photo, le bloc ci-dessous sert à enregistrer la photo prise par le Smartphone

<img src="https://github.com/BasileAmeeuw/DroneDelivreur/blob/main/Image%20github/BlockKodular/DelIvreApp/PrisePhotoCamera.png" width="50%"/>

4. Pour le payement, l'intégration de Paypal ce fait comme suit

<img src="https://github.com/BasileAmeeuw/DroneDelivreur/blob/main/Image%20github/BlockKodular/DelIvreApp/InkedPaypalConfig.jpg" width="50%"/>

et le payement comme ça

<img src="https://github.com/BasileAmeeuw/DroneDelivreur/blob/main/Image%20github/BlockKodular/DelIvreApp/PaypalPayePlusCommandePaye.png" width="50%"/>

5. Pour l'envoie des coordonnées GPS, tout d'abord l'app regarde si la commande est en cours de traitement grâce au bloc suivant

<img src="https://github.com/BasileAmeeuw/DroneDelivreur/blob/main/Image%20github/BlockKodular/DelIvreApp/CheckCommandePrepaForGPS.png" width="50%"/>

et puis les coordonnées sont envoyées avec ce bloc

<img src="https://github.com/BasileAmeeuw/DroneDelivreur/blob/main/Image%20github/BlockKodular/DelIvreApp/EnvoieCoordGPS.png" width="50%"/>

6. La gestion RGPD se fait grace à ces blocs

<img src="https://github.com/BasileAmeeuw/DroneDelivreur/blob/main/Image%20github/BlockKodular/DelIvreApp/RGPDGestion.png" width="50%"/>



