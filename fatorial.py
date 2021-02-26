# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 10:28:06 2020

@author: filip
"""


n = int(input("Digite o valor de n: "))
i = 1
m = n - 1
f = n * m

if n <= 1:
    print (1)   
else:
    while i < m:
        ant = m - 1
        f = f * ant
        m = ant
    print (f)