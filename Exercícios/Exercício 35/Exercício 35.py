import time
idade = int(input("Digite a idade: "))

estudante = input("É estudante? (sim/não): ")


if idade < 0:
    print("IDADE INVÁLIDA")

elif estudante != "sim" and estudante != "não":
    print("RESPOSTA INVÁLIDA")

elif idade < 12 or estudante == "sim" or idade >= 60:
    valor = 30 * 0.50

    print("Valor do ingresso:", valor)

else:
    valor = 30

    print("Valor do ingresso:", valor)

time.sleep(5)