# Suivi des prix des livres de Books to Scrape

### Description du projet :

  Le but de ce projet est d'automatiser le suivi des prix des livres chez [Books to Scrape](http://books.toscrape.com/), un revendeur de livres en ligne, ce qui permet un gain de temps 
  considérable donc un gain en productivité et surtout il permet d'éviter les erreurs qu'on peut faire en faisant le suivi manuellement.
  
L'application récupère les prix au moment de son exécution.
  

### Comment récupérer le projet :
Pour récupérer le projet il faut utiliser la commande clone comme suit : 

```commandline
git clone https://github.com/Mohammed57290/projet_2.git 
```
Cette instruction va récupérer le projet en créant un dossier qui a le même nom du projet.

Si vous voulez le récuperer sous un nom différent il faut le spécifier en le rajoutant à la fin de l'instruction :

```commandline
git clone https://github.com/Mohammed57290/projet_2.git "nom du dossier"
```
### Comment exécuter le projet :

Le fichier requirements.txt liste les paquets Python dont l'installation est requise dans un environnement virtuel pour que l'application s'exécute correctement. 
Pour exécuter le projet, il suffit d'installer un environnement virtuel, installer les dépendances mentionnées dans le fichier equirements.txt et lancer le projet 
en exécutant le fichier main.py.


Une fois que vous l'avez ouvert dans votre environnement de développement vous suivez les instructions suivantes :

````commandline
python -m venv env
````
pour créer un environnement virtuel

````
.\env\scripts\activate
````
Pour activer l'environnement sous windows
````
source /env/bin/activate
````
Pour activer l'environnement sous Linux et MacOS

````
pip install -r requirements.txt
````
Pour installer les dépendances
````
pip freeze
````
Pour s'assurer que les dépendances ont bien été installées
````
python main.py
````
Pour exécuter le programme

### Comment utiliser le projet :

Le résultat après l'exécution du projet :

1. **un dossier pour chaque catégorie** 


&emsp;chaque dossier porte le nom d'une catégorie et contient :

&emsp;&emsp;a) un fichier csv qui contient les données des livres de cette catégorie

&emsp;&emsp;b) un dossier images qui contient toutes les images des livres de cette catégorie.

la structure est la suivante :

```
     categorie_a/
          images/
          categorie_a.csv
     categorie_b/
          images/
          categorie_b.csv
     ...
   
```
2. **tous_les_livres.csv : un fichier** qui contient les informations de tous les livres du site Books to Scrape
3. **toutes_les_images : un dossier** qui contient toutes les images de tous les livres du site

L'ouverture/importation des fichiers csv dans un tableur comme Excel ou google Sheets permet la visualisation des informations de chaque livre.
