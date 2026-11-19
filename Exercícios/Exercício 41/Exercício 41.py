import time

# Exercício 41 - Tabuada de um número

numero = int(input("Digite um número inteiro: "))

for multiplicador in range(1, 11):
    resultado = numero * multiplicador
    print(numero, "x", multiplicador, "=", resultado)

time.sleep(5)