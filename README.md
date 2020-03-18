# Projet Realestate (01/2020)

## Méthode d'importation du projet et mise en oeuvre

1. Récupération des fichiers :
    - se placer dans le dossier parent
    - ouvrir un terminal de commande à partir de ce dossier
    - taper la commande suivante pour commencer le téléchargement :  
    `$ git clone https://github.com/Simplon-IA-Bdx-1/realestate-djml.git`
    - renommer le lien remote si besoin avec cette commande :  
    `$ git remote rename origin <nom_de_la_remote>`
    - se placer sur la branche master :  
    `$ git checkout master`
    - initialiser le workflow (branches develop, feature , ...) :  
    `$ git flow init`
    - valider les noms par défauts qui s'affichent (touche "entrée" plusieurs fois)

2. Avant toute modification, récupérer les dernières versions des branches principales :
    - Pour passer d'une branche à l'autre :  
    `$ git checkout <nom_de_la_branche_destination (master ou develop)>`
    - Appliquer cette commande sous les branches master et develop :  
    `$ git pull`

3. Afin de garder la branche master propre, nous utilisons des branches features séparées :  
    - aller sur la branche develop si vous n'y êtes pas déjà  
    `$ git checkout develop`
    - créer une nouvelle branche feature (branche de travail)  
    `$ git flow feature start <prénom_de_la_personne-nom_de_la_modification>`
    - intégrer dans git les fichiers modifiés  
    `$ git add <nom_du_fichier>`
    - commit des modifications sur la branche feature  
    `$ git commit -m "<nom_du_contibuteur> : <action_effectuée>"`
    - autres commits
    - clôturer la branche feature (la branche est supprimée définitivement)  
    `$ git flow feature finish`
    - nous nous retrouvons automatiquement sur la branche develop qui a intégrée les modifications précédentes, vous pouvez le vérifier avec la commande suivante :
    `$ git branch`
    - avant d'envoyer vos modifications, il faut au préalable récupérer la dernière version de la branche develop (si d'autres personnes ont travaillé entre-temps dessus) :
    `$ git pull`
    - traiter les éventuelles collisions, si vous êtes dans une étape de merging (avec VS code par exemple)
    - vous pouvez ensuite mettre à jour le dépôt distant avec vos dernières modifications :  
    `$ git push`
