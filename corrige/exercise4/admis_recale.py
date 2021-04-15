# Lit chaque ligne de ce fichier, extrait les notes sous forme de float et les stocke dans une liste.

fichier = open('notes.txt')
lines = fichier.readlines()
liste_note_float = []

for note in lines:
    note = float(note)
    if(note >= 10):
        note = str(note) + " admis\n"
    else :
        note = str(note) + " recalé\n"

    liste_note_float.append(note)

fichier2 = open("notes2.txt","w+")
fichier2.writelines(liste_note_float)
fichier.close()
