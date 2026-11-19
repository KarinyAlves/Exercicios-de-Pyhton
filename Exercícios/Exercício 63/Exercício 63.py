
import time

# Exercício 63 - Vetor em ordem inversa

vetor = []

for contador in range(1, 9):
    valor = int(input("Digite um número inteiro: "))
    vetor.append(valor)

print("Ordem inversa:", end=" ")

for indice in range(7, -1, -1):
    print(vetor[indice], end=" ")

time.sleep(5)
