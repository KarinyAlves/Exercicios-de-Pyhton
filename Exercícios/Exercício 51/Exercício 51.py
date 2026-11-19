import time

# Exercício 51 - Maior e menor valor

primeiro_valor = float(input("Digite o primeiro valor: "))

maior = primeiro_valor
menor = primeiro_valor

for contador in range(2, 11):
    valor = float(input("Digite outro valor: "))

    if valor > maior:
        maior = valor

    if valor < menor:
        menor = valor

print("Maior:", maior)
print("Menor:", menor)

time.sleep(5)