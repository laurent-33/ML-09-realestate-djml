#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re
from bien_immo import Bien_immo
from scrap_functions import scrap, get_refs, get_nb_pages
import pandas as pd
import csv
from datetime import date


def start_scrap():
    fieldnames = ["ref", "city", "departement", "region", "titre", "type",
                "living_area_m2", "lot_size_m2", "nb_room", 
                "nb_bedroom", "pool", "cellar", "garage",
                "output"]

    biens_df = pd.DataFrame(columns=fieldnames)
    nb_biens, nb_pages = get_nb_pages()

    print(f"Début du scrapping de {nb_biens} biens immobiliers.")
    for page in range(1, nb_pages + 1):
        refs = get_refs(page=page)

        print(f"Scrapping : page {page} / {nb_pages} ...", end='\r')
        for ref in refs:
            biens_df = biens_df.append(pd.DataFrame(scrap(ref), index = [0]), ignore_index=True, sort=False)

        
        if page%10 == 0:
            biens_df.to_csv("dataset_final_" + str(date.today()) + ".csv")


if __name__ == '__main__':
    start_scrap()
    