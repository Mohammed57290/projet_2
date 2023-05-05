# Suivi des prix des livres de Books to Scrape

### Description du projet :

  Le but de ce projet est d'automatiser le suivi des prix des livres chez [Books to Scrape](http://books.toscrape.com/), un revendeur de livres en ligne ce qui permet un gain de temps 
  considérable donc un gain en productivité et surtout il permet d'éviter les erreurs qu'on peut faire en faisant le suivi manuellement L'application récupère 
  les prix au moment de son exécution.
  
### Comment exécuter le projet :

Le fichier requirements.txt liste les paquets Python dont l'installation est requise dans un environnement virtuel pour que l'application s'exécute correctement. 
Pour exécuter le projet il suffit d'installer un environnement virtuel, installer les dependences mentionnées dans le fichier equirements.txt et lancer le projet 
en exécutant main avec les instructions suivantes :

````commandline
python -m venv env                  # pour créer un environnement virtuel
.\env\scripts\activate              # pour activer l'environnement
pip install -r requirements.txt     # pour installer les dépendances
pip freeze                          # pour s'assurer que les dépendances ont bien été installées
python main.py                      # pour exécuter le programme
````



### Comment utiliser le projet :

Le résultat après l'exécution du projet :

1. **un dossier par catégorie** qui porte son nom et qui contient à son tour un fichier csv qui porte le nom de la catégorie qui contient toutes informations des livres 
de cette catégorie ainsi qu'un fichier images qui contient toutes les images des livres de la catégorie avec la structure suivante :

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
3. **toutes_les_images.csv : un dossier** qui contient toutes les images de tous les livres du site

L'ouverture/importation des fichiers csv dans un tableur comme Excel ou google Sheets permet la visualisation des informations de chaque livre.
