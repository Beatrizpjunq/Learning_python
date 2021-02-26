# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 12:00:36 2020

@author: filip
"""


n = int(input("Digite um número: "))
i = 0
soma = 0
while i < n:
    div = n // 10
    sob = n % 10
    soma = soma + sob
    n = div
    
print (soma)
