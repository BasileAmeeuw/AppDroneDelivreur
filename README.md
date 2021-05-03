# AppDroneDelivreur
Ce repo contient deux fichier .aia que vous pouvez ouvrir dans kodular. C'est fichier sont les deux applications indispensables à notre projets le drone livreur

Voici le lien pour la documentation : [Docu app BarmanApp]() et [Docu app DelIvre]()

Voici une petite explication sur la database: [Vidéo d'explication](https://www.youtube.com/watch?v=zAVjq34hjDs&feature=youtu.be), l'intégration de la BDD est expliquée ci-dessous avec l'algorithme de la reconnaissance faciale

Pour ce qui est de l'algorithme de reconnaissance faciale. Voici le lien github de la librairie utilisée. [Reconnaissance_faciale](https://github.com/ageitgey/face_recognition) Cependant ici après sont expliquées quelques cas d'utilisation dans notre cas.

Vous pouvez suivre leur github pour l'installation qui est très bien expliquée.
Ensuite dans notre Use Case on utilise la base de donnée d'une facon particulière pour l'algorithme de reconnaissance.

## Intégration de la base de donnée

![Intégration base de donnée](https://github.com/BasileAmeeuw/AppDroneDelivreur/blob/main/Image%20github/IntegrationBDD.png)

## Comment on récupère la bonne commande (ici pour drone 5)

![Recupération BDD](https://github.com/BasileAmeeuw/AppDroneDelivreur/blob/main/Image%20github/RecupBDD.png)

## Essaie d'intégration de la photo dans l'algorithme
Etant donné qu'on ne peut pas prédéfinir le sens de la photo que l'utilisateur va prendre, on essaye de retourner la photo dans tous les sens jusqu'a ce que ca fonctionne

![Rotation image](https://github.com/BasileAmeeuw/AppDroneDelivreur/blob/main/Image%20github/photo4face.png)

## Algorithme en tant que tel
Pour plus d'info aller voir sur leur repo github

![reco_algo](https://github.com/BasileAmeeuw/AppDroneDelivreur/blob/main/Image%20github/reco_algo.png)

## Suppression des données après livraison
En effet pour ne pas etre soumis a une obligation d'inscription et une signature de droit d'utilisation, aucune donnée n'est gardée afin de respecter les RGPD

![RGPD](https://github.com/BasileAmeeuw/AppDroneDelivreur/blob/main/Image%20github/suppressionBDD.png)
