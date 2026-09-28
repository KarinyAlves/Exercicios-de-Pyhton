import math

numero = float(input("Digite um número inteiro: "))

while numero <=0:
    print("Verifique se você antedeu os requisitos estabelecidos e tente novamente")
    numero = float(input("Digite um número inteiro: "))

raiz = math.sqrt(numero)

print(f"O número é {numero} e a raiz deste número é {raiz}")
print(f"O número é {numero} e a raiz deste número, quando arredondado para baixo, é {math.floor(raiz)}")
print(f"O número é {numero} e a raiz deste número, quando arredondada para cima, é {math.ceil(raiz)}")