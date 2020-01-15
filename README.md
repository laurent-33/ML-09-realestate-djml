# Projet Realestate (01/2020)

## Méthode d'importation du projet et mise en oeuvre

1. Récupération des fichiers :
    - se placer dans le dossier parent
    - ouvrir un terminal de commande à partir de ce dossier
    - taper la commande suivante pour commencer le téléchargement :<br>
        $ git clone https://github.com/Simplon-IA-Bdx-1/realestate-djml.git
    - renommer le lien remote si besoin avec cette commande :<br>
        $ git remote rename origin simplon

2. Afin de garder la branche master propre, l'on utilise des branches features séparées:<br>
    - aller sur la branche develop si vous n'y êtes pas déjà<br>
    $ git checkout develop
    - créer une nouvelle branche de travail<br>
    $ git flow feature start <prénom_de_la_personne-nom_de_la_modification>
