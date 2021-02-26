# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 11:36:10 2020

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

lista_sent = separa_sentencas(texto)
def soma_caracteres(lista_sent):
    i = 0
    soma = 0
    while i < len(lista_sent):
        x = lista_sent[i]
        len(x)
        soma = soma + len(x)
        i +=1
    return soma

def tam_medio_sentenca(lista_sent):
    TMS = soma_caracteres(lista_sent)/len (lista_sent)
    return TMS

print (tam_medio_sentenca(lista_sent))




