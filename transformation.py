
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
    url_partiel_image_nettoye = ""
    for i in range(len(url_partiel_image)):
        url_partiel_image_nettoye = url_partiel_image.replace('../', '')
        if url_partiel_image[i] == 'm':
            break

    return url_partiel_image_nettoye


def nettoyer_url_partiel_image2(url_partiel_image):

    url_partiel_image_nettoye = url_partiel_image[6:]

    return url_partiel_image_nettoye
