
import time

# Exercício 93 - Maior valor do vetor

def maiorVetor(vetor):
    maior = vetor[0]

    for indice in range(1, len(vetor)):
        if vetor[indice] > maior:
            maior = vetor[indice]

    return maior


print(maiorVetor([4, 7, 2, 9, 5]))
print(maiorVetor([-8, -2, -5]))
print(maiorVetor([3, 3, 3]))

time.sleep(5)