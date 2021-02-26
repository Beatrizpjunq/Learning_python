# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 18:13:08 2020

@author: filip
"""


n = int(input("digite a quantidade de termos n: "))
i = 0
soma = 0

while i < n :
    x = int(input("digite o númeor a ser somado: "))
    soma = soma + x
    i = i + 1
        
        
print ( "a soma é igaul a :", soma )