# Crie uma função chamada calcular_area_circulo(raio) que receba o raio de um círculo como parâmetro e retorne a área desse círculo.
# Dica: A fórmula da área é A = π × r **2. Utilize a constante math.pi .
# No fluxo principal do código, solicite o valor do raio ao usuário, chame a função criada e exiba o
# resultado final formatado com 2 casas decimais.

import math

def calcular_area_circulo (raio):
    return math.pi * (raio **2)

r = float(input("Digite o valor referente ao raio: "))

area = calcular_area_circulo(r)

print(f"A área do círculo é: {area:.2f}")
