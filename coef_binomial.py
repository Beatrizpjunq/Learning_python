# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 22:19:52 2020

@author: filip
"""


from fat import fatorial


def num_binomial(n,k):
    coef = fatorial(n)/ (fatorial(k) * fatorial(n-k) )
    return round(coef, 2)



