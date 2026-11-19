import time

# Exercício 49 - Pares e ímpares

pares = 0
impares = 0

for contador in range(1, 7):
    valor = int(input("Digite um número inteiro: "))

    if valor % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

print("Pares:", pares)
print("Ímpares:", impares)

time.sleep(5)
