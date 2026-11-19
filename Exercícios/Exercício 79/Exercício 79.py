import time

# Exercício 79 - Soma de cada linha e coluna

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

print("Somas das linhas:", end=" ")
for linha in range(3):
    soma_linha = 0

    for coluna in range(3):
        soma_linha = soma_linha + matriz[linha][coluna]

    print(soma_linha, end=" ")

print()
print("Somas das colunas:", end=" ")
for coluna in range(3):
    soma_coluna = 0

    for linha in range(3):
        soma_coluna = soma_coluna + matriz[linha][coluna]

    print(soma_coluna, end=" ")

time.sleep(5)