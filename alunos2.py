n = int(input("insira a quantidade de alunos: "))
i = 0
r = 0
rp = 0
ap = 0
mb = 0
while i < n:
    x = float(input("Insira a nota do aluno:"))
    if x >= 3 and x < 5: 
        rp = rp + 1

    if x >= 5:
        ap = ap + 1

    if x >= 8:
        mb = mb + 1

    else:
        r = r + 1
    i = i + 1
             
print ("Total de alunos:", n, "\nReprovados:",rp,"\nAprovados:",ap, "\nDesempenho muito bom:", mb)
