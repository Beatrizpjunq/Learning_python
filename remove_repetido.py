# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 11:37:17 2020

@author: filip
"""


def remove_repetidos(lista):
    lista.sort()
    for num in lista:
        if num not in lista_correta:
            lista_correta.append(num)
    return lista_correta


lista = []
lista_correta = []         
n = 1
while n > 0:
    n = int(input("Digite os números da sua lista:" ))
    lista.append(n)

print (remove_repetidos(lista))



            
