#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re, string
from bien_immo import Bien_immo 
from dateutil import parser
from time import time
from datetime import date

def scrap(ref):
    r = requests.get(f"https://www.green-acres.fr{ref}", headers={'Accept-Language' : "fr-FR"})
    soup = BeautifulSoup(r.content, 'html.parser')

    bien_immo = Bien_immo(ref = ref)

    main_characteristics = soup.find(class_="item-content-part main-characteristics")

    characteristics = []
    main_characteristics_ul = main_characteristics.find_next('ul')
    for li in main_characteristics_ul.find_all('li'):
        for p in li.find_all("p"):
            characteristics.append(p.get_text().strip())

    informations = soup.find(class_="item-content-part price item-ecology")
    environment = []
    for p in informations.find_all("p"):
        environment.append(p.get_text().strip())

    emplacement = environment[-1].split(" ")
    #Date de publication (publish_date)
    div = soup.find(class_="popularity")
    if div:
        bien_immo.publish_date = parser.parse(div.prettify().partition(">\n</section>\n")[0][-11:-1], dayfirst = True).date()
    # Ville (city)
    if len(emplacement) == 10:
        bien_immo.city = emplacement[5][:-1].lower()
    if len(emplacement) == 11:
        bien_immo.city = emplacement[5]+" "+emplacement[6][:-1].lower()

    # Département (departement)
    if len(emplacement) == 10:
        bien_immo.departement = emplacement[7].lower()
    if len(emplacement) == 11:
        bien_immo.departement = emplacement[8].lower()
    
    # Région (region)
    bien_immo.region = emplacement[-1][:-2].lower()
    
    for characteristic in characteristics:
    # Surface habitable (living_area_m2)
        if re.match("\d{1,} m² de surface habitable", characteristic):
            bien_immo.living_area_m2 = int(characteristic.split(" ")[0])
    # Surface terrain (lot_size_m2)       
        if re.match("\d+,?\d+? hectares de terrain", characteristic):
            bien_immo.lot_size_m2 = int(float(re.sub(",", ".", characteristic.split(" ")[0]))*10000)
        if re.match("\d{1,} m² de terrain", characteristic):
            bien_immo.lot_size_m2 = int(characteristic.split(" ")[0])
    # Nombre de pièces (nb_room)
        if re.match("\d{1,} pièces", characteristic):
            bien_immo.nb_room = int(characteristic.split(" ")[0])
    # Nombre de chambres (nb_bedroom)
        if re.match("\d{1,} chambres", characteristic):
            bien_immo.nb_bedroom = int(characteristic.split(" ")[0])
    # Piscine (pool : booléen)
        if re.match("Piscine", characteristic):
            bien_immo.pool = True
    # Cave (cellar : booléen)
        if re.match("Cave", characteristic):
            bien_immo.cellar = True
    # Parking/Garage (garage : booléen)
        if re.match(".* parking", characteristic):
            bien_immo.garage = True
   
    # Prix (output)
    output = informations.find("h2")
    output = output.find(class_="price").get_text()
    bien_immo.output = int(re.sub("[\s€]","", output))

    #Type de bien (type)
    types_bien = ["maison", "villa", "appartement", "terrain", "manoir", "fond"]
    titre = soup.find("h1").text.strip()
    bien_immo.titre = titre
    check_match = set(titre.lower().split()) & set(types_bien)
    if check_match:
        if list(check_match)[0] == "villa":
            bien_immo.type = "maison"
        elif list(check_match)[0] in ["studio", "t1", "t2", "t3", "t4", "f1", "f2", "f3", "f4"]:
            bien_immo.type = "appartement"
        else:
            bien_immo.type = list(check_match)[0]
    else:
        bien_immo.type = "autre"
    return bien_immo.__dict__

def get_refs(page):
    r = requests.get(f"https://www.green-acres.fr/fr/prog_show_properties-order-date_d-lg-fr-cn-fr-i-24-city_id-rg_aquitaine.html?p_n={page}")
    soup = BeautifulSoup(r.content, "html.parser")
    agc = soup.find(id="adverts-grid-container")
    refs = []
    for figure in agc.find_all("figure"):
        a = figure.find("a", href=True)
        refs.append(a['href'])
    return refs

def get_nb_pages():
    r = requests.get(f"https://www.green-acres.fr/fr/prog_show_properties-order-date_d-lg-fr-cn-fr-i-24-city_id-rg_aquitaine.html?p_n=1")
    soup = BeautifulSoup(r.content, "html.parser")
    nb_biens = soup.find(class_="alert-title").get_text().split(" ")
    nb_biens = int(re.sub("\\xa0", "", nb_biens[3]))
    nb_pages = (nb_biens // 24) + 1
    return nb_pages

if __name__ == '__main__':
    ref = "/fr/properties/38078a-8500265552.htm"
    scrap(ref)