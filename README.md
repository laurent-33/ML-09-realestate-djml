# Projet Realestate (01/2020)

## Méthode d'importation du projet et mise en oeuvre

1. Récupération des fichiers :
    - se placer dans le dossier parent
    - ouvrir un terminal de commande à partir de ce dossier
    - taper la commande suivante pour commencer le téléchargement :<br>
        $ git clone https://github.com/Simplon-IA-Bdx-1/realestate-djml.git
    - renommer le lien remote si besoin avec cette commande :<br>
        $ git remote rename origin <nom_de_la_remote>
    - se placer sur la branche master :<br>
        $ git checkout master
    - initialiser le workflow (branches develop, feature , ...) :<br>
        $ git flow init

2. Avant toute modification, récupérer les dernières versions des branches principales :
    - Pour passer d'une branche à l'autre :<br>
    $ git checkout <nom_de_la_branche_destination (master ou develop)>
    - Appliquer cette commande sous les branches master et develop :<br>
    $ git pull

3. Afin de garder la branche master propre, nous utilisons des branches features séparées :<br>
    - aller sur la branche develop si vous n'y êtes pas déjà<br>
    $ git checkout develop
    - créer une nouvelle branche feature (branche de travail)<br>
    $ git flow feature start <prénom_de_la_personne-nom_de_la_modification>
    - intégrer dans git les fichiers modifiés<br>
    $ git add <nom_du_fichier>
    - commit des modifications sur la branche feature<br>
    $ git commit -m "<nom_du_contibuteur> : <action_effectuée>" 
    - autres commits
    - clôturer la branche feature (la branche est supprimée définitivement)<br>
    $ git flow feature finish <prénom_de_la_personne-nom_de_la_modification>
    - nous nous retrouvons automatiquement sur la branche develop qui a intégrée les modifications précédentes et vous pouvez mettre à jour le dépôt distant avec la commande :<br>
    $ git push