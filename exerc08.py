
#funções /by Caio

def mensagem():
    # Imprime uma mensagem de boas-vindas
    print("Oi professor Dieimes!!")

def soma(a, b):
    # Emite a soma de a + b
    result = a + b
    # Imprime o resultado
    print("resultado : ", result)

def calcular_area_retangulo(base, altura):
    # Calcula a área do retângulo
    area = base * altura
    # Retorna o valor da área
    return area


# Chamando a função mensagem
mensagem()
# Chamando a função soma
soma(3, 5)

# Chamando a função e armazenando o retorno em uma variável
resultado = calcular_area_retangulo(4, 6)
# Imprime o resultado
print("A área é: ", resultado)