#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 16:18:28 2025

@author: carlosjuarez

Descripción: Archivos de utlidad para tarea 3

"""

import random as rd

def lista_nombres(n):
    # Solicita nombres uno a uno y devuelve una lista de nombres
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
            
def lista_numrand(n):
    # solicita un numero n y genera una lista de num aleatorios
    numeros = []
    i = 0
    while i < n:
        num = rd.randint(0,500)
        if not(num in numeros):
            numeros.append(num)
            i=i+1
        else:
            print('oh oh')
    return numeros

def bd(lname,lnum):
    dicc={}
    
    for i in range(len(lname)):
        dicc.pop({lnum[i]:lname[i]})
        
    return dicc
    
    