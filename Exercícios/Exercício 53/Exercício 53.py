
import time

# Exercício 53 - Pesquisa de alturas

primeira_altura = float(input("Digite a primeira altura: "))

soma_alturas = primeira_altura
maior_altura = primeira_altura
menor_altura = primeira_altura

for contador in range(2, 9):
    altura = float(input("Digite outra altura: "))
    soma_alturas = soma_alturas + altura

    if altura > maior_altura:
        maior_altura = altura

    if altura < menor_altura:
        menor_altura = altura

media = soma_alturas / 8

print("Média:", format(media, ".2f"), "m")
print("Maior:", format(maior_altura, ".2f"), "m")
print("Menor:", format(menor_altura, ".2f"), "m")

time.sleep(5)