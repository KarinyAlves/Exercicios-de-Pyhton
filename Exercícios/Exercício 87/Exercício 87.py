import time

# Exercício 87 - Função fatorial

def fatorial(numero):
    resultado = 1

    for contador in range(1, numero + 1):
        resultado = resultado * contador

    return resultado


print(fatorial(0))
print(fatorial(1))
print(fatorial(5))
print(fatorial(6))

time.sleep(5)
