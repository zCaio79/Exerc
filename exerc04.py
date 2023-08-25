import os
import time

lista = []
i=0
cont=0

while cont==0:
    
    print("\t\tMINHA LISTA\n")
    op = input("\t(Opções)\n\t[1]Adicionar Item\n\t[2]Excluir Item\n\t[3]Editar Item\n\t[4]Imprimir Lista\n\t[5]Sair\n\nDigite a Opção: ")
    match op:
        case "1":
                os.system('cls')
                auxiliar = str(input("(Adicionar)\t Nome do Item: "))
                if auxiliar in lista:
                       print("Item já Existente!!")
                else:
                        lista.append(auxiliar)
                        print("Item Adicionado!! : ",auxiliar)
        case "2":
                os.system('cls')
                auxiliar = str(input("(Excluir)\t Nome do Item: "))
                if auxiliar in lista:
                        lista.remove(auxiliar)
                        print("Item Excluido!! : ",auxiliar)
                else:
                       print("Item Não Encontadro, tente Novamente!!")
                       time.sleep(3)
        case "3":
                os.system('cls')
                auxiliar = str(input("(Editar)\t Nome do Item a ser editado: "))
                
                if auxiliar in lista:
                       print("Editando o Item ",auxiliar)
                       newaux = auxiliar
                       newaux = str(input("Digite a Nova versão: "))
                       local = lista.index(auxiliar)
                       lista[local] = newaux
                       print("Item Editado!! : ",auxiliar,"--> ",newaux)
                else:
                       print("Item Não Encontadro, tente Novamente!!")
                       time.sleep(3) 
                
        case "4":
                os.system('cls')
                print("\t [Lista]")
                num = 0
                for x in lista:
                       num = num+1
                       print("\t[",num,"] ",x)
                time.sleep(4)
        case "5":
                os.system('cls')
                print("\tLista Finalizada!!")
                cont = 1
        case default:
                os.system('cls')
                print("Opção Inválida, Tente Novamente!!")


