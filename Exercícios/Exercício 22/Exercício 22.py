import time
nota_um = float(input("Digite a primeira nota: "))

nota_dois = float(input("Digite a segunda nota: "))


if nota_um >= 0 and nota_um <= 10 and nota_dois >= 0 and nota_dois <= 10:

    media = (nota_um + nota_dois) / 2

    print("Média:", media)

    if media < 5:
        print("REPROVADO")

    elif media >= 5 and media < 7:
        print("RECUPERAÇÃO")

    else:
        print("APROVADO")

else:
    print("NOTA INVÁLIDA")

time.sleep(5)