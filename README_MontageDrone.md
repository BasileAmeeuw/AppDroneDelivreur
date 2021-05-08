# Montage du drone

## 1. Le chassis

Le chassis utilisé est le QAV 250. Il est fourni avec toute la visserie nécessaire à son assemblage. La pièce "A" qui se place sur le dessus du chassis n'est pas nécessaire dans ce projet, elle ne sera pas montée dessus.

<p align="center"><img src="https://user-images.githubusercontent.com/50197705/117187407-28920280-addc-11eb-9fe1-ca7f4018f014.jpg" alt="PieceA" width="170" height="150">

Les moteurs DC XXX sont montés sur les branches du chassis, ils doivent être placés de sorte que les moteurs tournant dans le même sens soit en diagonale comme illustré ci-dessous.

<p align="center"><img src="https://user-images.githubusercontent.com/50197705/117295954-c6391080-ae74-11eb-971b-adc23ea421f1.png" alt="Motor Installation" width="200" height="200">

Le controlleur de vol F405-STD ainsi que la carte de distribution de puissance BEC XT60 sont installés au centre du chassis. Les ESC, eux-même soudés aux moteurs, sont soudés à la carte de puissance ; il faudra faire attention à souder correctement les moteurs comme ci-dessous pour respecter leur sens de rotation.

<p align="center"><img src="https://user-images.githubusercontent.com/50197705/117291760-af43ef80-ae6f-11eb-8467-825054a87ce7.png" alt="ESC Welding" width="425" height="150">
  
La batterie Lion 14.8V 4s de 2300 mAh se place sur le dessus du chassis au moyen d'un velcro collé à ce dernier. La connection à la carte de puissance se fait à travers un interrupteur on/off afin d'allumer et éteindre le drone plus facilement.

<p align="center">INSERT PHOTO BATTERIE INSTALLÉE

## 2. Pièces imprimées

Avant d'imprimer les pièces, il est important d'aller voir la documentation [Discussion et amélioration des pièces 3D](https://github.com/BasileAmeeuw/DroneDelivreur/blob/main/Design3D%20STL/Discussion%20et%20am%C3%A9lioration%20des%20pi%C3%A8ces%203D)

### A. Boitier Raspberry Pi Zero

Ce boitier se place sous le drone, proche des branches des moteurs, au moyen de la visserie du chassis QAV 250. Les connecteurs externes de la raspberry sont encore accesibles après l'installation mais pas les pins de connections présents sur la face supérieur. Il faut donc d'abord s'assurer que les connections sont bien réalisées avant de placer le raspberry dans son boitier.

<p align="center">INSERT PHOTO DU BOITIER INSTALLÉ

### B. Support de la Camera 

La camera se place au moyen d'un petit support imprimé qui lui-même se visse à la pièce du chassis ci-dessous. Il faudra utiliser 8 vis M2 pour fixer le support au chassis et fixer la camera au support. La camera peut ensuite être connectée à la Raspberry Pi Zero au moyen de la nappe de cables par l'avant du boitier Raspeberry.

<p align="center"><img src="https://user-images.githubusercontent.com/50197705/117321644-9d714500-ae8d-11eb-846b-8bc21bca98b9.jpg" alt="Piece B" width="150" height="150">

<p align="center">INSERT PHOTO DE LA CAM INSTALLÉE

### C. Support du module GPS

Le module GPS est composé d'un PCB connecté au flight controller et d'une antenne. Le PCB se place proche du F405-STD, il peut se fixer avec du papier-collant double face ou un autre moyen, l'antenne se place sur le support. Ce support est fixé sur le dessus du chassis, au niveau de la batterie et est maintenu par 2 vis du chassis. L'antenne se place dans l'emplacement carré alors que le fil passe par la goutière comme montré ci-dessous.

<p align="center">INSERT PHOTO ANTENNE GPS

### D. Train d'atterissage

Le train d'atterissage vient simplement remplacer celui fourni avec le chassis QAV 250. Les pieds sont plus longs et se fixe plus proches des moteurs afin d'augmenter la stabilité du drone au sol et de laisser plus de passage pour le plateau de transport des shots.

<p align="center">INSERT PHOTO TRAIN
  
### E. Système de plateau de livraison

Le plateau qui servira à transporter les consommations des clients en festival est en carton fin, il est possible d'utiliser un autre modèle que celui utilisé dans ce projet si il remplit les mêmes fonctions. Ce plateau est attaché au drône au moyen de 4 attaches et de 2 tiges filetées. Il est important de fixer au centre du plateau les 2 attaches du bas et de maintenir fixes les 2 attaches du haut avec 2 vis de pression après avoir percer les attaches au bon endroit (voir ci-dessous). Les vis de pression sont des M2.

<p align="center">INSERT PHOTO PLATEAU+ATTACHES

