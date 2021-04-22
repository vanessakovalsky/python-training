# Exercice 8 - Conception orientée objet 

## Objectifs 
* Etre capable à partir d'un cahier des charges de définir les diagrammes des cas d'utilisation
* Savoir concevoir un modèle de classe à partir d'un cahier des charges

## Cahier des charges 
Cette secion présente l'application que nous allons concevoir en modèle orienté objet et que nous allons développer dans les exercices suivants

### Présentation de l'application :
* mettre en ligne une application web qui permettent à chaque joueur de stocker sa collection de jeux de sociétés, 
* ainsi que d’obtenir des informations sur les jeux existants, à venir, ceux auxquels il a joué 
* créer une communauté de joueur

### Fonctionnalités pour l’administrateur : 
    • Pouvoir créer / modifier / supprimer des jeux de sociétés avec les infos suivantes : 
        ◦ Nom du jeux
        ◦ Editeur
        ◦ Année de sortie
        ◦ Photos (plusieurs)
        ◦ Descriptif
        ◦ Catégorie (Familiale / Gestion / Figurine / Expert / Apéro)
        ◦ Durée
        ◦ Nombre de joueur
        ◦ Commentaires
    • Pouvoir créer / modifier / supprimer des utilisateurs avec les informations suivantes
        ◦ Identifant (pseudo)
        ◦ Nom
        ◦ Prénom
        ◦ Role (membre / administrateur)
        ◦ Présentation
        ◦ Avatar (photo)
        ◦ Email
        ◦ Mot de passe

### Fonctionnalités pour le membre du site 
    • - Pouvoir choisir dans la liste de jeux proposés par le site, les jeux qu’il possède et les ajouter à sa collection
    • Visualiser sa collection
    • Mettre un jeu dans un statut « prété à » avec soit la sélection d’un autre membre, soit un champs libre (pour saisir un ami ou une personne de la famille)
    • Dans la listes des jeux proposés par le site pouvoir signaler ceux par lesquels le membre est intéressé, et retrouver sa liste de souhait dans une page, qu’il sera possible de partager sur les réseaux sociaux.
    • Mettre à jour son profil utilisateur
    • Mettre des commentaires sur les fiches de jeux
#### Fonctionnalités pour le visiteur du site
    • Accéder à la liste des jeux du site
    • Accéder à la liste des membres du site
    • Accéder pour chaque membre à une fiche présentant le membre et sa collection de jeux

## Realiser les diagrammes des cas d'utilisation

* A l'aide de l'outil https://app.diagrams.net/ réaliser les différents diagrammes des cas d'utilisation que vous devez identifier à partir du cachier des charges fournis

## Réaliser les diagrammes de classes

* A l'aide de l'outil https://app.diagrams.net/ réaliser les différents diagrammes des classes que vous devez définir à partir du cachier des charges fournis et des cas d'utilisation que vous aurez définis


## Pour aller plus loin 

* Définir les cas d'utilisation et les diagrammes de classes pour les fonctionnalités supplémentaires suivantes

### Fonctionnalités supplémentaires

#### Pour l'administrateur
*  Coordonnées de localisation

#### Pour le membre
* Ajouter des photos et constitués des albums
* Pouvoir géolocaliser les autres membres sur une carte et les contacter
* Pouvoir soumettre de nouveaux jeux pour le site
* Pour chaque jeu, pouvoir enregistré les parties effectuées (date, nombre de joueur, commentaire)
* Si on peut enregistré les parties effectués, obtenir des statistiques sur ses parties

#### Pour les visiteurs :
* Accéder à une carte localisant les joueurs

#### Ajout d'un nouveau type de cible : Associations avec les fonctionnalités suivantes :
* Pouvoir s’enregistrer sur le site en tant qu’association (avec une validation d’un administrateur) avec les infos suivantes 
        ◦ Nom
        ◦ Localisation (adresse complète)
        ◦ Présentation
        ◦ Horaire et jour d’ouverture
        ◦ Logo
* Apparaitre sur la carte avec les membres, avec une autre couleur pour les associations
* Apparaitre dans un annuaire des associations sur le site 
* Pouvoir proposer des évènements qui apparaitrait dans un agenda public 