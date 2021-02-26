# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 12:47:48 2020

@author: filip
"""


def soma_elementos(lista):
    soma_elementos = 0
    for num in lista:
        soma_elementos = soma_elementos + num
    return soma_elementos


lista = []      
n = 1
while n > 0:
    n = int(input("Digite os números da sua lista:" ))
    lista.append(n)
print(soma_elementos(lista))