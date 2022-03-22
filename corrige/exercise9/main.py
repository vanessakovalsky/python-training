from jeu import Jeu


jeu = Jeu()

choix = input('Choisir 1 - Liste, 2 - Ajout, 3 - Voir un jeu, 4 - Supprimer')

if choix == "1":
    for un_jeu in jeu.listeJeu():
        print(un_jeu)
elif choix == "2":
    nom_du_jeu = input('Nom du jeu')
    editeur = input('Editeur du jeu')
    annee_de_sortie = input('Annee de sortie')
    print(jeu.ajoutJeu(nom_du_jeu, editeur, annee_de_sortie))
elif choix == "3":
    identifiant = input('Nom du jeu')
    print(jeu.voirJeu(identifiant))
elif choix == "4":
    identifiant = input('Nom du jeu')
    jeu.supprimerJeu(identifiant)
else :
    print("Merci de saisir  un choix valide")