from modules.pair_impair import pair, impair
import modules.mini_maxi

type_donne = input('Pour entrer un texte taper 0, pour entrer un nombre taper 1')

valeur1 = input('Valeur 1 :')
valeur2 = input('Valeur 2 :')

if type_donne == "0": 
    mini = mini_maxi.mini(valeur1,valeur2)
    maxi = mini_maxi.maxi(valeur1,valeur2)
    print('Valeur la plus petite : ')
    print(mini)
    print('Valeur la plus grande :')
    print(maxi)
elif type_donne == "1":
    pair = pair_impair.pair(valeur1)
    impair = pair_impair.impair(valeur2)
    print('La valeur 1 est pair :', pair)
    print('La valeur 2 est impair :', impair)
else:
    print("Erreur de saisie")
