"""
Cette fonction permet de transformer le nomnre d'étoiles en chaine de caractères en nombre
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

    return nbre_etoiles


def nettoyer_url_partiel_image(url_partiel_image):
    # on parcourt l'url jusqu'au caractère m de media et on enlève les ../ à chaque itération
    url_partiel_image_nettoye = ""
    for i in range(len(url_partiel_image)):
        url_partiel_image_nettoye = url_partiel_image.replace('../', '')
        if url_partiel_image[i] == 'm':
            break

    return url_partiel_image_nettoye


def nettoyer_url_partiel_image2(url_partiel_image):

    # on enlève la première parie de l'url : ../../ et on garde le reste
    url_partiel_image_nettoye = url_partiel_image[6:]

    return url_partiel_image_nettoye
