import time

# Exercício 58 - Idades até valor negativo

quantidade = 0
soma_idades = 0
maiores_dezoito = 0

idade = int(input("Digite uma idade (valor negativo para encerrar): "))

while idade >= 0:
    quantidade = quantidade + 1
    soma_idades = soma_idades + idade

    if idade >= 18:
        maiores_dezoito = maiores_dezoito + 1

    idade = int(input("Digite uma idade (valor negativo para encerrar): "))

if quantidade == 0:
    print("NENHUMA IDADE INFORMADA")
else:
    media = soma_idades / quantidade

    print("Quantidade:", quantidade)
    print("Média:", media)
    print("Maiores ou iguais a 18 anos:", maiores_dezoito)

time.sleep(5)