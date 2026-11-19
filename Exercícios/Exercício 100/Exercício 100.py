
import time

# Exercício 100 - Desafio final: análise de uma turma

def calcularMedia(notas):
    soma = 0

    for indice in range(len(notas)):
        soma = soma + notas[indice]

    return soma / len(notas)


def encontrarMaiorNota(notas):
    maior = notas[0]
    indice_maior = 0

    for indice in range(1, len(notas)):
        if notas[indice] > maior:
            maior = notas[indice]
            indice_maior = indice

    return indice_maior


def encontrarMenorNota(notas):
    menor = notas[0]
    indice_menor = 0

    for indice in range(1, len(notas)):
        if notas[indice] < menor:
            menor = notas[indice]
            indice_menor = indice

    return indice_menor


def contarAprovados(notas):
    quantidade = 0

    for indice in range(len(notas)):
        if notas[indice] >= 7:
            quantidade = quantidade + 1

    return quantidade


def encontrarMaisVelho(idades):
    maior_idade = idades[0]
    indice_mais_velho = 0

    for indice in range(1, len(idades)):
        if idades[indice] > maior_idade:
            maior_idade = idades[indice]
            indice_mais_velho = indice

    return indice_mais_velho


def nomesAcimaDaMedia(nomes, notas):
    media = calcularMedia(notas)
    nomes_acima = []

    for indice in range(len(notas)):
        if notas[indice] > media:
            nomes_acima.append(nomes[indice])

    return nomes_acima


nomes = []
idades = []
notas = []

for contador in range(1, 11):
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    nota = float(input("Digite a nota do aluno: "))

    nomes.append(nome)
    idades.append(idade)
    notas.append(nota)

indice_maior_nota = encontrarMaiorNota(notas)
indice_menor_nota = encontrarMenorNota(notas)
indice_mais_velho = encontrarMaisVelho(idades)

print("Média das notas:", format(calcularMedia(notas), ".2f"))
print("Maior nota:", nomes[indice_maior_nota], "-", notas[indice_maior_nota])
print("Menor nota:", nomes[indice_menor_nota], "-", notas[indice_menor_nota])
print("Aprovados:", contarAprovados(notas))
print("Aluno mais velho:", nomes[indice_mais_velho], "-", idades[indice_mais_velho], "anos")
print("Alunos acima da média:", nomesAcimaDaMedia(nomes, notas))

time.sleep(5)