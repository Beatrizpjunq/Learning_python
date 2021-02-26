# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 14:06:06 2020

@author: filip
"""


def soma_matrizes(m1, m2):
    len1 = len(m1),len(m1[0])
    len2 = len(m2),len(m2[0])
    matriz_iguais = False
    if len1 == len2 and matriz_iguais == False:
        matriz_iguais = True
        matriz_soma = []
        for i in range (len(m1)):
            linha_soma = []
            for j in range (len(m1[0])):
                soma = m1[i][j] + m2[i][j]
                linha_soma.append(soma)
            matriz_soma.append(linha_soma)
        return matriz_soma
    else:
        return matriz_iguais
        
        




        
            
