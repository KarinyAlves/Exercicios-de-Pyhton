
import time

# Exercício 78 - Diagonal principal

matriz = []

for linha in range(3):
    valores_linha = []

    for coluna in range(3):
        valor = int(input("Digite um número inteiro: "))
        valores_linha.append(valor)

    matriz.append(valores_linha)

soma = 0
print("Diagonal principal:", end=" ")

for indice in range(3):
    print(matriz[indice][indice], end=" ")
    soma = soma + matriz[indice][indice]

print()
print("Soma:", soma)

time.sleep(5)