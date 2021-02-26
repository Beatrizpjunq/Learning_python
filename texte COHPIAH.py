# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 20:24:53 2020

@author: filip
"""

import re

texto = "Muito além, nos confins inexplorados da região mais brega da Borda Ocidental desta Galáxia, há um pequeno sol amarelo e esquecido. Girando em torno deste sol, a uma distancia de cerca de 148 milhões de quilômetros, há um planetinha verde-azulado absolutamente insignificante, cujas formas de vida, descendentes de primatas, são tão extraordinariamente primitivas que ainda acham que relógios digitais são uma grande ideia."
texto1 = ['Muito além, nos confins inexplorados da região mais brega da Borda Ocidental desta Galáxia, há um pequeno sol amarelo e esquecido', ' Girando em torno deste sol, a uma distancia de cerca de 148 milhões de quilômetros, há um planetinha verde-azulado absolutamente insignificante, cujas formas de vida, descendentes de primatas, são tão extraordinariamente primitivas que ainda acham que relógios digitais são uma grande ideia']


def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    sentenca = re.split(r'[,:;]+', sentenca)
    return sentenca
    
def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def lista_frases (sentenca):
    list_frases = []
    list_sent = separa_sentencas(sentenca)
    for sent in list_sent:
        novas_frases = separa_frases(sent)
        list_frases.extend(novas_frases)
    return list_frases
    
def lista_palavras (frases):
    list_palavras = []
    list_fr = lista_frases(frases)
    for frase in list_fr:
        novas_palavras = separa_palavras(frase)
        list_palavras.extend(novas_palavras)
    return list_palavras
    



def tam_medio (list_palavras): # Traço linguístico 1
    palavras = lista_palavras(texto)
    i = 0
    soma_palavras = 0
    while i < len(palavras):
        x = palavras[i]
        soma_palavras = soma_palavras + len(x)
        i +=1
    tam = soma_palavras/len(palavras)
    return tam

def type_token(list_palavras): # Traço linguístico 2
    palavras = lista_palavras(texto)
    TT = n_palavras_diferentes(palavras)/ len(palavras)
    return TT

def hapax_legomana (list_palavras): # Traço linguístico 3
    palavras = lista_palavras(texto)
    HL = n_palavras_unicas(palavras)/ len(palavras)
    return HL


def soma_caracteres_sentenca(lista_sent):
    lista_sent = separa_sentencas(texto)
    i = 0
    soma = 0
    while i < len(lista_sent):
        x = lista_sent[i]
        len(x)
        soma = soma + len(x)
        i +=1
    return soma

def tam_medio_sentenca(lista_sent): # Traço linguístico 4
    TMS = soma_caracteres_sentenca(lista_sent)/ len(separa_sentencas(lista_sent))
    return TMS

def frases (sentenca):
    list_frases = []
    list_sent = separa_sentencas(texto)
    for sent in list_sent:
        novas_frases = separa_frases(sent)
        list_frases.extend(novas_frases)
    return list_frases
    

def complexidade_sentenca (texto): # Traço linguístico 5
    CS = len(frases(texto))/ len(separa_sentencas(texto))
    return CS


def soma_caracteres_frases(lista_frases):
    lista_fr = frases(lista_frases)
    i = 0
    soma_fr = 0
    while i < len(lista_fr):
        x = lista_fr[i]
        len(x)
        soma_fr = soma_fr + len(x)
        i +=1
    return soma_fr

def tam_medio_frase(lista_frases): # Traço linguístico 6
    TMF = soma_caracteres_frases(lista_frases)/ len (frases(lista_frases))

    return TMF

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos


def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    i = 0
    soma = 0
    for i in range(6):
        soma += abs (as_a[i] - as_b[i])
    Sab = soma / 6
    return Sab

def calcula_assinatura(texto):
    as_b = []
    lista.append(tam_medio(texto))
    lista.append(type_token(texto))
    lista.append(hapax_legomana (texto))
    lista.append(tam_medio_sentenca(texto))
    lista.append(complexidade_sentenca (texto))
    lista.append(tam_medio_frase(texto))
    return as_b

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    lista_sab = []
    menor = 0
    for texto in textos:
        as_texto = calcula_assinatura(texto)
        comparar = compara_assinatura(ass_cp, as_texto)
        lista_sab.append(comparar)
    menor = min(lista_sab)
    return (lista.index(menor) + 1)




