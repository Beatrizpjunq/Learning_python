# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 10:10:51 2020

@author: filip
"""



def usuario_escolhe_jogada (n, m):
    mov = int(input("Quantas peças você vai tirar? "))
    while mov > m or mov <= 0:
        print ("Oops! Jogada inválida! Tente de novo.")
        mov = int(input("Quantas peças você vai tirar? "))
    return mov
     
        
def computador_escolhe_jogada (n, m):
     mov = m
     if m >= n:
        mov = n
        return mov
     else:
        mov = n % (m + 1)
        if mov > 0:
            return mov 
     

def partida ():
    
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogadas? "))
    
    if n % (m+1) == 0:
        print ("Você começa!")
        Turno_usuario = True
                            
    else: 
        print ("Computador começa!")
        Turno_usuario = False
        
    while n > 0:
        if Turno_usuario == False:
            mov2 = computador_escolhe_jogada(n, m)
            Turno_usuario = True
            n = n - mov2
            print ("O computador tirou", mov2, "peças.")
        
        else:
            mov = usuario_escolhe_jogada(n, m)
            Turno_usuario = False
            n = n - mov
            print ("Você tirou", mov, "peças." )
        if n != 0:
            print ("Agora restam apenas", n, "peças no tabuleiro.")
        
    if Turno_usuario == True:
        print ("Fim do jogo! O computador ganhou!")
        return 0
    else:
        print ("Fim do jogo! Você ganhou!")
        return 1
        

def campeonato ():
    cont = 0
    resultadoJ = 0
    resultadoC = 0
    while cont < 3:
        cont +=1
        print ("**** Rodada",cont, "****")
        resultado = partida()
        if resultado == 1:
            resultadoJ = resultadoJ + 1
        else:
            resultadoC = resultadoC + 1
    print("Placar: Você",resultadoJ,"x",resultadoC,"Computador")
             
                    
    
       
print ("Bem-vindo ao jogo do NIM! Escolha:")

j = int(input("1 - para jogar uma partida isolada\n2 - para jogar um campeonato "))

while (j != 1 and j != 2):
    j = int(input("1 - para jogar uma partida isolada\n2 - para jogar um campeonato "))
        
if j == 1:
    print ("Você escolheu uma partida isolada")
    partida()   
elif j == 2:
    print ("Você esccolheu um campeonato")
    campeonato()



'''


m = número máximo de peças a ser retirada
n = número de peças inicial
 se n deve ser multiplo de (m+1):
     jogador começa
     se não: computador começa
'''    
     
