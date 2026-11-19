import time

# Exercício 72 - Intercalar dois vetores

vetor_a = []
vetor_b = []
vetor_c = []

print("Digite os cinco valores do vetor A:")
for contador in range(1, 6):
    valor = int(input("Valor: "))
    vetor_a.append(valor)

print("Digite os cinco valores do vetor B:")
for contador in range(1, 6):
    valor = int(input("Valor: "))
    vetor_b.append(valor)

for indice in range(5):
    vetor_c.append(vetor_a[indice])
    vetor_c.append(vetor_b[indice])

print("Vetor C:", vetor_c)

time.sleep(5)