# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 19:49:43 2020

@author: filip
"""

from fat import fatorial

n = 1
while n >= 0:
    n = int(input("Digite um número inteiro: "))
    while n > 1:
        print (fatorial(n))
        break
        