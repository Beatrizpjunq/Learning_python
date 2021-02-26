# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 20:24:31 2020

@author: filip
"""


x = input("Digite um número inteiro: ")

num = int (x)

iguais = False

i = 0

while i < num and not iguais:
    inteiro = num // 10
    atual = num % 10
    ant =  inteiro % 10
    if atual == ant:
        iguais = True
    else:
        num = inteiro
if iguais:
    print ("sim")
            
else:
    print ("não")
            
        
    

