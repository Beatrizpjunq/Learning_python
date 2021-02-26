# -*- coding: utf-8 -*-
import math
a = float(input("digite o valor do coeficiente a:"))
b = float(input("digite o valor do coeficiente b:"))
c = float(input("digite o valor do coeficiente c:"))

delta = b ** 2 - (4 * a * c)
if delta < 0:
    print ("esta equação não possui raízes reais") 

else:
    x1 = -(b + math.sqrt(delta))/(2*a)
    x2 = -(b - math.sqrt(delta))/(2*a)

    if delta > 0:
        if x1 > x2:
            print ("as raízes da equação são", x2 ,"e", x1)
        else:
            print ("as raízes da equação são", x1 ,"e", x2)
    else:
        print ("a raiz desta equação é", x1)
    
    

    
    
    