import os
import time

class ContarBancaria:
    saldo = 0
    def __init__(self,titular):
        self.titular = str(titular)

    def depositar(self):
        os.system('cls')
        print("\t_DEPOSITO_\n\n")
        valor = float(input("- Digite o Valor do deposito :  "))
        if(valor>0):
            self.saldo = (self.saldo + valor)
            os.system('cls')
            print("\n- ",valor,"R$ Adicionado a Sua conta com sucesso!!")
            time.sleep(3)
            return
        else:
            os.system('cls')
            print("Valor Rejeitado!!")
            time.sleep(3)
            return
    
    def sacar(self):
        os.system('cls')
        print("\t_SAQUE_\n\n")
        valor = float(input("$ Digite o Valor do Saque :  "))
        if (self.saldo < valor or self.saldo == 0):
            os.system('cls')
            print("\n- Saldo insuficiente para Saque")
            time.sleep(3)
            return
        if (self.saldo >= valor):
            self.saldo = (self.saldo - valor)
            os.system('cls')
            print("\n- ",valor,"R$ Retirado de Sua conta com sucesso!!")
            print("\n- ",self.saldo,"R$ Saldo Atual")
            time.sleep(3)
            return
        
    def ver_saldo(self):
        os.system('cls')
        print("|\t_EXTRATO_\n\n")
        print("| - Titular:\t",conta.titular)
        print("\n| - ",self.saldo,"R$ Saldo Atual")
        time.sleep(4)
        return
    
i = 0
cont = 0
while (i==0):
    while cont == 0:
        os.system('cls')
        print("\t_BANCO_JAMAL_\n\n")
        print("$ Bem vindo ao Cadastro!!")
        nome = str(input("\n(Digite Seu nome Completo)\n\n- Titular: \t"))
        if(nome != ""):
            os.system('cls')
            conta = ContarBancaria(nome)
            print("\n\tCadastro realizado com Sucesso!")
            cont = cont+1
        else:
            os.system('cls')
            print("\nTitular Inválido! Tente Novamente")
            time.sleep(3)
    os.system('cls')
    print("\t_BANCO_JAMAL_\n\n")
    print(" - Opções")
    print("\n(1) $ Depositar")
    print("\n(2) $ Sacar")
    print("\n(3) $ Extrato")
    print("\n(0) $ Sair")
    op = int(input("\n\nDigite a opção desejada:  "))

    match op:
        case 1:
            conta.depositar()
        case 2:
            conta.sacar()
        case 3:
            conta.ver_saldo()
        case 0:
            os.system('cls')
            print("\n\nSistema Finalizado!!")
            i = i+1
        case default:
            os.system('cls')
            print("Opção Inválida!, Tente Novamente")
            time.sleep(3)


