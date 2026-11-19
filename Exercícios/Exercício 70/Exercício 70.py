import time

# Exercício 70 - Quantidade de ocorrências

vetor = []

for contador in range(1, 11):
    valor = int(input("Digite um número inteiro: "))
    vetor.append(valor)

valor_procurado = int(input("Digite o valor que deseja procurar: "))
ocorrencias = 0

for indice in range(10):
    if vetor[indice] == valor_procurado:
        ocorrencias = ocorrencias + 1

print("Ocorrências:", ocorrencias)

time.sleep(5)