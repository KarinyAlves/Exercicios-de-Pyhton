import time

# Exercício 44 - Fatorial

numero = int(input("Digite um número inteiro de 0 até 12: "))

if numero < 0 or numero > 12:
    print("VALOR INVÁLIDO")
else:
    fatorial = 1

    for contador in range(1, numero + 1):
        fatorial = fatorial * contador

    print(numero, "! =", fatorial)

time.sleep(5)