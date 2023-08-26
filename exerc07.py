import numpy as np
 
dieimes_matriz = np.array([[3,4,1],[3,2,1]])
i = 0
x = 0
soma = 0
for i in range(dieimes_matriz.shape[0]):
    for x in range(dieimes_matriz.shape[1]):
        soma = soma + dieimes_matriz[i][x]
print("Soma dos Número da Matriz = ",soma)