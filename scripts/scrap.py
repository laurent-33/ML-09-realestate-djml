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
    scrap_done = False
    #check if data up to date
    if last_csv_update_date == date.today():
        scrap_done = True
        print("Data up to date !")
    else:
        if last_csv_update_date.month < 10:
            print(f"Data collection since {last_csv_update_date.day}/0{last_csv_update_date.month}/{last_csv_update_date.year} (Last update).")
        else:
            print(f"Date collection since {last_csv_update_date.day}/{last_csv_update_date.month}/{last_csv_update_date.year} (Last update).")
        print("Please wait until data is up to date ...")
        print("You can still make an estimation in the meanwhile !")

        #get number of pages to scrap
        nb_pages = get_nb_pages()
        #init list of properties
        biens =  []
        #scrap
        while not scrap_done:
            for page in range(1, nb_pages + 1):
                #get all refs on current page
                refs = get_refs(page)
                for ref in refs:
                    #for each ref scrap property infos
                    bien_immo = scrap(ref)
                    #check if scrapped property's publish date is post last update
                    if bien_immo["publish_date"] == None or bien_immo["publish_date"] > last_csv_update_date:
                        biens.append(bien_immo)
                    else:
                        scrap_done = True
                        break
                #Each time 10 pages are scrapped or scrap is done, write in csv file
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
                    #re init list of properties
                    biens = []

                if scrap_done:
                    print("\nData up to date ! ")
                    break

#allows test in terminal eg."python scrap.py '2020-01-01'"
if __name__ == '__main__':
    start_scrap(parser.parse(sys.argv[1], dayfirst=True).date())
