# Lire le fichier loremipsum.txt (se trouvant dans le dossier resources)

fichier = open("../../resources/loremipsum.txt","r+")

#  Afficher le contenu du fichier depuis le script
print(fichier.read())

# Ajouter a la ligne 5 la chaine suivante (sur une nouvelle ligne) "Ma nouvelle chaine insérée dans mon fichier texte au milieu du lorem ipsum"

fichier.seek(0) # On remet le pointeur au début du fichier
lines = fichier.readlines() # Liste des lignes

print(lines)

lines[4] = lines[4] + "\nMa nouvelle chaine insérée dans mon fichier texte au milieu du lorem ipsum\n"
# Ou bien : lines.insert(4, "\nMa nouvelle chaine insérée dans mon fichier texte au milieu du lorem ipsum\n")

print(lines)

fichier.seek(0) # On remet le pointeur au début du fichier
fichier.writelines(lines)

fichier.close()
print("Modification du fichier terminée")