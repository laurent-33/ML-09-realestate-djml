#!/usr/bin/env python
# -- coding: utf-8 --


import requests
from bs4 import BeautifulSoup
import re

r = requests.get("https://www.green-acres.fr/fr/properties/59682a-greg3556.htm", headers={'Accept-Language' : "fr-FR"})
soup = BeautifulSoup(r.content, 'html.parser')


informations = soup.find(class_="item-content-part price item-ecology")
environment = []
for p in informations.find_all("p"):
    environment.append((p.get_text().strip().encode('ascii', 'ignore')).decode("utf-8"))

# Prix sans honoraires (prix_hh)



# Prix/m2 (prix_m2)


emplacement = environment[8].split(" ")
# Ville (city)
city = emplacement[5]
city = city[:-1]
# Département (county)
county = emplacement[7]
# Région (district)
district = emplacement[9]
district = district[:-2]
# Surface habitable (area_m2)

# Surface terrain (ground_m2)

# Nombre de pièces (nb_room)

# Nombre de chambres (nb_bedroom)

# Piscine (pool : booléen)

# Cave (cellar : booléen)

# Parking/Garage (garage : booléen)

# Prix (output)
output = informations.find_next("h2")
output = output.find(class_="price").get_text()
# output = (output.encode('ascii', 'ignore')).decode("utf-8")
output = re.sub("[\s]","", output)
output = int(output[:-1])

# Référence
ref = environment[4]
ref = ref.split(" ")
ref = ref[2]




print('Référence : ', ref)

# print('Prix sans honoraires :', prix_hh)

# print('Prix/m2 :', prix_m2)

print('Ville :', city)

print('Département :', county)

print('Région :', district)

# print('Surface habitable :', area_m2)

# print('Surface terrain :', ground_m2)

# print('Nombre de pièces :', nb_room)

# print('Nombre de chambres :', nb_bedroom)

# print('Piscine :', pool)

# print('Cave :', cellar)

# print('Parking/Garage :', garage)

print('Prix :', output)