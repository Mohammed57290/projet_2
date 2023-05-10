import extraction as extract


def transformer_les_donnees_d_un_livre(url_un_livre):

    url_acceuil = "https://books.toscrape.com/"

    toutes_infos_d_un_livre = extract.extraire_les_donnees_d_un_livre(url_un_livre)
    toutes_infos_d_un_livre['prix avec tax'] = float(toutes_infos_d_un_livre['prix avec tax'])
    toutes_infos_d_un_livre['prix sans tax'] = float(toutes_infos_d_un_livre['prix sans tax'])
    toutes_infos_d_un_livre['note'] = transformer_le_nombre_d_etoiles_str_en_nombre(toutes_infos_d_un_livre['note'])

    url_partiel_image = toutes_infos_d_un_livre['url image']
    # l'url de l'image est sous forme de : ../../media/cache/08/e9/08e94f3731d7d6b760dfbfbc02ca5c62.jpg
    # on enlève la première parie de l'url : ../../ et on garde le reste
    url_partiel_image_nettoye = url_partiel_image[6:]

    # on fait la concaténation avec l'url d_acceuil du site pour avoir l'url complet de l'image

    toutes_infos_d_un_livre['url image'] = url_acceuil + url_partiel_image_nettoye

    return toutes_infos_d_un_livre


"""
Cette fonction permet de transformer le nombre d'étoiles en chaine de caractères en nombre
paramètre : nombre d'étoiles en chaine de caractères
retour : nombre d'étoiles avec une valeur numérique
"""


def transformer_le_nombre_d_etoiles_str_en_nombre(nombre_etoiles_str):
    if nombre_etoiles_str == "One":
        nbre_etoiles = 1
    elif nombre_etoiles_str == "Two":
        nbre_etoiles = 2
    elif nombre_etoiles_str == "Three":
        nbre_etoiles = 3
    elif nombre_etoiles_str == "Four":
        nbre_etoiles = 4
    elif nombre_etoiles_str == "Five":
        nbre_etoiles = 5
    else:
        nbre_etoiles = 0

    return int(nbre_etoiles)


def transformer_urls_des_livres_d_une_page(url_livre):

    # on nettoie l'url de la page pour qu'elle soit valide
    url_livre_d_une_page_valide = url_livre.replace('../../../', '')
    return url_livre_d_une_page_valide


def transformer_url_next(url_d_une_categ, url_next):
    # on cherche la dernière occurence du caractère '/'
    index = url_d_une_categ.rfind('/')
    # on prend l'url da page suivante du début jusqu'à l'index + 1 (exclusif) et on rajoute
    # l'url du next (page suivante)
    url_page_suivante = url_d_une_categ[:index + 1].strip() + url_next

    return url_page_suivante


def transformer_nom_image(livre):

    # on nettoie le titre du livre pour pouvoir l'attribuer comme nom d'image
    titre_img = livre['titre']
    nom_image = titre_img.replace('(', '').replace(' ', '_').replace('#', '_').replace(')', '') \
        .replace(':', '_').replace('/', '_').replace('"', '_').replace('...', '_') \
        .replace('*', '_').replace('?', '_').replace(',','').strip()
    return nom_image
