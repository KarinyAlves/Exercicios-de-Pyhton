import time

# Exercício 83 - Menor de três valores

def menor(primeiro_valor, segundo_valor, terceiro_valor):
    if primeiro_valor <= segundo_valor and primeiro_valor <= terceiro_valor:
        return primeiro_valor
    elif segundo_valor <= primeiro_valor and segundo_valor <= terceiro_valor:
        return segundo_valor
    else:
        return terceiro_valor


print(menor(3, 8, 5))
print(menor(-1, -7, -2))
print(menor(4, 4, 9))

time.sleep(5)