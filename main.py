import extraction as extract
import chargement as load

if __name__ == '__main__':
    """
    Enregistrement des livres de toutes les catégories en faisant appele à la fonction 
    charger_infos_et_image_d_un_livre_d_une_categorie(nom_categorie, infos_livres_d_une_categorie)
    qui fait en sorte de séparer chaque catégorie à part dans un dossier.
    """

    urls_toutes_categories = extract.extraire_les_livres_de_toutes_les_categories()
    for nom_categorie, url_categorie in urls_toutes_categories.items():

        i = 1
        urls_de_la_caregorie_choisie = extract.extraire_les_livres_d_une_categorie(url_categorie)
        infos_livres_d_une_categorie = list()
        for url_d_une_page_de_la_categorie in urls_de_la_caregorie_choisie:
            urls_livres_de_la_page = extract.extraire_les_livres_d_une_page(url_d_une_page_de_la_categorie)
            for url_d_un_livre in urls_livres_de_la_page:
                toutes_les_infos_d_un_livre = extract.extraire_les_donnees_d_un_livre(url_d_un_livre)
                infos_livres_d_une_categorie.append(toutes_les_infos_d_un_livre)
                print(f"livre url : {url_d_un_livre} ===> catégorie : {nom_categorie} : url N° {i}")
                i += 1

        load.charger_infos_et_image_d_un_livre_d_une_categorie(nom_categorie, infos_livres_d_une_categorie)

    """
    chargement des livres et de leurs images (toutes les catégories).
     
    """
    i = 1
    infos_de_tous_les_livres = list()
    urls_toutes_categories = extract.extraire_les_livres_de_toutes_les_categories()

    for url_d_une_categorie in urls_toutes_categories.values():
        urls_de_la_categorie = extract.extraire_les_livres_d_une_categorie(url_d_une_categorie)
        for url_d_une_page_de_la_categorie in urls_de_la_categorie:
            urls_livres_de_la_page = extract.extraire_les_livres_d_une_page(url_d_une_page_de_la_categorie)
            for url_d_un_livre in urls_livres_de_la_page:
                toutes_les_infos_d_un_livre = extract.extraire_les_donnees_d_un_livre(url_d_un_livre)
                infos_de_tous_les_livres.append(toutes_les_infos_d_un_livre)
                print(f"url livre : {url_d_un_livre} ===>  N°{i}")
                i += 1
    load.charger_un_livre(infos_de_tous_les_livres, 'tous_les_livres')

    load.charger_une_image(infos_de_tous_les_livres)
