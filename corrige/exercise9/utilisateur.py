class Utilisateur:

    id = 0
    prenom = ""
    nom = ""
    role = "" 
    presentation = ""
    email = ""
    mot_de_passe = "" 
    connecte = False

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


