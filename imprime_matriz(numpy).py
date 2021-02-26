# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 21:24:25 2020

@author: filip
"""
import numpy as np

def cria_matriz(tot_lin, tot_col, valor):
    matriz = []  #lista vazia
    for i in range(tot_lin):
        linha = []
        for j in range(tot_col):
            linha.append(valor)
        matriz.append(linha)
    return np.matrix(matriz)

print (cria_matriz(3, 4, 0))