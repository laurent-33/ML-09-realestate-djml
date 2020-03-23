#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re, csv, os, sys, requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import date
from time import time
from dateutil import parser
from bien_immo import Bien_immo
from scrap_functions import scrap, get_refs, get_nb_pages

def start_scrap(last_csv_update_date):
    start = time()
    scrap_done = False
    nb_jours = (date.today()-last_csv_update_date).days
    if last_csv_update_date == date.today():
        scrap_done = True
        print("Data à jour")
    else:
        if last_csv_update_date.month < 10:
            print(f"Récupération des données depuis le {last_csv_update_date.day}/0{last_csv_update_date.month}/{last_csv_update_date.year} (dernière mise à jour).")
        else:
            print(f"Récupération des données depuis le {last_csv_update_date.day}/{last_csv_update_date.month}/{last_csv_update_date.year} (dernière mise à jour).")
        #print(f"Durée estimée {((nb_jours*15)//60)+1} min ")

        nb_pages = get_nb_pages()
        biens =  []
        while not scrap_done:
            for page in range(1, nb_pages + 1):
                print(f"Page {page} ...", end='\r')

                refs = get_refs(page)
                for ref in refs:
                    bien_immo = scrap(ref)
                    if bien_immo["publish_date"] == None or bien_immo["publish_date"] > last_csv_update_date:
                        biens.append(bien_immo)
                    else:
                        scrap_done = True
                        break
                print(f"page {page} ok!", end='\r')

                if page%10 == 0 or scrap_done:
                    if not os.path.isfile("../csv/dataset_final_" + str(date.today()) + ".csv"):
                        with open("../csv/dataset_final_" + str(date.today()) + ".csv", 'w') as csvfile:
                            fieldnames = list(biens[0].keys())
                            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                            writer.writeheader()
                            writer.writerows(biens)
                    else:
                        with open("../csv/dataset_final_" + str(date.today()) + ".csv", 'a') as csvfile:
                            writer = csv.writer(csvfile)
                            for bien in biens:
                                writer.writerow(list(bien.values()))
                    biens = []

                if scrap_done:
                    print("\nData à jour")
                    break

        print(f"Durée pour {nb_jours} jours de données: {round(time()-start)//60} min {round(time()-start)%60} ")


if __name__ == '__main__':
    start_scrap(parser.parse(sys.argv[1], dayfirst=True).date())