
import time

# Exercício 54 - Soma dos múltiplos de 3

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

soma = 0

if a <= b:
    for numero in range(a, b + 1):
        if numero % 3 == 0:
            soma = soma + numero
else:
    for numero in range(b, a + 1):
        if numero % 3 == 0:
            soma = soma + numero

print("Soma dos múltiplos de 3:", soma)

time.sleep(5)
