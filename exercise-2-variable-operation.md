# Exercice 2 - Variables et opérations 



## Séquence et affectation
* a,b,c sont trois variables de type entier; écrire les valeurs respectives des variables après chaque ligne de la séquence suivante :
```python
    a = 8
    b = 2
    c = 5
     
    a = a + b
    b = a - b 
    a = a - b

    c = a
    a = b
    b = c 
```

## Lecture de programmes, rôle des variables
* Voici deux programmes à comparer
```python
# Programme A 	

    print("Calcul de la somme de 3 nombres entiers")
    print()
    a = int(input("Donner un nombre = "))
    b = int(input("Donner un autre nombre = "))
    c = int(input("Donner un troisième nombre = "))
    s = a + b + c
    print()
    print("La somme des 3 nombres entiers est ",s)
    print()
    input("Taper entrée")

```

```python
# Programme B
    print("Calcul de la somme de 3 nombres entiers")
    print()
    a = int(input("Donner un nombre = "))
    s = a
    a = int(input("Donner un autre nombre = "))
    s = s + a
    a = int(input("Donner un troisième nombre = "))
    s = s + a
    print()
    print("La somme est des 3 nombres entiers est ",s)
    print()
    input("Taper entrée")
```

* Décider si ces deux programmes sont équivalents ; si oui, expliquer pourquoi. Si non, trouver des valeurs des variables pour lesquelles les deux programmes ne donnent pas le même résultat.
* Observer que les variables des programmes A et B n'ont pas tout à fait la même signification : dans le programme B, la variable a représente le nombre courant, celui que vient de donner l'utilisateur, et s représente la somme des nombres déjà donnés.
* Observer également que le programme B a moins de variables, mais plus de lignes d'instructions que le programme A.
