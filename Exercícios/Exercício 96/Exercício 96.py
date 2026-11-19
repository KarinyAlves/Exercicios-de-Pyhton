import time

# Exercício 96 - Estatísticas de vendas

def totalVendas(vetor):
    total = 0

    for indice in range(len(vetor)):
        total = total + vetor[indice]

    return total


def mediaVendas(vetor):
    media = totalVendas(vetor) / len(vetor)
    return media


def maiorVenda(vetor):
    maior = vetor[0]

    for indice in range(1, len(vetor)):
        if vetor[indice] > maior:
            maior = vetor[indice]

    return maior


def contarAcimaDaMedia(vetor):
    media = mediaVendas(vetor)
    quantidade = 0

    for indice in range(len(vetor)):
        if vetor[indice] > media:
            quantidade = quantidade + 1

    return quantidade


vendas = []

for contador in range(1, 11):
    valor = float(input("Digite o valor da venda: "))
    vendas.append(valor)

print("Total vendido:", totalVendas(vendas))
print("Média das vendas:", format(mediaVendas(vendas), ".2f"))
print("Maior venda:", maiorVenda(vendas))
print("Vendas acima da média:", contarAcimaDaMedia(vendas))

time.sleep(5)