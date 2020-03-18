# Projet Realestate (01/2020)

Machine Learning Project - Prediction House Prices (terrain, appartement ou maison) en Aquitaine

## Pré-requis

* Git
* Docker

## Usages

* Utilisez `git clone` pour récupérer le repo en locale sur votre laptop.
* Pour le fichier `auth.env`, reprendre le `auth-a-remplir.env` dans le dossier `docker/`, le renommer et remplacer par vos identifiants et vos mots de passe.
* Une fois tous les dossiers et fichiers créés, en ligne de commande, se positionner dans le dossier `docker`.
* Puis lancer une commande `docker-compose up --build` pour démarrer le container.

Vous aurez maintenant accès à notre outil de prédiction de biens immobiliers à l'adresse `localhost:5000/`.

Vous n'avez alors qu'à rentrer les informations du bien que vous souhaitez estimer et cliquez sur le bouton `Submit`.

## Précautions d'usages

Il se peut que lors de certaines connexions, la mise en route de notre outil prenne un peu de temps :

* Si c'est votre première utilisation, il faut laisser le temps à tous nos outils sous-jacents de s'installer,
* Si vous avez déjà utilisé notre outil, vous pouvez avoir une mise à jour des données qui empêche son utilisation immédiate.

@DJML (Damien Thiberge, Julien Lagoutte, Mehdi Ikbal, Laurent Pacquet).