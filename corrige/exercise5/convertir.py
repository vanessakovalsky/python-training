
#conversion euros en dollars.

devise = input('Dans quel devise allez vous entrer le montant : E ou $')

if devise != 'E' or devise != '$' :
    print('Erreur dans le choix de la devise')
else :
    taux = 1.2
    montant = input('Quel montant souhaitez vous convertir ?')
    if devise == 'E' :
        conversion = float(montant) / taux
    elif devise == '$' :
        conversion = float(montant) * taux

    print(conversion)
