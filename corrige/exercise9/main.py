import jeu


jeu = Jeu()

choix = input('Choisir 1 - Liste, 2 - Ajout, 3 - Voir un jeu, 4 - Supprimer')

if choix == "1":
    jeu.listeJeu()
elif choix == "2":
    jeu.ajoutJeu()
elif choix == "3":
    identifiant = input('Nom du jeu')
    jeu.voirJeu(identifiant)
elif choix == "4":
    identifiant = input('Nom du jeu')
    jeu.supprimerJeu(identifiant)
else :
    print("Merci de saisir  un choix valide")