
import time

# Exercício 99 - Controle de estoque

def calcularValorTotal(quantidades, precos):
    total = 0

    for indice in range(len(quantidades)):
        valor_produto = quantidades[indice] * precos[indice]
        total = total + valor_produto

    return total


def contarProdutosMenorQueCinco(quantidades):
    quantidade = 0

    for indice in range(len(quantidades)):
        if quantidades[indice] < 5:
            quantidade = quantidade + 1

    return quantidade


def encontrarProdutoMaiorValor(quantidades, precos):
    indice_maior = 0
    maior_valor = quantidades[0] * precos[0]

    for indice in range(1, len(quantidades)):
        valor_produto = quantidades[indice] * precos[indice]

        if valor_produto > maior_valor:
            maior_valor = valor_produto
            indice_maior = indice

    return indice_maior


nomes = []
quantidades = []
precos = []

for contador in range(1, 9):
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade em estoque: "))
    preco = float(input("Digite o preço unitário: "))

    nomes.append(nome)
    quantidades.append(quantidade)
    precos.append(preco)

indice_maior = encontrarProdutoMaiorValor(quantidades, precos)
valor_maior = quantidades[indice_maior] * precos[indice_maior]

print("Valor total do estoque: R$", format(calcularValorTotal(quantidades, precos), ".2f"))
print("Produtos com quantidade menor que 5:", contarProdutosMenorQueCinco(quantidades))
print("Maior valor em estoque:", nomes[indice_maior], "- R$", format(valor_maior, ".2f"))

time.sleep(5)