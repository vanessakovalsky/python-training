# from rentabilite import CalculatriceRentabilite

# calculatrice1 = CalculatriceRentabilite()
# montant = input('Quel est le montant de départ ?')
# calculatrice1.montant_depart = float(montant)
# print(calculatrice1.calculRentabilite())

# calculatrice2 =  CalculatriceRentabilite()
# calculatrice2.montant_depart = 78542
# print(calculatrice2.montant_depart)

from Utilisateur import Utilisateur

vanessa = Utilisateur("David",'Vanessa')
print(vanessa.jeMappelle())

jean = Utilisateur("NomDeJean",'Jean')
print(jean.jeMappelle())