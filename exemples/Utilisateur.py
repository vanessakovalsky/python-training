class Utilisateur:
    # Propriétés de l'utilisateur
    nom = ""
    prenom = ''
    age = int()

    # Constructeur
    def __init__(self, nom, prenom):
        self.nom = nom
        self.age = 42
        self.prenom = prenom

    # Méthodes la classe utilisateur
    def jeMappelle(self):
        nom_complet = self.nom + self.prenom
        return 'Je m\'appelle' + nom_complet

    def jaiXAge(self):
        return 'J\'ai ' + self.age + 'ans'

    # Destructeur appelé à la suppression de l'objet 
    def __del__(self):
        return 'L objet a bien été supprimé'