import time

# Exercício 71 - Copiar apenas valores positivos

vetor_a = []
vetor_b = []

for contador in range(1, 11):
    valor = float(input("Digite um número real: "))
    vetor_a.append(valor)

    if valor > 0:
        vetor_b.append(valor)

print("Vetor A:", vetor_a)

if len(vetor_b) == 0:
    print("VETOR VAZIO")
else:
    print("Vetor B:", vetor_b)

time.sleep(5)