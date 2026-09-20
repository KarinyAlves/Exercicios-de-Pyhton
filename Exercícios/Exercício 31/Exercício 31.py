import time

numero = int(input("Digite um número inteiro: "))


if numero % 3 == 0 and numero % 5 == 0:
    print("DIVISÍVEL POR 3 E 5")

elif numero % 3 == 0:
    print("DIVISÍVEL APENAS POR 3")

elif numero % 5 == 0:
    print("DIVISÍVEL APENAS POR 5")

else:
    print("NÃO DIVISÍVEL POR 3 NEM 5")

time.sleep(5)