
import time

# Exercício 76 - Leitura de matriz 3 x 3

matriz = []

for linha in range(3):
    valores_linha = []

    for coluna in range(3):
        valor = int(input("Digite um número inteiro: "))
        valores_linha.append(valor)

    matriz.append(valores_linha)

print("Matriz:")

for linha in range(3):
    print(matriz[linha])

time.sleep(5)
