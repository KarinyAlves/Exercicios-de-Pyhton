import time
salario = float(input("Digite o salário atual: "))


if salario < 0:
    print("SALÁRIO INVÁLIDO")

elif salario <= 1500:
    percentual = 15
    aumento = salario * 0.15

elif salario >= 1500.01 and salario <= 3000:
    percentual = 10
    aumento = salario * 0.10

else:
    percentual = 5
    aumento = salario * 0.05


if salario >= 0:
    novo_salario = salario + aumento

    print("Percentual aplicado:", percentual, "%")
    print("Valor do aumento:", aumento)
    print("Novo salário:", novo_salario)

time.sleep(5)