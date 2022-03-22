class Utilisateur:
    id = 0
    _prenom = ""
    _nom = ""# protégé
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
        if(str(valeur) and '?' in valeur ):
            self.__mot_de_passe = valeur
            return 'ok'
        else:
            return 'ko'

    def connexion(self, identifiant, password):
        file = open('utilisateurs.txt')
        lines = file.readlines()
        for line in lines:
            line_split = line.split(',')
            if identifiant == line_split[0] and password == line_split[6]:
                print('id ok + password ok')
                self.connecte = True
            else:
                continue
    
    nom = property(fget = get_nom, fset = set_nom)
    mot_de_passe = property (fget =  get_mot_de_passe, fset=set_mot_de_passe)

class Membre(Utilisateur):
    is_membre = True
    def isMembre(self):
        return True

    def ajouterASaCollection(self, jeu):
        return ('ajoute à sa collection')




