import time

# Exercício 94 - Posições de um valor

def buscarPosicoes(vetor, valor_procurado):
    posicoes = []

    for indice in range(len(vetor)):
        if vetor[indice] == valor_procurado:
            posicoes.append(indice)

    return posicoes


print(buscarPosicoes([4, 7, 2, 7, 9], 7))
print(buscarPosicoes([5, 5, 5, 5], 5))
print(buscarPosicoes([1, 3, 5], 2))

time.sleep(5)
