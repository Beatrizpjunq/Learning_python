# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 21:54:13 2020

@author: filip
"""






l = int(input("Digite a largura: "))
a = int(input("Digite a altura: "))
i = l
j = a

while a <= j and a >=1:
    while l <= i and l >=1:
        if l == i or l == 1 or a == j or a == 1:
            print ("#", end = "")
            l = l - 1
        else:
            print (" ", end = "")
            l = l - 1
    a = a - 1
    l = i
    print ()
    













'''

while l > i :
    print ("#", end = " ")
    i = i + 1
print ()
l = i
if a > 3:
    b = a -2
while b >= 1:
    print("#", end = " ")
    while (l - 2) > i :
        print (" ", end = " ")
        i = i + 1
    a = a - 1
    l = i
    i = 0
    print ('#')
l = i
i = 0
while l > i :
        print ("#", end = " ")
        i = i + 1    

'''        
