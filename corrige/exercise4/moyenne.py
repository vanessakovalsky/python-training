# Lit chaque ligne de ce fichier, extrait les notes sous forme de float et les stocke dans une liste.

fichier = fopen('notes.txt')
lines = fichier.readlines()
liste_note_float = []

for note in lines:
    liste_note_float.append(float(note))

print('Moyenne : ')
print(somme(liste_note_float)/len(liste_note_float))