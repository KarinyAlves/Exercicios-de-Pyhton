import time

# Exercício 57 - Leitura até zero

quantidade = 0
soma = 0

valor = float(input("Digite um valor (0 para encerrar): "))

while valor != 0:
    quantidade = quantidade + 1
    soma = soma + valor
    valor = float(input("Digite um valor (0 para encerrar): "))

if quantidade == 0:
    print("NENHUM VALOR VÁLIDO")
else:
    media = soma / quantidade

    print("Quantidade:", quantidade)
    print("Soma:", soma)
    print("Média:", media)

time.sleep(5)