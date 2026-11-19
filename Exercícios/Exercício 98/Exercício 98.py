import time

# Exercício 98 - Temperaturas da semana

def mediaTemperaturas(temperaturas):
    soma = 0

    for indice in range(len(temperaturas)):
        soma = soma + temperaturas[indice]

    return soma / len(temperaturas)


def maiorTemperatura(temperaturas):
    maior = temperaturas[0]

    for indice in range(1, len(temperaturas)):
        if temperaturas[indice] > maior:
            maior = temperaturas[indice]

    return maior


def menorTemperatura(temperaturas):
    menor = temperaturas[0]

    for indice in range(1, len(temperaturas)):
        if temperaturas[indice] < menor:
            menor = temperaturas[indice]

    return menor


def contarAcimaDaMedia(temperaturas):
    media = mediaTemperaturas(temperaturas)
    quantidade = 0

    for indice in range(len(temperaturas)):
        if temperaturas[indice] > media:
            quantidade = quantidade + 1

    return quantidade


temperaturas = []

for contador in range(1, 8):
    temperatura = float(input("Digite a temperatura do dia: "))
    temperaturas.append(temperatura)

print("Média:", format(mediaTemperaturas(temperaturas), ".2f"))
print("Maior:", maiorTemperatura(temperaturas))
print("Menor:", menorTemperatura(temperaturas))
print("Dias acima da média:", contarAcimaDaMedia(temperaturas))

time.sleep(5)
