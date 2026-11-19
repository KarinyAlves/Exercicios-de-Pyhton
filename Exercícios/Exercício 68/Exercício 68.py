import time

# Exercício 68 - Menor valor e posição

vetor = []

for contador in range(1, 9):
    valor = int(input("Digite um número inteiro: "))
    vetor.append(valor)

menor = vetor[0]
primeira_posicao = 0

for indice in range(1, 8):
    if vetor[indice] < menor:
        menor = vetor[indice]
        primeira_posicao = indice

print("Menor valor:", menor)
print("Primeira posição:", primeira_posicao)

time.sleep(5)