
import time

# Exercício 52 - Pesquisa de idades

soma_idades = 0
menores_dezoito = 0
maiores_ou_iguais_sessenta = 0

for contador in range(1, 11):
    idade = int(input("Digite uma idade: "))

    while idade < 0:
        print("IDADE INVÁLIDA")
        idade = int(input("Digite uma idade: "))

    soma_idades = soma_idades + idade

    if idade < 18:
        menores_dezoito = menores_dezoito + 1

    if idade >= 60:
        maiores_ou_iguais_sessenta = maiores_ou_iguais_sessenta + 1

media = soma_idades / 10

print("Média das idades:", media)
print("Menores de 18:", menores_dezoito)
print("Com 60 anos ou mais:", maiores_ou_iguais_sessenta)

time.sleep(5)
