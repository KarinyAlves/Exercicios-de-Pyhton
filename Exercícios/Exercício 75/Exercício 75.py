import time

# Exercício 75 - Ordenação crescente

vetor = []

for contador in range(1, 11):
    valor = int(input("Digite um número inteiro: "))
    vetor.append(valor)

for indice in range(9):
    for outra_posicao in range(9 - indice):
        if vetor[outra_posicao] > vetor[outra_posicao + 1]:
            valor_temporario = vetor[outra_posicao]
            vetor[outra_posicao] = vetor[outra_posicao + 1]
            vetor[outra_posicao + 1] = valor_temporario

print("Ordem crescente:", vetor)

time.sleep(5)

