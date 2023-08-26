import os
import time
#Média das Notas /by Caio
nome = [2]
nota = [2]
cont = 0
soma = 0
while (cont <= 2):
    os.system('cls')
    auxiliarnome = input("Digite o nome do aluno: ")
    nome.append(auxiliarnome)
    auxiliarnota = float(input("Digite a nota do aluno: "))
    nota.append(auxiliarnota)
    os.system('cls')
    print("Aluno ",auxiliarnome," Cadastrado!! | Nota : ",auxiliarnota)
    cont = (cont+1)
    time.sleep(3)
cont = 0
while (cont <= 2):
    soma = soma + nota[cont]
    cont = (cont+1)
soma = soma/3
os.system('cls')
print("Média das Notas = ",soma)