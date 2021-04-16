# Déterminer si le nombre entrer est pair ou non

def pair(valeur):
    if valeur % 2 == 0 :
        print("La fonction Pair retourne True pour la valeur {0}". format(valeur))

def impair(valeur):
    if valeur % 2 != 0 :
        print("La fonction Impair retourne True pour la valeur {0}". format(valeur))

# On demande la valeur
valeur = int(input('Entrer un nombre : '))

# On appelle les deux fonctions
pair(valeur)
impair(valeur)
