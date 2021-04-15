# Créez 4 listes hiver, printemps, ete et automne contenant les mois correspondants à ces saisons. 
hiver = ['janvier,fevrier,mars']
printemps = ['avril','mai','juin']
ete = ['juillet','aout','septembre']
automne = ['octobre', 'novembre', 'decembre']

# Créez ensuite une liste saisons contenant les listes hiver, printemps, ete et automne. 
saisons = [hiver, printemps, ete, automne ]
print(saisons)

# Prévoyez ce que renvoient les instructions suivantes, puis vérifiez-le dans l’interpréteur :
print(saisons[2])# ['juillet','aout','septembre']
print(saisons[1][0]) # avril
print(saisons[1:2]) # [['avril', 'mai', 'juin']]
print(saisons[:][1]) # ['avril', 'mai', 'juin']