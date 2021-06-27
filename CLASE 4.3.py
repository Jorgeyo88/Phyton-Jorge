# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 19:58:57 2021

@author: acer_i5.7tmaG
"""

lista=["R1", "R2", "R3",
       "S1","S2","AP"]
print("antes de for")
for a in lista:
    print(a)
    print("dentro de for")
    print("fuera de for")
    
lista=["R1", "R2", "R3", "S1"]
for i in lista:
    if"R" in i:
        print(i)