
import time

# Exercício 88 - N-ésimo termo de Fibonacci

def fibonacci(indice):
    if indice == 0:
        return 0
    elif indice == 1:
        return 1
    else:
        anterior = 0
        atual = 1

        for contador in range(2, indice + 1):
            proximo = anterior + atual
            anterior = atual
            atual = proximo

        return atual


print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(6))
print(fibonacci(10))

time.sleep(5)
