import os
os.system('cls')
cont = 0
conta = 0.0
result = 0.0
num = float(input("Digite um Número: "))

conta = num
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
            print("Operador Inválido")
    result = conta
    print(result)
    print("Deseja Continuar a Conta ?")
    op = str(input("Digite:\tN p/ Finalizar\tQualquer outra p/ Continuar "))
    if ((op == "N") or (op == "n")):
        cont = 1
    else:
        print("Contagem Atual: ",result)
        
os.system('cls')
print("Resultado da conta =  ",result)
