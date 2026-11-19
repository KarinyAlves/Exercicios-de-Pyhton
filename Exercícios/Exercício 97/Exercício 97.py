import time

# Exercício 97 - Estatísticas da turma

def calcularMedia(notas):
    soma = 0

    for indice in range(len(notas)):
        soma = soma + notas[indice]

    return soma / len(notas)


def maiorNota(notas):
    maior = notas[0]

    for indice in range(1, len(notas)):
        if notas[indice] > maior:
            maior = notas[indice]

    return maior


def menorNota(notas):
    menor = notas[0]

    for indice in range(1, len(notas)):
        if notas[indice] < menor:
            menor = notas[indice]

    return menor


def nomesAcimaDaMedia(nomes, notas):
    media = calcularMedia(notas)
    nomes_acima = []

    for indice in range(len(notas)):
        if notas[indice] > media:
            nomes_acima.append(nomes[indice])

    return nomes_acima


nomes = []
notas = []

for contador in range(1, 9):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))

    nomes.append(nome)
    notas.append(nota)

print("Média:", format(calcularMedia(notas), ".2f"))
print("Maior nota:", maiorNota(notas))
print("Menor nota:", menorNota(notas))
print("Alunos acima da média:", nomesAcimaDaMedia(nomes, notas))

time.sleep(5)