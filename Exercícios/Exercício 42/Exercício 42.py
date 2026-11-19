import time

# Exercício 42 - Tabuada com início e fim

numero = int(input("Digite o número da tabuada: "))
inicio = int(input("Digite o multiplicador inicial: "))
fim = int(input("Digite o multiplicador final: "))

if inicio <= fim:
    for multiplicador in range(inicio, fim + 1):
        resultado = numero * multiplicador
        print(numero, "x", multiplicador, "=", resultado)
else:
    for multiplicador in range(inicio, fim - 1, -1):
        resultado = numero * multiplicador
        print(numero, "x", multiplicador, "=", resultado)

time.sleep(5)

