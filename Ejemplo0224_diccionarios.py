#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 14:32:31 2025

@author: carlosjuarez

Descripciòn: Uso de dicionarios
"""

# Creaciòn de un diccionairio
# dicc = {key: value}

dicc = {'00013600':9,'00012398':7.5,'00324507':3}

for key in dicc:
    print("La llave %s està asociada al valor %5.2f" % (key,dicc[key]))
    
    
persona1 = {"nombre":'Juan',"apellido":"Perez",'edad':30,'nota':9.9}
persona2 = {"nombre":'Miguel',"apellido":"Alberto",'edad':23,'nota':5.0}
persona3 = {"nombre":'Maria',"apellido":"Martinez",'edad':20,'nota':3.9}

# Diccionario puede contener otros diccionarios

bd = dicc = {'00013600':persona1,'00012398':persona2,'00324507':persona3}
print(bd)