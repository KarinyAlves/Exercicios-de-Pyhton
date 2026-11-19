import time

# Exercício 81 - Função para somar

def soma(primeiro_valor, segundo_valor):
    resultado = primeiro_valor + segundo_valor
    return resultado


resultado = soma(8, 5)
print("Resultado:", resultado)

resultado = soma(-3, 7)
print("Resultado:", resultado)

resultado = soma(2.5, 1.5)
print("Resultado:", resultado)

time.sleep(5)