# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 00:13:55 2020

@author: filip
"""


def maior_primo (x):
    i = x -1
    p = 0
    if x ==2:
        return 2
    else:
        while i > 1:
            x / i
            if x % i == 0:
                x = x -1
                i = x - 1
            else:
                i = i - 1
                p = x          
        return p
        





