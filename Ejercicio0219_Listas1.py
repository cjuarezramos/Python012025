#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 16:36:56 2025

@author: carlosjuarez
"""
def quitar_pares(L):
    respuesta = []
    for n in L: # Python el for toma cada valor de la lista
        if n % 2 == 0:
            respuesta.append(n)
    return respuesta

print(quitar_pares(i for i in range(1000))) # declaraciòn de lista por comprensión


