## Exercice 14 - DB API

## Objectifs 
* Lire et écrire des données dans une base de données

## Pré-requis 
* installer un moteur de base de données (par exemple sqllite)
* Créer une base de données et importer le fichier sql https://github.com/vanessakovalsky/php-oo/blob/master/kingoludo.sql 

## Lire les données
* A l'aide du module sqlite3, modifier la classe Jeu et faire en sorte que les données de la liste viennent de la base de données et plus du fichier
* Afficher un jeu (via la fonction voirJeu) depuis les données de la base de données

## Ecrire / modifier / supprimer des données

* Modifier les fonction ajoutJeu et supprimerJeu pour qu'elles utilisent la base de données à la place des fichiers
* Ajouter une fonction modifierJeu pour permettre la modification d'un jeu existant

## Pour aller plus loin : basculer les utilisateurs en base de données

* Rajouter une classe ConnexionDB, qui permettra de centraliser la connexion à la base de donnée et sera appelé par la classe Jeu et par les autres classes qui ont besoins d'utiliser la base de données
* Reprendre la classe Utilisateur et modifier les différentes fonctions pour que les données ne proviennent plus du fichier texte mais de la base de données