<!-- ABOUT THE PROJECT -->
## About The Scripts

Les différents scripts python présent dans ce dossier servent à :
* [fonction_drone.py](https://github.com/BasileAmeeuw/DroneDelivreur/blob/main/Algorithme%20de%20vol/functions_drone.py) : Piloter le drone via des lignes de commandes. Les différentes fonctions disponible sont : armed & takeoff, change alitutude, go to, rtl, armed off.
* [hc-sr04_test.py](https://github.com/BasileAmeeuw/DroneDelivreur/blob/main/Algorithme%20de%20vol/hc-sr04_test.py) : Sert à tester le capteur hc-sr04 sur une Raspberry Pi à l'aide de la librairie adafruit_hcsr04.
* [main.py](https://github.com/BasileAmeeuw/DroneDelivreur/blob/main/Algorithme%20de%20vol/main.py) : Script Principale servant à utiliser l'algorithme de vol du drone ainsi que la reconaissance faciale. L'algorithme suivra la manoeuvre suivante :
  * Le drone décolle à une certaine altitude.
  * Le drone se dirige vers la coordonnées gps récupérer via la database
  * Le drone atterit à une altitude d'1,5m
  * Le drone commence la reconnaissance faciale
  * Si la reconnaissance faciale est bonne, le drone dépose les boissons, sinon il attend
  * Le drone re-décolle à la même altitude de départ
  * Le drone retourne à la base

### Built With

* Python3
* dronekit


<!-- GETTING STARTED -->
## Getting Started

Pour pouvoir utiliser les différents scripts python, il suffit uniquement d'avoir les bonnes librairies associées.
Pour les scripts se connectant à un drone (ou une simulation), n'oubliez pas de changer ligne de [connexion](https://github.com/BasileAmeeuw/DroneDelivreur/blob/main/Algorithme%20de%20vol/main.py#L206).

### Prerequisites

Les pré-requis nécessaire pour lancer les différents scripts sont les librairies suivantes :

* script fonction_drone.py :
  * dronekit
* script hc-sr04_test.py :
  * adafruit_hcsr04
  * board
* script main.py :
  * pyrebase
  * firebase_admin
  * google.cloud

