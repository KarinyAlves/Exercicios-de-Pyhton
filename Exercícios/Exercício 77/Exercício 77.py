
import time

# Exercício 77 - Soma dos elementos da matriz

matriz = []
soma = 0

for linha in range(3):
    valores_linha = []

    for coluna in range(3):
        valor = int(input("Digite um número inteiro: "))
        valores_linha.append(valor)
        soma = soma + valor

    matriz.append(valores_linha)

print("Matriz:")
for linha in range(3):
    print(matriz[linha])

print("Soma:", soma)

time.sleep(5)
