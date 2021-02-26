# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 19:01:00 2020

@author: filip
"""

def Primo (n):
    i = 2
    if n == 2:
        return True
    while n % i != 0 and i <= n/2:
        i = i + 1
    if n % i == 0:
        return False
    else:
        return True


n = int(input("Insira um número inteiro positivo: "))
while n > 0:
    if Primo(n):
        print ("É primo")
    else:
        print ("não é primo")
    n = int(input("Insira um número inteiro positivo: "))
      

        
    
