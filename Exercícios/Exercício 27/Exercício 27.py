import time
peso = float(input("Digite o peso em kg: "))

altura = float(input("Digite a altura em metros: "))


if peso <= 0:
    print("PESO INVÁLIDO")

elif altura <= 0:
    print("ALTURA INVÁLIDA")

else:
    imc = peso / (altura * altura)

    print("IMC:", imc)

    if imc < 18.5:
        print("ABAIXO DA FAIXA")

    elif imc >= 18.5 and imc < 25:
        print("FAIXA NORMAL")

    elif imc >= 25 and imc < 30:
        print("ACIMA DA FAIXA")

    else:
        print("FAIXA ELEVADA")

time.sleep(5)
