
import time

# Exercício 92 - Média dos elementos do vetor

def mediaVetor(vetor):
    soma = 0

    for indice in range(len(vetor)):
        soma = soma + vetor[indice]

    media = soma / len(vetor)
    return media


print(mediaVetor([2, 4, 6, 8]))
print(mediaVetor([10, 10, 10]))
print(mediaVetor([-5, 5]))

time.sleep(5)