import transformation as transform
import requests
from bs4 import BeautifulSoup


def extraire_les_donnees_d_un_livre(url_un_livre):
    toutes_infos_d_un_livre = dict()
    url_acceuil = "https://books.toscrape.com/"

    page_info_livre = requests.get(url_un_livre)
    soup_infos_livre = BeautifulSoup(page_info_livre.text, 'html.parser')

    # Extraire toutes les données du livre :
    infos_livre = soup_infos_livre.find('article', class_="product_page")

    # Extraire les données du produit contenues dans la balise table :
    infos_livre_table = soup_infos_livre.find('table', class_="table table-striped")

    # Extraire les informations conçernant chaque produit séparémment :
    # code_universel_produit_nom = infos_livre_table.find_all('tr')[0].find('th').text
    code_universel_produit_valeur = infos_livre_table.find_all('tr')[0].find('td').text

    titre_livre = infos_livre.find('div', class_="col-sm-6 product_main").h1.text

    # prix_avec_tax_nom = infos_livre_table.find_all('tr')[3].find('th').text
    prix_avec_tax_valeur = infos_livre_table.find_all('tr')[3].find('td').text[2:]
    prix_avec_tax_valeur = float(prix_avec_tax_valeur)

    # prix_sans_tax_nom = infos_livre_table.find_all('tr')[2].find('th').text
    prix_sans_tax_valeur = infos_livre_table.find_all('tr')[2].find('td').text[2:]
    prix_sans_tax_valeur = float(prix_sans_tax_valeur)

    # nombre_disponible_nom = infos_livre_table.find_all('tr')[5].find('th').text
    nombre_disponible_valeur = infos_livre_table.find_all('tr')[5].find('td').text

    description_livre = soup_infos_livre.find_all('p')[3].text

    categorie = soup_infos_livre.find('ul', class_="breadcrumb").find_all('li')[2].text.strip()

    note_livre = soup_infos_livre.find('p', class_='star-rating')
    nombre_etoiles_str = note_livre.get("class")[1]

    nbre_etoiles = transform.transformer_le_nombre_d_etoiles_str_en_nombre(nombre_etoiles_str)
    nombre_etoiles = nbre_etoiles
    """
    Extraire l'url de l'image du livre et le concatener avec l'url d_acceuil du site pour 
    avoir l'url complet de l'image
    """
    url_partiel_image = infos_livre.find('img').get('src')
    url_image = url_acceuil + transform.nettoyer_url_partiel_image2(url_partiel_image)

    toutes_infos_d_un_livre['url page'] = url_un_livre
    toutes_infos_d_un_livre['code universel produit'] = code_universel_produit_valeur
    toutes_infos_d_un_livre['titre'] = titre_livre
    toutes_infos_d_un_livre['prix avec tax'] = float(prix_avec_tax_valeur)
    toutes_infos_d_un_livre['prix sans tax'] = float(prix_sans_tax_valeur)
    toutes_infos_d_un_livre['nombre disponible'] = nombre_disponible_valeur
    toutes_infos_d_un_livre['description'] = description_livre
    toutes_infos_d_un_livre['categorie'] = categorie
    toutes_infos_d_un_livre['note'] = nombre_etoiles
    toutes_infos_d_un_livre['url image'] = url_image

    return toutes_infos_d_un_livre


def extraire_les_livres_d_une_page(url_une_page):
    url_fixe_livre = "http://books.toscrape.com/catalogue/"
    urls_livres_d_une_page = []
    page = requests.get(url_une_page)
    soup_page = BeautifulSoup(page.content, 'html.parser')

    urls_livres_page = soup_page.find('ol', class_="row").find_all('li')
    for url_livre_page in urls_livres_page:
        url_livre = url_livre_page.find('article', class_="product_pod").find('h3').find('a').get('href') \
            .replace('../../../', '')
        url_livre = url_fixe_livre + url_livre
        urls_livres_d_une_page.append(url_livre)

    return urls_livres_d_une_page


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
                # on cherche la dernière occurence du caractère '/'
                index = url_d_une_categ.rfind('/')
                # on prend l'url da page suivante du début jusqu'à l'index + 1 (exclusif) et on rajoute
                # l'url du next
                url_page_suivante = url_d_une_categ[:index + 1].strip() + url_next
                urls_une_categorie.append(url_page_suivante)
                page_actuelle = requests.get(url_page_suivante)
                soup_page_actuelle = BeautifulSoup(page_actuelle.content, 'html.parser')
                url_next = soup_page_actuelle.find('li', class_='next').find('a').get('href')
        except AttributeError:
            pass
        break

    return urls_une_categorie


def extraire_les_livres_de_toutes_les_categories():

    noms_et_urls_categories = dict()
    url_accueil = "http://books.toscrape.com/"

    url_page_accueil = requests.get(url_accueil)
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
    # return url_toutes_les_categories
    return noms_et_urls_categories
