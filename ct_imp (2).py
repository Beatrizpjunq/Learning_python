# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 11:52:39 2020

@author: filip
"""


n = int(input("Digite um número inteiro: "))
i = 1
ip = 1
while i > 0 and ip <= n :
    if i % 2 != 0:
        print (i)
        ip = ip + 1
    i = i + 1