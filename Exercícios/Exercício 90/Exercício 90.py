import time

# Exercício 90 - Procedimento para mostrar a tabuada

def mostrarTabuada(numero):
    for multiplicador in range(1, 11):
        resultado = numero * multiplicador
        print(numero, "x", multiplicador, "=", resultado)


mostrarTabuada(4)

time.sleep(5)