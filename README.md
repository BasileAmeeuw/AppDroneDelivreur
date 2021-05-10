# README séparé en plusieurs:

1. Reconnaissance faciale algorithme: [ici](https://github.com/BasileAmeeuw/AppDroneDelivreur/blob/main/README_RecoFaciale.md)

2. Applications:

  * Application Barman: [ici](https://github.com/BasileAmeeuw/AppDroneDelivreur/blob/main/README_BarmanApp.md)
  
  * Application Client: [ici](https://github.com/BasileAmeeuw/AppDroneDelivreur/blob/main/README_DelivreApp.md)
  
3. Fonctions drone: [ici](https://github.com/BasileAmeeuw/DroneDelivreur/blob/main/README_FonctionDrone.md)
4. Configuration du drone: [ici](https://github.com/BasileAmeeuw/DroneDelivreur/blob/main/README_Drone-Configuration.md)
5. Montage du drone: [ici](https://github.com/BasileAmeeuw/DroneDelivreur/blob/main/README_MontageDrone.md)

# Scope du projet

### Scope PROJET DRONE Delivreur

Le concept du  projet  est  de  développer  un  drone  autopiloté qui,  grâce  à  une  application,  peut  se déplacer  vers  des  coordonnées  GPS afin  de  livrer des  consommations  à  des  festivaliersdans  une optique de limiter les contacts entre les personnes et désengorger les files au bar.Le  drone  devra  être  capable  de  transporter jusqu’à 6 consommations de 4clsur  une  distance  de maximum 500 mètres.Il livrera aux coordonnées GPS avec une marge d’erreur d’1 mètre carré qui délimitera sa zone d’atterrissage.Il pourra voler tant que le temps n’est pas pluvieux et si les rafalesde vent ne dépassent pas 30 km/h.Il disposera d’une caméra ainsi que d’un protocole de reconnaissance faciale afin de déterminer  le commanditaire de la livraison.La batterie sera éjectable facilement afin de pouvoir la changer rapidement.Le  drone utilisera un accéléromètre à 6 axes afin de se stabiliser et de se repérer dans l’espace.  Il utilisera soit un altimètre soit l’accéléromètre pour se situer en hauteur par rapport à son espace de décollage. Il sera muni d’un capteur GPS afin de connaitre ses propres coordonnées.Le drone sera motorisé par 4 moteurs DC Brushless qui feront tourner des hélices.Il disposera d’un train d’atterrissage muni d’un plateau pour le transport des consommations.Il sera alimenté par une batterie Lipod’au moins 3000mAh et utilisera un convertisseur pour alimenter les composants électroniques.Coté  application: l'application auraune  interface  de  connexion  afin  de  se  connecter  à  la  base  de donnéesde l’event et avoir accès à ces “Coins”.Une  autre  interface  sera  dédiéeà  la  commande  qui  renverra  une  commande  plus  la  photo  de  la personne.Tout sera alors envoyé dans une base de données, dans une liste d’attente, que le drone se chargera de prendre dans l’ordre d’envoide commande

# App DroneDelivreur
Ce repo contient deux fichier .aia que vous pouvez ouvrir dans kodular. C'est fichier sont les deux applications indispensables à notre projets le drone livreur

Voici le lien pour la documentation : [README app BarmanApp](https://github.com/BasileAmeeuw/AppDroneDelivreur/blob/main/README_BarmanApp.md) et [README app DelIvre](https://github.com/BasileAmeeuw/AppDroneDelivreur/blob/main/README_DelivreApp.md) et une vidéo d'explication supplémentaire pour les deux [Vidéo explicative](https://youtu.be/whOkrrNxA8E)

Database et reconnaissance faciale: L'intégration de la BDD est expliquée avec l'algorithme de la reconnaissance faciale [ici](https://github.com/BasileAmeeuw/DroneDelivreur/blob/main/README_RecoFaciale.md) ainsi que les explications sur la base de données [ici](https://github.com/BasileAmeeuw/DroneDelivreur/tree/main/README_DataBase) ainsi qu'une [Vidéo d'explication](https://www.youtube.com/watch?v=zAVjq34hjDs&feature=youtu.be)

# Algorithme de Vol
Ce repo contient les scripts permettant de tester les fonctions de vol et l'algorithme de vol. Il est également possible de tester le capteur à UltraSon HC-SR04 depuis une Raspberry Pi.

N'hésitez pas à consulter le [ReadMe](https://github.com/BasileAmeeuw/DroneDelivreur/blob/main/README_FonctionDrone.md) ainsi que la documentation :
* [Simulation d'un drone via dronekit-sitl](https://github.com/BasileAmeeuw/DroneDelivreur/blob/main/Algorithme%20de%20vol/Drone_Simulation.pdf)
* [Communication entre la Raspberry Pi Zéro et le Flight Controller](https://github.com/BasileAmeeuw/DroneDelivreur/blob/main/Algorithme%20de%20vol/Raspberry-FC%20Communication.pdf)
* [Utilisation de la librairie dronekit pour communiquer avec le drone](https://github.com/BasileAmeeuw/DroneDelivreur/blob/main/Algorithme%20de%20vol/Talk%20to%20the%20FC%20with%20dronekit.pdf)

Il y a également 2 tutoriels disponible :
* [Simulation d'un drone et visualisation sur Mission Planner](https://github.com/BasileAmeeuw/DroneDelivreur/blob/main/Algorithme%20de%20vol/Simulation%20d'un%20drone%20via%20dronekit.mp4)
* [Utilisation de dronekit pour envoyer des commandes sur un drone](https://github.com/BasileAmeeuw/DroneDelivreur/blob/main/Algorithme%20de%20vol/Tutoriel%20_%20Communication%20MAVLink%20entre%20une%20RPi%20Z%C3%A9ro%2C%20une%20station%20de%20contr%C3%B4le%20et%20un%20drone.mp4)

