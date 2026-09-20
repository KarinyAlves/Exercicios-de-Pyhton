import time
ano = int(input("Digite o ano: "))


if ano <= 0:
    print("ANO INVÁLIDO")

elif ano % 400 == 0:
    print("BISSEXTO")

elif ano % 4 == 0 and ano % 100 != 0:
    print("BISSEXTO")

else:
    print("NÃO BISSEXTO")

time.sleep(5)