import os
import time
#Média das Notas /by Caio

alunos = {}
i = 0
soma = 0
os.system('cls')
while i<=2:
    auxnome = str(input("Digite o Nome do Aluno: "))
    auxnota = float(input("Insira a Nota do Aluno: "))
    alunos[auxnome] = auxnota
    i = i+1
    os.system('cls')
    print("Aluno Adicionado")
    time.sleep(2)
    os.system('cls')
for x in alunos:
    print(x," : ",alunos[x])
    soma = soma+ alunos[x]
soma = soma/3
print("Média das Notas : ",soma)