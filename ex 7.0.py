# Escreva o seu programa

def primo(n):
    i = 2
    if n ==1:
        return False
    if n ==2:
        return True
    while n % i !=0 and i <= n/2:
        i = i + 1
    if n %i == 0:
        return False
    else:
        return True
       
      
#-----------------------------------------------------
n = int(input("digite um numero n ( ao digitar zero, termina a sequencia): "))
cont = 0
while n > 0:
    if primo(n): # chamada da funcao principal
        cont = cont + 1
    n = int(input("digite um numero n ( ao digitar zero, termina a sequencia): "))
print("encontrei", cont, "números primos!")
