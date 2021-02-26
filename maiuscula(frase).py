# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 21:37:57 2020

@author: filip
"""




def maiusculas(frase):
    tam = len(frase) - 1
    letra_mai =''
    i = 0
    while tam >= i:
        if ord(frase[i]) >= 65 and ord(frase[i]) <=90:
            letra_mai = letra_mai + frase[i]
        i += 1
    return (letra_mai)
    
    

         
       
        
