import time

# Exercício 95 - Contar ocorrências em função

def contarOcorrencias(vetor, valor_procurado):
    quantidade = 0

    for indice in range(len(vetor)):
        if vetor[indice] == valor_procurado:
            quantidade = quantidade + 1

    return quantidade


print(contarOcorrencias([3, 5, 3, 8, 3], 3))
print(contarOcorrencias([1, 2, 3], 4))
print(contarOcorrencias([7, 7, 7, 7], 7))

time.sleep(5)