#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Bien_immo():

    def __init__(self, ref = None, city = None, county = None, district = None, 
                 area_m2 = None, ground_m2 = None, nb_room = None, nb_bedroom = None,
                 pool = None, cellar = None, garage = None, output = None):
        self.ref = ref
        self.city = city
        self.county = county
        self.district = district
        self.area_m2 = area_m2
        self.ground_m2 = ground_m2
        self.nb_room = nb_room
        self.nb_bedroom = nb_bedroom
        self.pool = pool
        self.cellar = cellar
        self.garage = garage
        self.output = output

    def __str__(self):
        return f"ref: {self.ref}\ncity: {self.city}\ncounty: {self.county}\ndistrict: {self.district}\narea_m2: {self.area_m2}\
            \nnb_room: {self.nb_room}\nnb_bedroom: {self.nb_bedroom}\npool: {self.pool}\ncellar: {self.cellar}\
            \ngarage: {self.garage}\noutput: {self.output}"