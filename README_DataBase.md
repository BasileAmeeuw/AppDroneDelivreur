# Explication sur la base de donnée

## Cloud Firestore

Voici une présentation structurelle de la base de donnée "cloud firestore":

<img src="https://github.com/BasileAmeeuw/DroneDelivreur/blob/main/Image%20github/BDDetRECO/DatabaseStructure.png" width="70%"/>

Document (id):
* id: timestamp qui est le même que l'id référence du document pour pouvoir les mettre dans l'ordre de la commande
* nom: nom de l'utilisateur
* prenom: prenom de l'utilisateur
* prix: prix de la commande (somme de tous les prix des shots
* drone: numéro du drone 
* paye: bool pour dire si c'est paye ou non
* gps: contient la latitude et la longitude de l'utilisateur
* commande: commande qui contient une liste avec tous les shots commandés ainsi que le nombre
* commandeId: l'id de la commande
* livre: bool pour définir si le drone est en cours de livraison
* enPreparation: bool pour dire si il est en cours de préparation
* enRepriseCommande: bool pour définir si il est en reprise de commande (quand la commande a été commencé a etre préparé mais n'a jamais ete en cours de livraison)

## Cloud Storage

Le storage est très basique les images des gens sont juste stockés sur un cloud et supprimer après utilisation
Les images sont stockés sous cette forme nom#prenom.jpg

### Référence
[https://firebase.google.com/docs/firestore](https://firebase.google.com/docs/firestore)
[https://firebase.google.com/docs/storage](https://firebase.google.com/docs/storage)
