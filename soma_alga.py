# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 19:20:31 2020

@author: filip
"""

n = input("digite um número: ")
tam = len(n)
i = 0
num = int(n)
soma = 0
while i < tam:
    rest = num % 10
    soma = soma + rest
    num = num // 10
    i = i + 1 

print ("A soma dos algarismos do seu número é: ", soma)
