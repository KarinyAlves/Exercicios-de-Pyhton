
import time

# Exercício 65 - Valores acima da média

notas = []
soma = 0

for contador in range(1, 9):
    nota = float(input("Digite uma nota: "))
    notas.append(nota)
    soma = soma + nota

media = soma / 8
quantidade_acima = 0

print("Média:", media)
print("Notas acima da média:", end=" ")

for indice in range(8):
    if notas[indice] > media:
        print(notas[indice], end=" ")
        quantidade_acima = quantidade_acima + 1

if quantidade_acima == 0:
    print("NENHUMA")

print()
print("Quantidade:", quantidade_acima)

time.sleep(5)
