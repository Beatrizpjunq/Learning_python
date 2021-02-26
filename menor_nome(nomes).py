# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 22:19:27 2020

@author: filip
"""


def menor_nome(nomes):
    i = 0
    nova_lista = []
    while i < len(nomes):
        nova_lista.append(nomes[i].strip())
        i+=1
    menor = nova_lista[0]
    n = 0
    while n < (len(nomes)-1):
        if len(menor) > len(nova_lista[n]):
            menor = nova_lista[n]
        n+=1
    return menor.capitalize()




