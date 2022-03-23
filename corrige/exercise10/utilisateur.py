class Utilisateur:
    id = 0
    _prenom = ""
    _nom = ""# protégé
    _pseudo = ""
    role = "" # public
    presentation = ""
    email = ""
    __mot_de_passe = "" # private mot_de_passe
    connecte = False
    _keys = ['_nom', '_prenom' ]

    # Méthode 1 avec une boucle simple
    def __init__(self, dictionnaire) :
        # self._nom = dictionnaire['nom']
        # self._prenom = dictionnaire['prenom']
        # self.role = dictionnaire['role']
        for cle, valeur in dictionnaire.items():
            setattr(self, cle, valeur)

    # Méthode 2 avec une liste de valeur modifiables et des tests
    # def __init__(self, liste):
    #     for cle, valeur in liste.items():
    #         if cle in self._keys:
    #             setattr(self, cle, valeur)
    #         else:
    #             setattr(self, cle, None)
    #     self.__mot_de_passe = 'password'
        
    def get_nom(self):
        return self._nom.upper()

    def set_nom(self, valeur):
        self._nom = "ma regle a moi " + valeur

    def get_mot_de_passe(self):
        mot_de_passe = ''
        for caractere in self.__mot_de_passe:
            mot_de_passe += '*'
        return mot_de_passe

    def set_mot_de_passe(self,valeur):
        if(len(valeur) > 8 and not valeur.isalpha() and not valeur.isnumeric() ):
            self.__mot_de_passe = valeur
            print('ok')
            return 'ok'
        else:
            print('ko')
            return 'ko'

    def ListeUtilisateur(self) : 
        #affiche la liste des utilisateurs depuis un fichier utilisateurs.txt
        fichier = open('./corrige/exercise10/utilisateurs.txt','r')
        liste_utilisateurs = fichier.readlines()
        fichier.close()
        return liste_utilisateurs

    def AjoutUtilisateur(self, chaine_caractere_donnees) : 
        #permet l'ajout d'un utilisateur depuis une saisie de l'utilisateur et enregistre l'utilisateur dans le fichier utilisateurs.txt (à la suite des autres)
        user = '\n' + chaine_caractere_donnees
        fichier = open('./corrige/exercise10/utilisateurs.txt','a')
        fichier.write(user)
        fichier.close()
        return user + 'L\'utilisateur a bien été ajouté'

    def VoirUtilisateur(self, idutilisateur) :
        # permet d'afficher les informations d'un utilisateur précis en fonction de son identifiant (paramètre à demander à l'utilisateur)
        user_a_afficher = self.__trouverunuser(idutilisateur)
        return user_a_afficher

    def SupprimeUtilisateur(self, idutilisateur) :
        # supprime un jeu du fichier utilisateurs.txt à partir de son identifiant
        user_a_supprimer = self.__trouverunuser(idutilisateur)
        liste_users = self.ListeUtilisateur()
        for user in liste_users:
            if user_a_supprimer ==  user:
                liste_users.remove(user_a_supprimer)
        fichier = open('./corrige/exercise10/utilisateurs.txt','w')
        fichier.writelines(liste_users)
        fichier.close()

    def __trouverunuser(self,id):
        liste_user = self.ListeUtilisateur()
        user_a_afficher = ''
        for user in liste_user:
            user_split = user.split(',')
            if user_split[0] == id:
                user_a_afficher = ','.join(user_split)
        return user_a_afficher

    def connexion(self, identifiant, password):
        file = open('./corrige/exercise10/utilisateurs.txt')
        lines = file.readlines()
        for line in lines:
            line_split = line.split(',')
            if identifiant == line_split[0] and password == line_split[6]:
                self.connecte = True
            else:
                continue
    
    nom = property(fget = get_nom, fset = set_nom)
    mot_de_passe = property (fget =  get_mot_de_passe, fset=set_mot_de_passe)