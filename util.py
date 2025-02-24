#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 15:17:11 2025

@author: carlosjuarez
Descripción. Creación de funciones
"""

def crear_datos_persona(nombre,apellido,edad,nota):
    return {'nombre':nombre,'apellido':apellido,'edad':edad,'nota':nota}

def pedir_vector():
    #Se asume formato de vector V = [Vx,Vy,Vz]
    V = []
    V.append(float(input('Ingrese componente en x: ')))
    V.append(float(input('Ingrese componente en y: ')))
    V.append(float(input('Ingrese componente en z: ')))
    return V

def producto_punto(a,b):
    # Asume que a y b son vectores
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]