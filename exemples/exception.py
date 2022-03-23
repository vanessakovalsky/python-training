# age = input('QUel est votre age ?')

# try : 
#     nom_chaine = int(age)
# except:
#     print('Merci de saisir une valeur numérique')
#     age = input('QUel est votre age ?')
#     nom_chaine = int(age)


# print(nom_chaine)

# nom = input('Votre nom ?')

password = input('password')

if len(password)> 8 :
    print(password)
else :
    raise Exception('Le mot de passe doit faire au moins 8 caractères')

email = input('email')