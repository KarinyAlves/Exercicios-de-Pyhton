import time

# Exercício 47 - Média de dez notas

soma = 0

for contador in range(1, 11):
    nota = float(input("Digite uma nota de 0 a 10: "))

    while nota < 0 or nota > 10:
        print("NOTA INVÁLIDA")
        nota = float(input("Digite uma nota de 0 a 10: "))

    soma = soma + nota

media = soma / 10

print("Média:", media)

time.sleep(5)