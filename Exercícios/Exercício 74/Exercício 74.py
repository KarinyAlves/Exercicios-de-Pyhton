
import time

# Exercício 74 - Nomes acima da média

nomes = []
notas = []
soma = 0

for contador in range(1, 6):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))

    nomes.append(nome)
    notas.append(nota)
    soma = soma + nota

media = soma / 5

print("Média:", media)
print("Alunos acima da média:")

for indice in range(5):
    if notas[indice] > media:
        print(nomes[indice])

time.sleep(5)