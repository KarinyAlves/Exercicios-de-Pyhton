
import time

# Exercício 43 - Somatório de 1 até N

n = int(input("Digite um número inteiro positivo: "))

if n <= 0:
    print("VALOR INVÁLIDO")
else:
    soma = 0

    for numero in range(1, n + 1):
        soma = soma + numero

    print("Soma:", soma)

time.sleep(5)
