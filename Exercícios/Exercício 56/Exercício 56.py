import time

# Exercício 56 - Validação de nota

nota = float(input("Digite uma nota de 0 a 10: "))
tentativas_invalidas = 0

while nota < 0 or nota > 10:
    print("Valor inválido.")
    tentativas_invalidas = tentativas_invalidas + 1
    nota = float(input("Digite uma nota de 0 a 10: "))

print("Nota aceita:", nota)
print("Tentativas inválidas:", tentativas_invalidas)

time.sleep(5)
