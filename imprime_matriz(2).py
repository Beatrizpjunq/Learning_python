# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 18:55:40 2020

@author: filip
"""


def imprime_matriz(matriz):
    for i in range (len(matriz)):
        for j in range (len(matriz[0])):
            if(j == (len(matriz[0])) - 1):
                print(matriz[i][j])
            else:
                print (matriz [i][j], end= " ")

