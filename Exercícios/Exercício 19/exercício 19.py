##Exercício: Leia três números reais e mostre o maior e o menor valor informado.

import time


primeiro_valor= float(input("Insira o primeiro valor: "))

segundo_valor = float(input("Insira o segundo valor: "))

terceiro_valor = float(input("Insira o terceiro valor: "))

if primeiro_valor > segundo_valor and primeiro_valor > terceiro_valor:
    print(f"O maior valor é {primeiro_valor}")

elif segundo_valor > primeiro_valor and terceiro_valor:
    print(f"O maior valor é {segundo_valor}")

elif terceiro_valor > primeiro_valor and segundo_valor:
    print(f"O maior valor é o {terceiro_valor}")

else:
    print("valores iguais")

time.sleep(5)
