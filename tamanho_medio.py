# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 21:42:23 2020

@author: filip
"""


feira = ["banana", "maca", "uva", "ameixa", "laranja"]

def tam_palavras(lista):
    i = 0
    soma_palavras = 0
    while i < len(lista):
        x = lista[i]
        len(x)
        soma_palavras = soma_palavras + len(x)
        i +=1
    return soma_palavras

def num_palavras(lista):
    return len(lista)

def tam_medio (lista):
    tam = tam_palavras(lista)/num_palavras(lista)
    return tam
    

print (tam_medio(feira))