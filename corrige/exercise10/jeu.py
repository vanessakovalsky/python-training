class Jeu():
    identifiant_du_jeu = ""
    nom_du_jeu = ""
    editeur = ""
    annee_de_sortie = ""
    descriptif = ""
    categorie  = 'Familiale'
    duree = ''
    nombre_de_joueurs = ''
    toto = ''

    def __init__(self, liste_parametre):
        print('constructeur class jeu')
        self.nom_du_jeu = liste_parametre['nom_du_jeu'] 
        self.editeur = liste_parametre['editeur']
        return 'ok l\'objet est créé'

    def listeJeu(self):
        pass

    def ajoutJeu(self):
        pass

    def voirJeu(self, identifiant_du_jeu):
        pass

    def supprimerJeu(self, identifiant_du_jeu):
        pass