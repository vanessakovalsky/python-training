# mon_fichier = open('C:/Users/vdavi/Documents/python-training/exemples/demo.txt',"r")
# print(mon_fichier)

# # lecture = mon_fichier.read(15)
# # print(lecture)

# # lecture_ligne = mon_fichier.readline()
# # print(lecture_ligne)

# # lecture_ligne2 = mon_fichier.readline()
# # print(lecture_ligne2)

# liste_ligne = mon_fichier.readlines()
# print(liste_ligne)
# for ligne in liste_ligne :
#      print(ligne)

# mon_fichier.close()


# mon_fichier2 = open('C:/Users/vdavi/Documents/python-training/exemples/demo.txt',"w")

# nouvelle_ligne = "Une démo de modification du fichier"

# mon_fichier2.write(nouvelle_ligne) ## /!\ on remplace le contenu du fichier avec l'argument ici nouvelle_ligne

# mon_fichier2.close()

# mon_fichier3 = open('C:/Users/vdavi/Documents/python-training/exemples/demo.txt',"r")

# print(mon_fichier3.read())

# mon_fichier3.close()

mon_fichier4 = open('C:/Users/vdavi/Documents/python-training/exemples/demo.txt',"a")

nouvelle_ligne2 = ["Une démo de modification du fichier \n", "Une autre ligne \n"]

mon_fichier4.writelines(nouvelle_ligne2) ## /!\ on remplace le contenu du fichier avec l'argument ici nouvelle_ligne

mon_fichier4.close()

mon_fichier5 = open('C:/Users/vdavi/Documents/python-training/exemples/demo.txt',"r")

print(mon_fichier5.read())

mon_fichier5.close()

