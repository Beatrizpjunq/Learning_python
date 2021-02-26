# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 23:49:00 2020

@author: filip
"""


x= int(input("insira o x:"))
i = int(x/2)
p = 0

if x == 2:
    print (2)
   
elif x > 2 and x < 5:
    i = x - 1
    x / i
    if x % i == 0:
        x = x -1
        i = x - 1 
    else:
        i = i - 1
        p = x
    print (p)
    
else:
    while i > 1:
        x / i
        if x % i == 0:
            x = x -1
            i = int(x / 2)
        
        else:
            i = i - 1
            p = x          
            print (p)



