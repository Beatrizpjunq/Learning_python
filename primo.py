# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 12:56:39 2020

@author: filip
"""


n = int(input("Digite um número inteiro: "))

if n > 1 and n <= 3:
    print ("primo")
    
else:
    if n % 2 != 0 and n % 3 != 0 and n % 5 != 0 and n % 7 != 0:
        print ("primo")
    else:
        print ("não primo")