# Exercice 1 - Installation et premier pas

## Objectifs 

Cet exercice a pour objectifs :
* de vous faire installer l'environnement nécessaire à Python
* de faire vos premier pas avec l'interpréteur de Python

## Installation

### Environnement Python 

#### VM vagrant :

* Pour les VM, avec Vagrant (à installer : https://www.vagrantup.com/downloads )
* * Récupérer les deux fichiers dans le dossier resources : install.sh et VagrantFile 
* * Mettre les deux fichier dans un dossier python-training (à créer)
* * Depuis le dossier, lancer la VM avec : `vagrant up`

#### Conteneur Docker 

* Avec docker installer (https://www.docker.com/get-started )
* * Dans un dossier python-training (à créer sur votre poste), récupèrer le fichier Dockerfile dans resources
* * Puis lancer le conteneur : `docker up`

#### Sur votre système d'exploitation
* Suivre les recommandations officielles de Python : https://wiki.python.org/moin/BeginnersGuide/Download 

### Editeur de code
* Il est nécessaire d'avoir un éditeur de code installé. Il est possible d'utiliser différents éditeurs : 
* * Certains sont spécialisés comme 
* * * PyDev (https://www.pydev.org/ ) 
* * * PyCharm (https://www.jetbrains.com/pycharm/ )
* * D’autres sont plus léger comme 
* * * Visual Studio Code (https://code.visualstudio.com/ ), 
* * * Atom (https://atom.io/ ) 
* * * Sublime text (http://www.sublimetext.com/ )

* Nous utiliserons VisualStudioCode et les extensions : Python, Python for VSCode et Visual Studio IntelliCode

### Stockage du code dans un éditeur

* Nous vous recommandons de stocker votre code dans un dépôt Git 

## Premier pas

* Lancer votre environnement et utiliser l'intérpréteur de python (commande : `python`)

* Voici une série d'opération, essayer de trouver le résultat de chaque avant de vérifier le résultat dans l'intérpréteur de Python : 
* * (1+2)**3
* * "Da" * 4
* * "Da" + 3
* * ("Pa"+"La") * 2
* * ("Da"*4) / 2
* * 5 / 2
* * 5 // 2
* * 5 % 2

* Bien, nous passons maintenant à des opérations sur les types de données, même chose, quelle est le résultat de chacune des instructions suivantes (vérifier ensuite dans l'intérpréteur )
* * str(4) * int("3")
* * int("3") + float("3.2")
* * str(3) * float("3.2")
* * str(3/4) * 2
