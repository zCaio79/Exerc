import os
#Declarações
os.system('cls')
cont = 0
conta = 0.0
result = 0.0
num = float(input("Digite um Número: "))

conta = num
#Looping para Operações
while cont == 0:
   
    ope = str(input("Digite um Operador: "))
    match ope:
        case "+":
            num = float(input("Digite um Número: "))
            conta = conta + num

        case "-":
            num = float(input("Digite um Número: "))
            conta = conta - num
        case "x":
            num = float(input("Digite um Número: "))
            conta = conta * num
        case "/":
            num = float(input("Digite um Número: "))
            conta = conta / num
        case default:
            print("Operador Inválido Tente Novamente")
    
    result = conta
    print("Resultado atual: ",result)
    print("Deseja Continuar a Conta ?")
    op = str(input("Digite N p/ Finalizar OU qualquer outra letra p/ Continuar : "))
    #Segmento de opção
    if ((op == "N") or (op == "n")):
        cont = 1
    else:
        print("Contagem Atual: ",result)
        
os.system('cls')
print("Resultado da conta =  ",result)