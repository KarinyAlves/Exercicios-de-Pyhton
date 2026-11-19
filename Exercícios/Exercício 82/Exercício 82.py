import time

# Exercício 82 - Função maior

def maior(primeiro_valor, segundo_valor):
    if primeiro_valor > segundo_valor:
        return primeiro_valor
    else:
        return segundo_valor


print(maior(8, 3))
print(maior(4, 11))
print(maior(-2, -7))
print(maior(5, 5))

time.sleep(5)
