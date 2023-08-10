#Calculadora IMC /by Caio

print("Calculadora IMC")
peso = float(input('Digite seu Peso : '))
altura = float(input('Digite sua Altura : '))
resp = peso / altura**2
print("IMC %.2f"%resp)

#Classificação
if resp<16.9:
    print("Muito Abaixo do Peso")
elif (resp>=17 and resp<=18.4):
    print("Abaixo do Peso")
elif (resp>=18.5 and resp<=24.9):
    print("Peso Normal")
elif (resp>=25 and resp<=29.9):
    print("Acima do Peso")
elif (resp>=30 and resp<=34.9):
    print("Obesidade I")
elif (resp>=35 and resp<=40):
    print("Obesidade II")
elif (resp>40):
    print("Obesidade III")
else:
    print("Valores inválidos")
