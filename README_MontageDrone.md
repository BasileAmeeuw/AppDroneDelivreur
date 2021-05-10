# Montage du drone

## 1. Le chassis

Le chassis utilisé est le QAV 250. Il est fourni avec toute la visserie nécessaire à son assemblage. La pièce "A" qui se place sur le dessus du chassis n'est pas nécessaire dans ce projet, elle ne sera pas montée dessus.

<p align="center"><img src="https://user-images.githubusercontent.com/50197705/117539922-ffa48400-b00c-11eb-9665-dfd01454da7d.png" alt="PieceA" width="220" height="200">


Les moteurs DC DX2205 sont montés sur les branches du chassis, ils doivent être placés de sorte que les moteurs tournant dans le même sens soit en diagonale comme illustré ci-dessous.

<p align="center"><img src="https://user-images.githubusercontent.com/50197705/117539686-0a124e00-b00c-11eb-8e64-1dd3038c38f5.png" alt="Motor Installation" width="250" height="250">


Le controlleur de vol F405-STD ainsi que la carte de distribution de puissance BEC XT60 sont installés au centre du chassis. Les ESC, eux-même soudés aux moteurs, sont soudés à la carte de puissance ; il faudra faire attention à souder correctement les moteurs comme ci-dessous pour respecter leur sens de rotation.

<p align="center"><img src="https://user-images.githubusercontent.com/50197705/117539449-fca89400-b00a-11eb-99fa-17694d365739.png" alt="ESC Welding" width="425" height="170">
  
La batterie Lion 14.8V 4s de 2300 mAh se place sur le dessus du chassis au moyen d'un velcro collé à ce dernier. La connection à la carte de puissance se fait à travers un interrupteur on/off afin d'allumer et éteindre le drone plus facilement.

<p align="center"><img src="https://user-images.githubusercontent.com/50197705/117622748-4613f300-b173-11eb-91b9-065400a7a09e.jpg" width="450" height="200">

## 2. Pièces imprimées

Avant d'imprimer les pièces, il est important d'aller voir la documentation [Discussion et amélioration des pièces 3D](https://github.com/BasileAmeeuw/DroneDelivreur/blob/main/Design3D%20STL/Discussion%20et%20am%C3%A9lioration%20des%20pi%C3%A8ces%203D.md)

### A. Boitier Raspberry Pi Zero

Ce boitier se place sous le drone, proche des branches des moteurs, au moyen de la visserie du chassis QAV 250. Les connecteurs externes de la raspberry sont encore accesibles après l'installation mais pas les pins de connections présents sur la face supérieur. Il faut donc d'abord s'assurer que les connections sont bien réalisées avant de placer le raspberry dans son boitier.

<p align="center"><img src="https://user-images.githubusercontent.com/50197705/117622465-f03f4b00-b172-11eb-977d-352fc7abe302.jpg">


### B. Support de la Camera 

La camera se place au moyen d'un petit support imprimé qui lui-même se visse à la pièce du chassis ci-dessous. Il faudra utiliser 8 vis M2 pour fixer le support au chassis et fixer la camera au support. La camera peut ensuite être connectée à la Raspberry Pi Zero au moyen de la nappe de cables par l'avant du boitier Raspeberry.

<p align="center"><img src="https://user-images.githubusercontent.com/50197705/117539412-cc60f580-b00a-11eb-93cb-357e965fd160.png" alt="Piece B" width="150" height="150">
<img src="https://user-images.githubusercontent.com/50197705/117622277-c25a0680-b172-11eb-83e3-c3af50b357aa.jpg">


### C. Support du module GPS

Le module GPS est composé d'un PCB connecté au flight controller et d'une antenne. Le PCB se place proche du F405-STD, il peut se fixer avec du papier-collant double face ou un autre moyen, l'antenne se place sur le support. Ce support est fixé sur le dessus du chassis, au niveau de la batterie et est maintenu par 2 vis du chassis. L'antenne se place dans l'emplacement carré alors que le fil passe par la goutière comme montré ci-dessous.

<p align="center"><img src="https://user-images.githubusercontent.com/50197705/117624936-c4719480-b175-11eb-9fef-ea072607e269.jpg" width="300" height="300">


### D. Train d'atterissage

Le train d'atterissage vient simplement remplacer celui fourni avec le chassis QAV 250. Les pieds sont plus longs et se fixe plus proches des moteurs afin d'augmenter la stabilité du drone au sol et de laisser plus de passage pour le plateau de transport des shots. Pour s'assurer de la stabilité du drône, après l'installation du train, effectuez une légère pression sur le drone et observez si les pieds bougent ou restent en place. Si ils bougent, il faudra simplement augmenter le frottement entre leur point d'attache et le drone, avec du tape ou en les reculant un peu plus sur les branches.

<p align="center"><img src="https://user-images.githubusercontent.com/50197705/117625114-f5ea6000-b175-11eb-8899-a028d8de8392.jpg" width="400" height="300">

  
### E. Système de plateau de livraison

Le plateau qui servira à transporter les consommations des clients en festival est en carton fin, il est possible d'utiliser un autre modèle que celui utilisé dans ce projet si il remplit les mêmes fonctions. Ce plateau est attaché au drône au moyen de 4 attaches et de 2 tiges filetées. Il est important de fixer au centre du plateau les 2 attaches du bas et de maintenir fixes les 2 attaches du haut avec 2 vis de pression après avoir percer les attaches au bon endroit (voir ci-dessous). Les vis de pression sont des M2.
Ensuite on viendra fixer les 2 modules Ultra-Sons sous les attaches du plateau (avec du collant double-face ou un autre moyen d'adhésion) et les connections se feront via des fils qui longeront les tiges filetées pour se connecter à la Raspberry Pi Zero.

<p align="center"><img src="https://user-images.githubusercontent.com/50197705/117624823-a310a880-b175-11eb-83eb-096304fb49ca.jpg" width="300" height="350">


