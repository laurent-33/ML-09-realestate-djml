#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Bien_immo():

    def __init__(self, ref = None, publish_date = None, city = None, departement = None, region = None, titre = None, 
                 type = None, living_area_m2 = None, lot_size_m2 = None, nb_room = None,
                 nb_bedroom = None, pool = False, cellar = False, garage = False,
                 output = None):
        self.ref = ref
        self.publish_date = publish_date
        self.city = city
        self.departement = departement
        self.region = region
        self.titre = titre
        self.type = type
        self.living_area_m2 = living_area_m2
        self.lot_size_m2 = lot_size_m2
        self.nb_room = nb_room
        self.nb_bedroom = nb_bedroom
        self.pool = pool
        self.cellar = cellar
        self.garage = garage
        self.output = output

    def __str__(self):
        return f"ref: {self.ref}\ncity: {self.city}\ndepartement: {self.departement}\nregion: {self.region}\nliving_area_m2: {self.living_area_m2}\
            \nnb_room: {self.nb_room}\nnb_bedroom: {self.nb_bedroom}\npool: {self.pool}\ncellar: {self.cellar}\
            \ngarage: {self.garage}\noutput: {self.output}"
