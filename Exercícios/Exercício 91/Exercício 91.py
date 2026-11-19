
import time

# Exercício 91 - Contar positivos no vetor

def contarPositivos(vetor):
    quantidade = 0

    for indice in range(len(vetor)):
        if vetor[indice] > 0:
            quantidade = quantidade + 1

    return quantidade


print(contarPositivos([5, -2, 0, 8, -1]))
print(contarPositivos([1, 2, 3]))
print(contarPositivos([-1, -2, 0]))

time.sleep(5)