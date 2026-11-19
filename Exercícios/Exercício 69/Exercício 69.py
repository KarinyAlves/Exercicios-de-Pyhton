import time

# Exercício 69 - Busca de valor no vetor

vetor = []

for contador in range(1, 11):
    valor = int(input("Digite um número inteiro: "))
    vetor.append(valor)

valor_procurado = int(input("Digite o valor que deseja procurar: "))
encontrou = False

print("Posições:", end=" ")

for indice in range(10):
    if vetor[indice] == valor_procurado:
        print(indice, end=" ")
        encontrou = True

if encontrou == False:
    print("VALOR NÃO ENCONTRADO")

time.sleep(5)