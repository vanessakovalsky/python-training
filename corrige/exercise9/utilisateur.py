class Utilisateur:
    id = 0
    prenom = ""
    _nom = ""
    role = ""
    presentation = ""
    email = ""
    __mot_de_passe = "" # private mot_de_passe
    connecte = False

    def __init__(self, nom, prenom):
        self._nom = nom
        self.prenom = prenom
        self.__mot_de_passe = 'password'

    def get_nom(self):
        return self._nom.upper()

    def set_nom(self, valeur):
        self._nom = "ma regle a moi " + valeur

    def get_mot_de_passe(self):
        return 'toto' + self.__mot_de_passe

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
