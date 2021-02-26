# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 13:03:22 2020

@author: filip
"""
import re

texto = input("Digite o texto (aperte enter para sair):")

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(texto):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    frases = re.split(r'[.,:;]+', texto)
    if frases[-1] == '':
        del frases[-1]
    return frases

lista_fr = separa_frases(texto)

def soma_caracteres_sentenca(lista_fr):
    i = 0
    soma_fr = 0
    while i < len(lista_fr):
        x = lista_fr[i]
        len(x)
        soma_fr = soma_fr + len(x)
        i +=1
    return soma_fr

def tam_medio_frase(list_fr):
    TMF = soma_caracteres_sentenca(lista_fr)/ len (separa_frases(texto))
    return TMF
    
print (tam_medio_frase(texto))   