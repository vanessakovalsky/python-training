import jeu
import utilisateur
import membre
import admin

user_or_jeu = input('1 - User, 2 - Jeu')

if user_or_jeu == "1":
    choix = input('1-liste 2-Se connecter')
    dico = {'_pseudo':'vdavid','_nom':'david','_prenom':'vanessa','role':'membre','presentation':'Une description','email':'v.david@kovalibre.com', '__mot_de_passe':'UnSuperPassword456!'}
    user = utilisateur.Utilisateur(dico)
    if choix == '1':
        liste_utilisateurs = user.ListeUtilisateur()
        for one_user in liste_utilisateurs:
            print(one_user)
    elif choix == "2":
        login = input('Identifiant')
        password = input('Mot de passe')
        user.connexion(login, password)
        print('Utilisateur connecté')
        if user.connecte :
            if user.role == "membre":
                print('Modification de votre fiche')
                membre1 = membre.Membre(dico)
                membre1.connecte = True
                membre1.modifieMesInfos(dico)
            elif user.role == 'admin':
                choix_admin = input('1-Ajouter un membre 2-Supprimer un membre')
                if choix_admin == "1":
                    dico['_nom'] = input('Nom')
                    dico['_prenom'] = input('prenom')
                    nouvelle_donnees = ','.join(dico.values())
                    user.AjoutUtilisateur(nouvelle_donnees)
                elif choix_admin == "2":
                    id_user_supp = input('Quel est le pseudo de l\'utilisateur que vous voulez supprimer?')
                    user.SupprimeUtilisateur(id_user_supp)
elif user_or_jeu == "2":
    jeu = jeu.Jeu()
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
        print(jeu.supprimerJeu(identifiant))
    else :
        print("Merci de saisir  un choix valide")
else :
        print("Merci de saisir  un choix valide")