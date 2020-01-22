#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re
from bien_immo import Bien_immo
from scrap import scrap, get_refs, get_nb_pages
import pandas as pd
import csv


fieldnames = ["ref", "city", "county", "district",
              "area_m2", "ground_m2", "nb_room", 
              "nb_bedroom", "pool", "cellar", "garage",
              "output"]
biens_df = pd.DataFrame(columns=fieldnames)


for page in range(1, get_nb_pages() + 1):
    refs = get_refs(page=page)

    for ref in refs:
        biens_df = biens_df.append(pd.DataFrame(scrap(ref), index = [0]), ignore_index=True, sort=False)
    
    print(f"page {page} scrappée!")

    if page%10 == 0:
        biens_df.to_csv("dataset_final.csv")
        print("10 pages (240 biens immo) ajoutées au csv!")