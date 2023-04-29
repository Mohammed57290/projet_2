import csv
import os
import requests

"""
cette fonction permet le chargement des données d'un livre qui apartient à une catégorie
Ainsi on peut l'utiliser pour le chargement des livres de toutes les catégories en séparant chaque catégorie 
à part dans un dossier.
Ce dernier contient un fichier csv de la catégorie ainsi qu'un dossier qui contient toutes les images
de la catégorie.
arborescence : 
                category_a/
                    images/
                    category_a.csv
                category_b/
                    images/
                    category_b/
                ...
paramètres : nom de la categorie , url du livre(infos_livre)
"""


def charger_infos_et_image_d_un_livre_d_une_categorie(categorie, infos_livre):
    # On crée une liste pour les en-têtes
    en_tete = ["product_page_url", "universal_ product_code (upc)", "title", "price_including_tax",
               "price_excluding_tax", "number_available", "product_description", "category",
               "review_rating", "image"]

    if not os.path.exists("categorie_" + categorie):
        os.mkdir("categorie_" + categorie)
    nom_fichier_csv = os.path.join("categorie_" + categorie, categorie + '.csv')

    # On crée un nouveau fichier en mode écriture avec comme nom la valeur récupérée avant de : nom_fichier_csv
    with open(nom_fichier_csv, 'w', encoding='utf-8', newline='') as nom_fichier_csv:

        # Créer un objet writer (écriture) avec ce fichier
        writer = csv.writer(nom_fichier_csv, delimiter=',')
        writer.writerow(en_tete)

        i = 1
        for i, livre in enumerate(infos_livre):
            url_page_livre = livre['url page']
            code_universel_produit_valeur = livre['code universel produit']
            titre_livre = livre['titre']
            prix_avec_tax = livre['prix avec tax']
            prix_sans_tax = livre['prix sans tax']
            nombre_disponible = livre['nombre disponible']
            description_livre = livre['description']
            categorie = livre['categorie']
            note_des_avis = livre['note']
            url_image = livre['url image']

            ligne = [url_page_livre, code_universel_produit_valeur, titre_livre, prix_avec_tax,
                     prix_sans_tax, nombre_disponible, description_livre, categorie,
                     note_des_avis, url_image]
            writer.writerow(ligne)

            # cette ligne permet uniquement de visualiser l'évolution du programme
            print("écriture des infos livre :      " + titre_livre + "      N°==>" + str(i + 1) +
                  "   Categorie : " + livre['categorie'])

    for i, livre in enumerate(infos_livre):

        # on nettoie le titre du livre pour pouvoir l'attribuer comme nom d'image
        titre_img = livre['titre']
        nom_image = titre_img.replace('(', '').replace(' ', '_').replace('#', '_').replace(')', '') \
            .replace(':', '_').replace('/', '_').replace('"', '_').replace('...', '_') \
            .replace('*', '_').replace('?', '_').strip()

        # on spécifie le chemin avec path pour qu'il soit compatible avec tous les OS avec os.path.join
        nom_fichier_image = os.path.join(os.path.join("categorie_" + categorie, "images"), nom_image + ".jpg")

        # on vérifie si le dossier images n'existe pas, si c'est le cas, on le crée
        if not os.path.exists(os.path.join("categorie_" + categorie, "images")):
            os.mkdir(os.path.join("categorie_" + categorie, "images"))

        url_image = livre['url image']
        image = requests.get(url_image).content

        # On crée un nouveau fichier en mode écriture binaire avec comme nom la valeur récupérée
        # avant de : nom_fichier_image
        with open(nom_fichier_image, 'wb') as images:
            try:
                images.write(image)

                # cette ligne permet uniquement de visualiser l'évolution du programme
                print("écriture de l'image :      " + url_image + "      N°==>" + str(i + 1) + "   Categorie : "
                      + livre['categorie'])
            except IOError:
                print("Cette image n'existe pas")
                pass


"""
Cette fonction permet le chargement des données d'un livre dans un fichier csv.
Ainsi on peut choisir de charger tous les livres on donnant au nom_fichier_csv : 
    tous_les_livres : lorsqu'on souhaite charger tous les livres de toutes les catégories
    sequential_art : lorsqu'on souhaite charger tous les livres de la catégorie choisie

Comme exemple : on peut charger les données d'un livre qui appartient à la catégorie : Sequential Art. 
Pour le faire on donne comme paramètres positionels à la fonction : 
    infos_livres : url du livre
    nom_fichier_csv : sequential_art 
"""


def charger_un_livre(infos_livre, nom_fichier_csv):
    # On crée une liste pour les en-têtes
    en_tete = ["product_page_url", "universal_ product_code (upc)", "title", "price_including_tax",
               "price_excluding_tax", "number_available", "product_description", "category",
               "review_rating", "image_url"]

    # On crée un nouveau fichier en mode écriture dans le fichier (nom_fichier_csv)
    with open(nom_fichier_csv + '.csv', 'w', encoding='utf-8', newline='') as data:
        # Créer un objet writer (écriture/ajout) avec ce fichier
        writer = csv.writer(data, delimiter=',')
        writer.writerow(en_tete)

        for livre in infos_livre:
            url_page_livre = livre['url page']
            code_universel_produit_valeur = livre['code universel produit']
            titre_livre = livre['titre']
            prix_avec_tax = livre['prix avec tax']
            prix_sans_tax = livre['prix sans tax']
            nombre_disponible = livre['nombre disponible']
            description_livre = livre['description']
            categorie = livre['categorie']
            note_des_avis = livre['note']
            url_image = livre['url image']

            ligne = [url_page_livre, code_universel_produit_valeur, titre_livre, prix_avec_tax,
                     prix_sans_tax, nombre_disponible, description_livre, categorie,
                     note_des_avis, url_image]
            writer.writerow(ligne)


"""
Cette fonction permet l'enregistrement d'une image d'un livre (dans un dossier)
"""


def charger_une_image(infos_livre):
    for i, livre in enumerate(infos_livre):

        # on nettoie le titre du livre pour pouvoir l'attribuer comme nom d'image
        titre = livre['titre']
        titre = titre.replace('(', '').replace(' ', '_').replace('#', '_').replace(')', '')\
            .replace(':', '_').replace('/', '_').replace('"', '_').replace('...', '_')\
            .replace('*', '_').replace('?', '_').strip()

        # titre = 'Livre_' + str(i)
        url_image = livre['url image']
        image = requests.get(url_image).content
        # nom_fichier = 'images_livres/' + titre + '.jpg'
        # nom_fichier = titre + '.jpg'

        # on vérifie si le dossier "toutes_les_images" n'existe pas, si c'est le cas, on le crée
        if not os.path.exists("toutes_les_images"):
            os.mkdir("toutes_les_images")
        nom_fichier = os.path.join("toutes_les_images", titre + '.jpg')

        with open(nom_fichier, 'wb') as f:
            try:
                f.write(image)
                print('écriture img livre :    ' + titre + '      N°==>' + str(i + 1) + ' url_image : ' + url_image)
            except IOError:
                print("Cette image n'existe pas")
                pass

