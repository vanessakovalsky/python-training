# Constituez une liste semaine contenant les 7 jours de la semaine.
jours_semaine = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche']

# récupérez-vous seulement les 5 premiers jours de la semaine d’une part, 
jours_semaine[0:4]
# et ceux du week-end d’autre part ? Utilisez pour cela l’indiçage.
jours_semaine[5:6]

# Cherchez un autre moyen pour arriver au même résultat (en utilisant un autre indiçage).

jours_semaine[-7:-2]
jours_semaine[-2:7]

# Trouvez deux manières pour accéder au dernier jour de la semaine.
jours_semaine[6]
jours_semaine[-1]

#. Inversez les jours de la semaine en une commande.

jours_semaine.reverse()