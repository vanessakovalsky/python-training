import jeu
import utilisateur

user_or_jeu = input('1 - User, 2 - Jeu')

if user_or_jeu == "1":
    liste = {'_nom':'david','_prenom':'vanessa'}
    user = utilisateur.Utilisateur(liste)
    print(user.mot_de_passe)
    print(user._nom)
elif user_or_jeu == "2":
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
else :
        print("Merci de saisir  un choix valide")