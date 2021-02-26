# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 21:54:13 2020

@author: filip
"""

l = int(input("Digite a largura: "))
a = int(input("Digite a altura: "))
i = 0
while a >= 1:
    while l > i :
        print ("#", end = "")
        i = i + 1
    a = a - 1
    l = i
    i = 0
    print ()
    

        