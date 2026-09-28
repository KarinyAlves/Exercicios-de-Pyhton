import math

def calcular_hipotenusa(cateto_a, cateto_b):
    return math.sqrt(cateto_a**2 + cateto_b**2)

cateto_a = float(input("insira o valor de cateto a: "))
cateto_b = float(input("insira o valor de cateto b: "))

resultado = calcular_hipotenusa (cateto_a, cateto_b)

print(f"O valor é: {resultado}")