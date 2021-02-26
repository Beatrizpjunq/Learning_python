# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 20:41:43 2020

@author: filip
"""

n = 1
num = []
while n > 0:
    n = int(input("Digite uma sequencia de números terminado pelo número zero: "))
    num.append(n)
tam = len(num) - 2
while tam >= 0:
    print (num[tam], end = ", ")
    tam = tam - 1
        