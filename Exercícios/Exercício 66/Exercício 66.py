
import time

# Exercício 66 - Pares e suas posições

vetor = []

for contador in range(1, 11):
    valor = int(input("Digite um número inteiro: "))
    vetor.append(valor)

encontrou_par = False

for indice in range(10):
    if vetor[indice] % 2 == 0:
        print("Valor", vetor[indice], "- posição", indice)
        encontrou_par = True

if encontrou_par == False:
    print("NENHUM VALOR PAR")

time.sleep(5)
