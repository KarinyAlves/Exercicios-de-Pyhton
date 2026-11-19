import time

# Exercício 64 - Soma dos elementos do vetor

vetor = []
soma = 0

for contador in range(1, 11):
    valor = float(input("Digite um número real: "))
    vetor.append(valor)
    soma = soma + valor

print("Vetor:", vetor)
print("Soma:", soma)

time.sleep(5)