# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 21:02:34 2020

@author: filip
"""


def fatorial (n):
    i = n
    f = 1

    while i > 1:
        f = f * i
        i = i - 1
    return  f
