# Exercice 3 - Liste

## Objectifs : 
* Créer des listes et récupérer les données de celle-ci
* Manipuler les fonctions range et list

## Jours de la semaine
* Constituez une liste semaine contenant les 7 jours de la semaine.
1. À partir de cette liste, comment récupérez-vous seulement les 5 premiers jours de la semaine d’une part, et ceux du
week-end d’autre part ? Utilisez pour cela l’indiçage.
2. Cherchez un autre moyen pour arriver au même résultat (en utilisant un autre indiçage).
3. Trouvez deux manières pour accéder au dernier jour de la semaine.
4. Inversez les jours de la semaine en une commande.

## Saisons
* Créez 4 listes hiver, printemps, ete et automne contenant les mois correspondants à ces saisons. 
* Créez ensuite une liste saisons contenant les listes hiver, printemps, ete et automne. 
* Prévoyez ce que renvoient les instructions suivantes, puis vérifiez-le dans l’interpréteur :
1. saisons[2]
2. saisons[1][0]
3. saisons[1:2]
4. saisons[:][1]. Comment expliquez-vous ce dernier résultat ?

## Table de multiplication par 9
* Affichez la table de multiplication par 9 en une seule commande avec les instructions range() et list().

## Nombres pairs
* Répondez à la question suivante en une seule commande. Combien y a-t-il de nombres pairs dans l’intervalle [2, 10000] inclus ?

## Pour aller plus loin

* On va créer un jeu de carte
    * Créer un programme jeu_de_cartes.py, qui crée une liste avec l’ensemble des cartes soit :1,2,...10,V,D,R sans spécifier la couleur. On se permettra une saisie manuelle des valeurs descartes.
    * Contrôler le contenu de votre liste en l’affichant
    * Créer une deuxième liste de couleur
    * Afficher l'ensemble du jeu de carte (une valeur de chaque couleur)
* Copier le script jeu_de_cartes.py et renommer la copie en jeu_de_cartes2.py avec deux jeux de 52 cartes 
    * Afficher le contenu de vos deux listes en les affichang
    * On tire 10 cartes au hasard dans chaque jeu. Faire afficher les 10 cartes tirées pour chacun des 2 jeux.
    * Trouver les cartes identiques dans les 2 tirages.