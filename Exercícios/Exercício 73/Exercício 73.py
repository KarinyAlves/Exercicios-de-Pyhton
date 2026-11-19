import time

# Exercício 73 - Comparar dois vetores

vetor_a = []
vetor_b = []

print("Digite os cinco valores do vetor A:")
for contador in range(1, 6):
    valor = int(input("Valor: "))
    vetor_a.append(valor)

print("Digite os cinco valores do vetor B:")
for contador in range(1, 6):
    valor = int(input("Valor: "))
    vetor_b.append(valor)

encontrou_igual = False
print("Posições iguais:", end=" ")

for indice in range(5):
    if vetor_a[indice] == vetor_b[indice]:
        print(indice, end=" ")
        encontrou_igual = True

if encontrou_igual == False:
    print("NENHUMA POSIÇÃO")

time.sleep(5)
