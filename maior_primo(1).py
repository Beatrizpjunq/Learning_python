# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 00:30:35 2020

@author: filip
"""


x= int(input("insira um número maior ou igual a 2: "))
i = x -1
p = 0

if x == 2:
    print (2)
else:    
    while i > 1:
        x / i
        if x % i == 0:
            x = x -1
            i = x - 1
        
        else:
            i = i - 1
            p = x          
    print (p)