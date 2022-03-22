class Jeu():
    identifiant_du_jeu = ""
    nom_du_jeu = ""
    editeur = ""
    annee_de_sortie = ""
    descriptif = ""
    categorie  = ''
    duree = ''
    nombre_de_joueurs = ''

    def __init__(self):
        self.categorie = 'Familiale'

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
        jeu_a_afficher = self.trouverunjeu(identifiant_du_jeu)
        return jeu_a_afficher

    def supprimerJeu(self, identifiant_du_jeu):
        jeu_a_supprimer = self.trouverunjeu(identifiant_du_jeu)
        fichier = open('./corrige/exercise9/jeux.txt','r')
        liste_jeux = fichier.readlines()
        fichier.close()
        for jeu in liste_jeux:
            if jeu_a_supprimer ==  jeu:
                liste_jeux.remove(jeu_a_supprimer)
        fichier = open('./corrige/exercise9/jeux.txt','w')
        fichier.writelines(liste_jeux)
        fichier.close()

    def trouverunjeu(self,id):
        liste_jeux = self.listeJeu()
        jeu_a_afficher = ''
        for jeu in liste_jeux:
            jeu_split = jeu.split(',')
            if jeu_split[0] == id:
                jeu_a_afficher = jeu_split
        return jeu_a_afficher