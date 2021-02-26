# -*- coding: utf-8 -*-

import math

x1 = int(input("Digite o x1: "))
y1 = int(input("Digite o y1: "))
x2 = int(input("Digite o x2: "))
y2 = int(input("Digite o y2: "))

d = math.sqrt((x1 - x2)**2 + (y1-y2)**2)

if d >= 10:
    print ("longe")
    
else:
    print ("perto")