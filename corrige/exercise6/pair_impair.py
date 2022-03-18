# Déterminer si le nombre entrer est pair ou non

def pair(valeur):
    if valeur % 2 == 0 :
        return "La fonction Pair retourne True pour la valeur " + str(valeur)

def impair(valeur):
    if valeur % 2 != 0 :
        return "La fonction Impair retourne True pour la valeur " + str(valeur)

# On demande la valeur
valeur = int(input('Entrer un nombre : '))

# On appelle les deux fonctions
result = pair(valeur) if pair(valeur) else impair(valeur)
print(result)

