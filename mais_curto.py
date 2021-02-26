# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 20:35:31 2020

@author: filip
"""

def mais_curto(lista):
    i = 0
    nova_lista = []
    while i < len(lista):
        nova_lista.append(lista[i].strip())
        i+=1
    menor = nova_lista[0]
    n = 0
    while n < (len(lista)-1):
        if len(menor) > len(nova_lista[n]):
            menor = nova_lista[n]
        n+=1
    return menor.capitalize()



lista_de_nomes = ['Paulo','carlos',"Laura", "J V", "BIA      "]


print (mais_curto(lista_de_nomes))