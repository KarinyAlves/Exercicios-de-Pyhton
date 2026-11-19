
import time

# Exercício 48 - Positivos, negativos e zeros

positivos = 0
negativos = 0
zeros = 0

for contador in range(1, 9):
    valor = int(input("Digite um número inteiro: "))

    if valor > 0:
        positivos = positivos + 1
    elif valor < 0:
        negativos = negativos + 1
    else:
        zeros = zeros + 1

print("Positivos:", positivos)
print("Negativos:", negativos)
print("Zeros:", zeros)

time.sleep(5)
