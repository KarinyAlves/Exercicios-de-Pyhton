# Exercício 13 - Positivo, negativo ou zero

import time

numero = float(input("Digite um número: "))

if numero > 0:
    resultado = "POSITIVO"
elif numero < 0:
    resultado = "NEGATIVO"
else:
    resultado = "ZERO"

print(f"Resultado: {resultado}")

time.sleep(5)
