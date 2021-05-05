# README séparé en plusieurs:

1. Reconnaissance faciale algorithme: [ici](https://github.com/BasileAmeeuw/AppDroneDelivreur/blob/main/README_RecoFaciale.md)

2. Applications:

  * Application Barman: [ici](https://github.com/BasileAmeeuw/AppDroneDelivreur/blob/main/README_BarmanApp.md)
  
  * Application Client: [ici](https://github.com/BasileAmeeuw/AppDroneDelivreur/blob/main/README_DelivreApp.md)
  
3. Fonctions drone: [ici](https://github.com/BasileAmeeuw/DroneDelivreur/blob/main/README_FonctionDrone.md)

# Scope du projet

### Scope PROJET DRONE Delivreur

Le concept du  projet  est  de  développer  un  drone  autopiloté qui,  grâce  à  une  application,  peut  se déplacer  vers  des  coordonnées  GPS afin  de  livrer des  consommations  à  des  festivaliersdans  une optique de limiter les contacts entre les personnes et désengorger les files au bar.Le  drone  devra  être  capable  de  transporter jusqu’à 6 consommations de 4clsur  une  distance  de maximum 500 mètres.Il livrera aux coordonnées GPS avec une marge d’erreur d’1 mètre carré qui délimitera sa zone d’atterrissage.Il pourra voler tant que le temps n’est pas pluvieux et si les rafalesde vent ne dépassent pas 30 km/h.Il disposera d’une caméra ainsi que d’un protocole de reconnaissance faciale afin de déterminer  le commanditaire de la livraison.La batterie sera éjectable facilement afin de pouvoir la changer rapidement.Le  drone utilisera un accéléromètre à 6 axes afin de se stabiliser et de se repérer dans l’espace.  Il utilisera soit un altimètre soit l’accéléromètre pour se situer en hauteur par rapport à son espace de décollage. Il sera muni d’un capteur GPS afin de connaitre ses propres coordonnées.Le drone sera motorisé par 4 moteurs DC Brushless qui feront tourner des hélices.Il disposera d’un train d’atterrissage muni d’un plateau pour le transport des consommations.Il sera alimenté par une batterie Lipod’au moins 3000mAh et utilisera un convertisseur pour alimenter les composants électroniques.Coté  application: l'application auraune  interface  de  connexion  afin  de  se  connecter  à  la  base  de donnéesde l’event et avoir accès à ces “Coins”.Une  autre  interface  sera  dédiéeà  la  commande  qui  renverra  une  commande  plus  la  photo  de  la personne.Tout sera alors envoyé dans une base de données, dans une liste d’attente, que le drone se chargera de prendre dans l’ordre d’envoide commande

# AppDroneDelivreur
Ce repo contient deux fichier .aia que vous pouvez ouvrir dans kodular. C'est fichier sont les deux applications indispensables à notre projets le drone livreur

Voici le lien pour la documentation : [README app BarmanApp](https://github.com/BasileAmeeuw/AppDroneDelivreur/blob/main/README_BarmanApp.md) et [README app DelIvre](https://github.com/BasileAmeeuw/AppDroneDelivreur/blob/main/README_DelivreApp.md) et une vidéo d'explication supplémentaire pour les deux [Vidéo explicative](https://youtu.be/whOkrrNxA8E)

Voici une petite explication sur la database: [Vidéo d'explication](https://www.youtube.com/watch?v=zAVjq34hjDs&feature=youtu.be), l'intégration de la BDD est expliquée avec l'algorithme de la reconnaissance faciale [ici](https://github.com/BasileAmeeuw/DroneDelivreur/blob/main/README_RecoFaciale.md) ainsi qu'une vue d'ensemble de la base de donnée se trouve [ici](https://github.com/BasileAmeeuw/DroneDelivreur/tree/main/DataBase)



