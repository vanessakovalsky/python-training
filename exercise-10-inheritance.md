# Exercice 10 - Constructeur, encapsulation et Héritage

## Objectifs : 
* Définir un constructeur pour créer des objets avec des données 
* Encapsuler ces données
* Savoir définir une classe enfant 

## Ajouter un constructeur a notre classe utilisateur

* Sur la classe Utilisateur, ajouter un constructeur (méthode __init__ ) qui prend en paramètre un dictionnaire
* Pour chaque clé du dictionnaire affecter la valeur à l'attribut correspondant

## Encapsuler les données

* Pour l'attribut mot de passe : 
    * définir une fonction getMotDepasse qui affiche des étoiles à la places des caractères pour ne pas afficher le mot de passe en clair
    * définir une fonction setMotDePasse qui vérifie que le mot de passe contient au moins 8 caractères et un chiffre et une lettre
    * utiliser ses deux fonctions sur l'attribut mot de passe avec la méthode property

## Spécialiser les classes utilisateurs
* Créer deux classe Membre et Admin qui hérite toute les deux de la classe utilisateur
* Dans la classe membre, créer une méthode qui permette à l'utilisateur de modifier ses propres informations (et uniquement les siennes) après s'être connecté
* Dans la classe admin, déplacer la fonction d'ajout et de suppression de la classe utilisateur, car seul celui-ci doit pouvoir créer et supprimer de nouveaux utilisateurs
* Reprendre le script main pour afficher une étape supplémentaire à l'utilisateur lorsqu'il se connecte : si c'est un admin lui permettre d'ajouter / supprimer un utilisateur, si c'est un membre lui permettre de modifier ses informations

## Pour aller plus loin : Définir une classe commune pour les actions de lecture, écriture

* Créer une classe CRUD 
* Celle-ci contiendra des méthodes génériques permettant de : 
    * renvoyer une liste des éléments d'un fichier à partir de son nom
    * renvoyer un élement spécifique d'un fichier à partir du nom du fichier et d'un identifiant
    * ajouter une ligne dans un fichier à partir du nom du fichier et des données à ajouter
    * supprimer un élement spécifique d'un fichier à partir du nom du fichier et de l'identifiant de l'élément à supprimer
* Faire hériter les classes Jeu et Utilisateur de cette classe Crud et modifier le code pour éviter de dupliquer le code en utilisant cette classe parente.

