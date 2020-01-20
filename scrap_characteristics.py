#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re
from bien_immo import Bien_immo

ref = "9023a-261"

r = requests.get(f"https://www.green-acres.fr/fr/properties/{ref}.htm", headers={'Accept-Language' : "fr-FR"})
soup = BeautifulSoup(r.content, 'html.parser')

main_characteristics = soup.find(class_="item-content-part main-characteristics")

characteristics = []
main_characteristics_ul = main_characteristics.find_next('ul')
for li in main_characteristics_ul.find_all('li'):
    for p in li.find_all("p"):
        characteristics.append(p.get_text().strip())

print(characteristics)

bien_immo = Bien_immo(ref=ref)

# Surface habitable (area_m2)
for characteristic in characteristics:
    if re.match("\d{1,} m² de surface habitable", characteristic):
        bien_immo.area_m2 = float(characteristic.split(" ")[0])
# Surface terrain (ground_m2)       
    if re.match("\d+,?\d+? hectares de terrain", characteristic):
        bien_immo.ground_m2 = float(re.sub(",", ".", characteristic.split(" ")[0]))*10000
    if re.match("\d{1,} m² de terrain", characteristic):
        bien_immo.ground_m2 = characteristic.split(" ")[0]
# Nombre de pièces (nb_room)
    if re.match("\d{1,} pièces", characteristic):
        bien_immo.nb_room = characteristic.split(" ")[0]
# Nombre de chambres (nb_bedroom)
    if re.match("\d{1,} chambres", characteristic):
        bien_immo.nb_bedroom = characteristic.split(" ")[0]
# Piscine (pool : booléen)
    if re.match("Piscine", characteristic):
        bien_immo.piscine = True
# Cave (cellar : booléen)
    if re.match("Cave", characteristic):
        bien_immo.cellar = True
# Parking/Garage (garage : booléen)
    if re.match(".* parking", characteristic):
        bien_immo.garage = True

print(bien_immo)