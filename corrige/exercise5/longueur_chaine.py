# Écrire un script longeur_chaine.py, qui demande de saisir 2 chaînes de caractères et qui affiche la plus grande des 2 chaînes (celle qui a le plus de caractères)

valeur1 = input('Chaine 1 :')
valeur2 = input('Chaine 2 :')

print('La plus grande chaine')
if len(valeur1) > len(valeur2) : 
    print(valeur1)
else :
    print(valeur2)