#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 16:18:28 2025

@author: carlosjuarez

Descripción: Archivos de utlidad para tarea 3
"""

def lista_nombres(n):
    nombres = []
    i = 0
    while i < n:
        name = input('Ingrese nombre %i: ' % (i+1))
        if not(name in nombres):
            nombres.append(name) 
            i=i+1
        else:
            print('nombre ya està en el listado, debe usar otro')
    return nombres
            