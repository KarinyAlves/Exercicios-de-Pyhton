import time
mes = int(input("Digite o mês: "))

ano = int(input("Digite o ano: "))


if mes < 1 or mes > 12:
    print("MÊS INVÁLIDO")

elif ano <= 0:
    print("ANO INVÁLIDO")

elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    print("31 dias")

elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    print("30 dias")

else:

    if ano % 400 == 0:
        print("29 dias")

    elif ano % 4 == 0 and ano % 100 != 0:
        print("29 dias")

    else:
        print("28 dias")

time.sleep(5)
