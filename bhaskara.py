# -*- coding: utf-8 -*-
import math
a = float(input("digite o valor do coeficiente a:"))
b = float(input("digite o valor do coeficiente b:"))
c = float(input("digite o valor do coeficiente c:"))

delta = b ** 2 - (4 * a * c)
if delta < 0:
    print ("Esta equação não possui raízes reais") 

else:
    x1 = -(b + math.sqrt(delta))/(2*a)
    x2 = -(b - math.sqrt(delta))/(2*a)

    if delta > 0:
        print ("Suas raízes são: ", x1 ,"e", x2) 
        

    else:
        print ("Delta é igual a zero, logo sua raíz dupla é igual a: ", x1)
    
    

    
    
    