
import time

# Exercício 50 - Maior valor informado

maior = float(input("Digite o primeiro valor: "))

for contador in range(2, 11):
    valor = float(input("Digite outro valor: "))

    if valor > maior:
        maior = valor

print("Maior valor:", maior)

time.sleep(5)