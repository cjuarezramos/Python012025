#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 14:17:17 2025

@author: carlosjuarez
"""

archivo = open('num.txt','r')
L = []

for linea in archivo:
    linea = linea.replace('\n', '')
    L.append(float(linea))
    
a =archivo.read()

print(L)


archivo.close()


archivo1 = open('texto.txt','r')
L1 = []
b=archivo1.read()
c = b.split('\n')
archivo1.close()

archivo2 = open('iris.csv','r')
L = []

for linea in archivo2:
    linea = linea.split(',')
    L.append(linea)
    
archivo2.close()