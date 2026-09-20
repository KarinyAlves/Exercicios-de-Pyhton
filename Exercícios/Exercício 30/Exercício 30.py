import time
valor_imovel = float(input("Digite o valor do imóvel: "))

salario = float(input("Digite o salário mensal: "))

anos = int(input("Digite o prazo em anos: "))


if valor_imovel <= 0:
    print("VALOR DO IMÓVEL INVÁLIDO")

elif salario <= 0:
    print("SALÁRIO INVÁLIDO")

elif anos <= 0:
    print("PRAZO INVÁLIDO")

else:
    meses = anos * 12

    prestacao = valor_imovel / meses

    limite = salario * 0.30

    print("Prestação:", prestacao)
    print("Limite:", limite)

    if prestacao <= limite:
        print("APROVADO")

    else:
        print("NEGADO")

time.sleep(5)