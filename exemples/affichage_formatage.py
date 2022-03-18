# Insertion d'une variable dans un print 
variable = 'un contenu dans une variable'
print(f'Un message avec une {variable}')

# On utilise les % : https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting 
print("C'est dans % d ans je m'en irai j'entends le loup le renard chanter" %n)


nom = input('Votre nom')
prenom = input('Votre prenom')

chaine_caractere3 = 'Mon nom est {nom} et mon prenom est {prenom}'.format(prenom =  prenom, nom = nom)
chaine_caractere2 = 'Mon nom est {} et mon prenom est {}'.format(nom, prenom)
chaine_caractere = 'Mon nom est {0} et mon prenom est {1}'.format(nom, prenom)
print(chaine_caractere)
print(chaine_caractere2)
print(chaine_caractere3)
