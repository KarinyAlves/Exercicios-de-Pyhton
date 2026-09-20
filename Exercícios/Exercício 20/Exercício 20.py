#Exercício em ordem crescente, e que aceite repetições
import time

valor_um = float(input("Digite o primeiro valor: "))
valor_dois = float(input("Digite o valor dois: "))
valor_tres = float(input("Digite o segundo valor: "))

if valor_um <= valor_dois and valor_dois <= valor_tres:
    print(valor_um, valor_dois, valor_tres)

elif valor_um <= valor_tres and valor_tres <= valor_dois:
    print(valor_um, valor_tres, valor_dois)

elif valor_dois <= valor_um and valor_um <= valor_tres:
    print(valor_dois, valor_um, valor_tres)

elif valor_dois <= valor_tres and valor_tres <= valor_um:
    print(valor_dois, valor_tres, valor_um)

elif valor_tres <= valor_um and valor_um <= valor_dois:
    print(valor_tres, valor_um, valor_dois)

else:
    print(valor_tres, valor_dois, valor_um)