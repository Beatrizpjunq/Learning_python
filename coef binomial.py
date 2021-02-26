# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 21:10:21 2020

@author: filip
"""
from fat import fatorial


n = int(input("digite um número n: "))
k = int(input("digite uma classe k: "))


coef = (fatorial(n)/ (fatorial(k)* fatorial(n-k)))

print (round(coef, 2))