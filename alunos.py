n = int(input("insira a quantidade de alunos: "))
i = 1
soma = 0
while i <= n:
    x = float(input("Insira a nova do aluno: "))
    soma = soma + x
    i = i + 1
    
media =  soma / n   
print ("A média das notas dos alunos é: ", media)
                    
