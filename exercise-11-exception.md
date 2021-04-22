# Exercice 11 - Gestion des exceptions

## Objectifs 
* Etre capable d'identifier une exception et de la gérer lors de la saisie
* Déclencher une exception

## Récupérer une exception 
* Lors de l'ajout d'un jeu, vérifier que les données saisies soient du bons type en castant les données qui viennent de input
* Si ce n'est pas le bon type récupérer l'exception et afficher un message à l'utilisateur en l'invitant à ressaisir la donnée

## Déclencher une exception
* Lors de l'ajout d'un jeu dans le fichier, déclencher une exception de type ValueError si le jeu exsite déjà dans la liste
* Puis afficher un message à l'utilisateur


## Pour aller plus loin : 
* A partir de cette explication : http://www.xavierdupre.fr/app/teachpyx/helpsphinx/c_exception/exception.html#definir-ses-propres-exceptions 
* Définir sa propre classe d'exception pour gérer les doublons dans les listes de jeux et d'utilisateurs