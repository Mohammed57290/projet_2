import transformation
import requests
from bs4 import BeautifulSoup


"""
Cette fonction permet d'extraire les données d'un livre à partir de son url 
paramètre : url d'un livre
retour : un dictionnaire qui contient toutes les informations du livre
"""


def extraire_les_donnees_d_un_livre(url_un_livre):
    toutes_infos_d_un_livre = dict()

    page_info_livre = requests.get(url_un_livre)
    soup_infos_livre = BeautifulSoup(page_info_livre.text, 'html.parser')

    # Extraire toutes les données du livre :
    infos_livre = soup_infos_livre.find('article', class_="product_page")

    # Extraire les données du produit contenues dans la balise table :
    infos_livre_table = soup_infos_livre.find('table', class_="table table-striped")

    # Extraire les informations conçernant chaque produit séparémment :

    try:
        code_universel_produit = infos_livre_table.find_all('tr')[0].find('td').text
    except AttributeError:
        code_universel_produit = ""

    try:
        titre_livre = infos_livre.find('div', class_="col-sm-6 product_main").h1.text
    except AttributeError:
        titre_livre = ""

    try:
        prix_avec_tax = infos_livre_table.find_all('tr')[3].find('td').text[2:]
    except AttributeError:
        prix_avec_tax = "0"

    try:
        prix_sans_tax = infos_livre_table.find_all('tr')[2].find('td').text[2:]
    except AttributeError:
        prix_sans_tax = "0"

    try:
        nombre_disponible = infos_livre_table.find_all('tr')[5].find('td').text
    except AttributeError:
        nombre_disponible = "0"

    try:
        description_livre = soup_infos_livre.find_all('p')[3].text
    except AttributeError:
        description_livre = ""

    try:
        categorie = soup_infos_livre.find('ul', class_="breadcrumb").find_all('li')[2].text.strip()
    except AttributeError:
        categorie = ""

    try:
        note_livre = soup_infos_livre.find('p', class_='star-rating')
        nombre_etoiles_str = note_livre.get("class")[1]
    except AttributeError:
        nombre_etoiles_str = "0"

    try:
        url_partiel_image = infos_livre.find('img').get('src')
    except AttributeError:
        url_partiel_image = "../../media/cache/6d/41/6d418a73cc7d4ecfd75ca11d854041db.jpg"

    toutes_infos_d_un_livre['url page'] = url_un_livre
    toutes_infos_d_un_livre['code universel produit'] = code_universel_produit
    toutes_infos_d_un_livre['titre'] = titre_livre
    toutes_infos_d_un_livre['prix avec tax'] = prix_avec_tax
    toutes_infos_d_un_livre['prix sans tax'] = prix_sans_tax
    toutes_infos_d_un_livre['nombre disponible'] = nombre_disponible
    toutes_infos_d_un_livre['description'] = description_livre
    toutes_infos_d_un_livre['categorie'] = categorie
    toutes_infos_d_un_livre['note'] = nombre_etoiles_str
    toutes_infos_d_un_livre['url image'] = url_partiel_image

    return toutes_infos_d_un_livre


"""
Cette fonction permet d'extraire tous les livres affichés dans une page
paramètre : l'url d'une page
retour : une liste de tous les urls des livre qui sont dans la page
"""


def extraire_les_livres_d_une_page(url_une_page):
    url_livre_fixe = "http://books.toscrape.com/catalogue/"
    urls_livres_d_une_page = []
    page = requests.get(url_une_page)
    soup_page = BeautifulSoup(page.content, 'html.parser')

    urls_livres_page = soup_page.find('ol', class_="row").find_all('li')
    for url_livre_page in urls_livres_page:
        url_livre = url_livre_page.find('article', class_="product_pod").find('h3').find('a').get('href')
        url_livre_valide = transformation.transformer_urls_des_livres_d_une_page(url_livre)
        url_livre_complet = url_livre_fixe + url_livre_valide
        urls_livres_d_une_page.append(url_livre_complet)

    return urls_livres_d_une_page


"""
Cette fonction permet d'extraire les urls des livres qui appartiennent à une catégorie
paramètre : l'url d'une catégorie
retour : une liste des urls des livres qui appartiennent à cette catégorie
"""


def extraire_les_livres_d_une_categorie(url_d_une_categ):
    urls_une_categorie = list()

    while True:
        page_actuelle = requests.get(url_d_une_categ)
        soup_page_actuelle = BeautifulSoup(page_actuelle.content, 'html.parser')
        urls_une_categorie.append(url_d_une_categ)

        try:
            # on cherche le texte du lien next dans la page
            url_next = soup_page_actuelle.find('li', class_='next').find('a').get('href')
            while url_next:
                url_page_suivante = transformation.transformer_url_next(url_d_une_categ, url_next)
                urls_une_categorie.append(url_page_suivante)
                page_actuelle = requests.get(url_page_suivante)
                soup_page_actuelle = BeautifulSoup(page_actuelle.content, 'html.parser')
                url_next = soup_page_actuelle.find('li', class_='next').find('a').get('href')
        except AttributeError:
            pass
        break

    return urls_une_categorie


"""
Cette fontion permet d'extraire les noms et urls de toutes les catégories
retour : un dictionnaire qui contient les noms et les urls de toutes les catégories
"""


def extraire_les_livres_de_toutes_les_categories():

    noms_et_urls_categories = dict()
    url_accueil = "http://books.toscrape.com/"
    try:
        url_page_accueil = requests.get(url_accueil)
    except requests.exceptions.HTTPError as e:
        print("Erreur HTTP")
        print(e.args[0])
    except requests.exceptions.ReadTimeout as e:
        print("Time out")
    except requests.exceptions.ConnectionError as conerr:
        print("Erreur de connexion")
    except requests.exceptions.RequestException as errex:
        print("Exception request")

    soup_accueil = BeautifulSoup(url_page_accueil.content, 'html.parser')

    # On extrait toutes les catégories des livres
    categories = soup_accueil.find('ul', class_='nav nav-list').find('li').find('ul').find_all('li')

    url_toutes_les_categories = []
    # On fait une boucle sur les catégories pour pouvoir extraire les informations de chaque categorie
    for categorie in categories:
        nom_categorie = categorie.find('a').text.strip()
        url_categorie_lien = categorie.find('a').get('href')
        url_categorie = url_accueil + url_categorie_lien
        noms_et_urls_categories[nom_categorie] = url_categorie
        url_toutes_les_categories.append(url_categorie)
    return noms_et_urls_categories
