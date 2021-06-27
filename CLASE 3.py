# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 20:45:10 2021

@author: acer_i5.7tmaG
"""

lista1=[]
lista2=[]
lista3=[]
lista=["R1", "R2", "R3", "S1", "V1","V2","S4"]
for puntero in lista:
    if "R" in puntero:
        lista1.append(puntero)
    if "S" in puntero:
        lista2.append(puntero)
        lista3.append(puntero)
        print(lista1)
        print(lista2)
        print(lista3)