class Jeu():
    __nom_du_jeu = ""
    __editeur = ""
    __annee_de_sortie = ""
    __descriptif = ""
    __categorie  = ''
    __duree = ''
    __nombre_de_joueurs = ''

    def __init__(self):
        self.setCategorie('Familiale')
        self.__identifiant_du_jeu = 178

    def getIdentifiantDuJeu(self):
        return self.__identifiant_du_jeu

    def setNomDuJeu(self, nom):
        if type(nom) == 'str':
            self.nom_du_jeu = nom
        else :
            return 'Erreur : merci de saisir une chaine de caractère valide'

    def setCategorie(self, categorie):
        if categorie == 'Familiale':
            self.__categorie = categorie
        elif categorie ==  'Expert':
            self.__categorie = categorie
        else: 
            return 'Erreur la catégorie n\'est pas valide'


    def listeJeu(self):
        fichier = open('./corrige/exercise9/jeux.txt','r')
        liste_jeux = fichier.readlines()
        fichier.close()
        return liste_jeux

    def ajoutJeu(self, nom_du_jeu, editeur, annee_de_sortie):
        jeu = '\n' + nom_du_jeu + ',' + editeur + ',' + annee_de_sortie
        fichier = open('./corrige/exercise9/jeux.txt','a')
        fichier.write(jeu)
        fichier.close()
        return jeu + 'Le jeu a bien été ajouté'

    def voirJeu(self, identifiant_du_jeu):
        if type(identifiant_du_jeu) == 'str':
            jeu_a_afficher = self.__trouverunjeu(identifiant_du_jeu)
            return jeu_a_afficher

    def supprimerJeu(self, identifiant_du_jeu):
        jeu_a_supprimer = self.__trouverunjeu(identifiant_du_jeu)
        liste_jeux = self.listeJeu()
        for jeu in liste_jeux:
            if jeu_a_supprimer ==  jeu:
                liste_jeux.remove(jeu_a_supprimer)
        fichier = open('./corrige/exercise9/jeux.txt','w')
        fichier.writelines(liste_jeux)
        fichier.close()
        return 'Le jeu a bien été supprimé'

    def __trouverunjeu(self,id):
        liste_jeux = self.listeJeu()
        jeu_a_afficher = ''
        for jeu in liste_jeux:
            jeu_split = jeu.split(',')
            if jeu_split[0] == id:
                jeu_a_afficher = jeu_split
        return jeu_a_afficher