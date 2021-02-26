# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 12:45:02 2020

@author: filip
"""


lista = []
remove_repetido = []

n = 1
while n > 0:
    n = int(input("Digite os números da sua lista:" ))
    lista.append(n)
lista.sort()
remove_repetido.append(lista[0])
for i in range((len(lista) - 1)):
    if lista[i] != lista [i +1]:
        remove_repetido.append(lista[i + 1])             
print (remove_repetido)

        