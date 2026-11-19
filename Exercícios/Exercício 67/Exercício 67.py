import time

# Exercício 67 - Maior valor e posição

vetor = []

for contador in range(1, 9):
    valor = int(input("Digite um número inteiro: "))
    vetor.append(valor)

maior = vetor[0]
primeira_posicao = 0

for indice in range(1, 8):
    if vetor[indice] > maior:
        maior = vetor[indice]
        primeira_posicao = indice

print("Maior valor:", maior)
print("Primeira posição:", primeira_posicao)

time.sleep(5)