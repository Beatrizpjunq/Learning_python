# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 15:08:38 2020

@author: filip
"""


def maior_elemento(lista):
    lista.sort()
    return lista[len(lista) - 1]


lista = []      
n = 1
while n > 0:
    n = int(input("Digite os números da sua lista:" ))
    lista.append(n)

print (maior_elemento(lista))