#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 16:51:41 2025

@author: carlosjuarez
"""
def fibonacci(n):
    fibo = [0, 1]
    for i in range(n-2):
        fibo.append(fibo[-1] + fibo[-2])#Agrega el último elemento de la lista y el penúltimo
    return fibo 

n = int(input('Ingrese cantidad de términos serie de Fibonacci: '))
print(fibonacci(n)[-1])