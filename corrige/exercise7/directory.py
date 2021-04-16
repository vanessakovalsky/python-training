import os

# Dans quel répertoire je suis ?
print('pwd')
print(os.getcwd())

# Que contient le répertoire ?
print('ls')
print(os.listdir())

# Nombre de fichier : 
print('nombre de fichiers')
print(len([name for name in os.listdir('.') if os.path.isfile(name)]))