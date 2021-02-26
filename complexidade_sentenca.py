# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 12:37:38 2020

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

sentenca = separa_sentencas(texto)
def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    frases = re.split(r'[.,:;]+', texto)
    if frases[-1] == '':
        del frases[-1]
    return frases

print (separa_frases(sentenca))


def complexidade_sentenca ():
    CS = len(separa_frases(sentenca))/ len (separa_sentencas(texto))
    return CS

print (complexidade_sentenca())