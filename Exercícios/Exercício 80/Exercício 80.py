import time

# Exercício 80 - Maior elemento da matriz

matriz = []

for linha in range(4):
    valores_linha = []

    for coluna in range(4):
        valor = int(input("Digite um número inteiro: "))
        valores_linha.append(valor)

    matriz.append(valores_linha)

maior = matriz[0][0]
primeira_linha = 0
primeira_coluna = 0

for linha in range(4):
    for coluna in range(4):
        if matriz[linha][coluna] > maior:
            maior = matriz[linha][coluna]
            primeira_linha = linha
            primeira_coluna = coluna

print("Maior valor:", maior)
print("Primeira posição: linha", primeira_linha, "coluna", primeira_coluna)

time.sleep(5)
