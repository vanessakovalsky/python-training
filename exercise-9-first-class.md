# Exercice 9 - Première classes

## Objectifs :
* Savoir définir une classe, ses attributs et méthodes 
* Etre capable d'instancier un objet depuis une classe et de l'utiliser

## La classe Jeu
* Définir une classe Jeu avec les attributs suivants :
    * Nom du jeux
    * Editeur
    * Année de sortie
    * Descriptif
    * Catégorie (Familiale / Gestion / Figurine / Expert / Apéro)
    * Durée
    * Nombre de joueur
* Dans cette classe définir les méthodes suivantes : 
    * ListeJeu : affiche la liste des jeux depuis un fichier jeux.txt 
    * AjoutJeu : permet l'ajout d'un jeu depuis une saisie de l'utilisateur et enregistre le jeu dans le fichier jeux.txt (à la suite des autres)
    * VoirJeu(iddujeu) : permet d'afficher les informations d'un jeu précis en fonction de son identifiant (paramètre à demander à l'utilisateur)
    * SupprimeJeu(iddujeu) : supprime un jeu du fichier jeu.txt à partir de son identifiant
* Créer un script main.py qui appelle la classe et demande à l'utilisateur quelle action il souhaite faire (parmi les 4 disponibles) puis appelle la fonction correspondante selon le choix de l'utilisateur

## Classe Utilisateur
* Définir une classe Utilisateur avec les attributs suivants :
    * Identifant (pseudo)
    * Nom
    * Prénom
    * Role (membre / administrateur)
    * Présentation
    * Email
    * Mot de passe
* Dans cette classe définir les méthodes suivantes : 
    * ListeUtilisateur : affiche la liste des utilisateurs depuis un fichier utilisateurs.txt 
    * AjoutUtilisateur : permet l'ajout d'un utilisateur depuis une saisie de l'utilisateur et enregistre l'utilisateur dans le fichier utilisateurs.txt (à la suite des autres)
    * VoirUtilisateur(idutilisateur) : permet d'afficher les informations d'un utilisateur précis en fonction de son identifiant (paramètre à demander à l'utilisateur)
    * SupprimeUtilisateur(idutilisateur) : supprime un jeu du fichier utilisateurs.txt à partir de son identifiant
    * SeConnecter(identifiant, motdepasse) : vérifier si les informations saisies par l'utilisateur correspondent à celle de l'utilisateur puis lui donné le statut connecté
* Compléter le script main.py qui demande si l'on veut travailler sur les jeux ou sur les utilisateurs puis appelle la classe et demande à l'utilisateur quelle action il souhaite faire (parmi les 4 disponibles) puis appelle la fonction correspondante selon le choix de l'utilisateur

## Aller plus loin 

* Définir la classe commentaire qui permet à l'utilsiateur d'ajouter un commentaire sur un jeu
* Définir la classe collection, qui permet à un utilsiateur de définir certains jeux comme faisant partie de sa collection
* Permettre la gestion de photos, en copiant des fichiers dans un dossier spécifique et en stockant leur chemin dans le fichier pour que l'utilisateur puisse accéder à l'image associée au jeu