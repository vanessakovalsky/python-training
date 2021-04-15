# Exercice 4 - manipulation de fichier

## Objectifs 
* Savoir ouvrir et lire des donnnées dans un fichier
* Etre capable d'écrire dans un fichier

## Lire et écrire dans un fichier

* Créer un script qui lit le fichier loremipsum.txt (se trouvant dans le dossier resources)
* Afficher le contenu du fichier depuis le script
* Ajouter a la ligne 5 la chaine suivante (sur une nouvelle ligne) "Ma nouvelle chaine insérée dans mon fichier texte au milieu du lorem ipsum"

## Moyenne des notes

* Le fichier notes.txt (dans le dossier resources) contient les notes obtenues par des étudiants pour le cours de Python. Chaque ligne du fichier ne
contient qu’une note.
* Téléchargez le fichier notes.txt et enregistrez-le dans votre répertoire de travail. N’hésitez pas à l’ouvrir avec un éditeur de texte pour voir à quoi il ressemble.
* Créez un script Python qui lit chaque ligne de ce fichier, extrait les notes sous forme de float et les stocke dans une liste.
* Terminez le script en calculant et affichant la moyenne des notes avec deux décimales.


## Admis ou recalé

* Utiliser le même fichier notes.txt que pour l'exercice précédent
* Reprendre également le script écrit à l'exercice précédent nous allons le compléter
* Le script réécrira ensuite les notes dans le fichier notes2.txt avec une note par ligne suivie de « recalé » si la note est
inférieure à 10 et « admis » si la note est supérieure ou égale à 10. Toutes les notes seront écrites avec une décimale.
*  À titre d’exemple, voici les 3 premières lignes attendues pour le fichier notes2.txt :
    * 13.5 admis
    * 17.0 admis
    * 9.5 recalé

## Pour aller plus loin 

* Rechercher des palindromes dans un dictionnaire
    * Créer un fichier dico.py
    * Ce programme extrait les mots depuis un fichier dico.txt (à créer)
    * Il recherche et affiche les palindromes (les mots qui se lise dans les deux sens)