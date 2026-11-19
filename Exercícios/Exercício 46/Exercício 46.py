import time

# Exercício 46 - Soma de cinco valores

soma = 0

for contador in range(1, 6):
    valor = float(input("Digite um valor real: "))
    soma = soma + valor

print("Soma:", soma)

time.sleep(5)