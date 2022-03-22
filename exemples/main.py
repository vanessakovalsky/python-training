# from rentabilite import CalculatriceRentabilite

# calculatrice1 = CalculatriceRentabilite()
# montant = input('Quel est le montant de départ ?')
# calculatrice1.montant_depart = float(montant)
# print(calculatrice1.calculRentabilite())

# calculatrice2 =  CalculatriceRentabilite()
# calculatrice2.montant_depart = 78542
# print(calculatrice2.montant_depart)

from Utilisateur import *

vanessa = Utilisateur("David",'Vanessa')
print(vanessa.jeMappelle())

jean = Utilisateur("NomDeJean",'Jean')
print(jean.jeMappelle())

pauline = Admin('Nom','Pauline')
print(pauline.jeMappelle())
print(Admin.is_admin)

print(pauline.nom)
print(pauline.is_membre)


visiteur1 = Visiteur()
print(visiteur1.adresse)

print(pauline.adresse)