import time

# Exercício 62 - Leitura e exibição de vetor

vetor = []

for contador in range(1, 9):
    valor = int(input("Digite um número inteiro: "))
    vetor.append(valor)

print("Vetor:", vetor)

time.sleep(5)
