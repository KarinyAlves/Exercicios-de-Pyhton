
import time

# Exercício 60 - Caixa de compras

quantidade_produtos = 0
total_compra = 0
maior_preco = 0

preco = float(input("Digite o preço do produto (0 para encerrar): "))

while preco != 0:
    if preco < 0:
        print("PREÇO INVÁLIDO")
    else:
        quantidade_produtos = quantidade_produtos + 1
        total_compra = total_compra + preco

        if preco > maior_preco:
            maior_preco = preco

    preco = float(input("Digite o preço do produto (0 para encerrar): "))

if quantidade_produtos == 0:
    print("NENHUM PRODUTO INFORMADO")
else:
    print("Produtos:", quantidade_produtos)
    print("Total da compra: R$", format(total_compra, ".2f"))
    print("Maior preço: R$", format(maior_preco, ".2f"))

time.sleep(5)