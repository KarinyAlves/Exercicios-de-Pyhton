import time

idade = int(input("Digite a idade: "))


if idade < 0:
    print("IDADE INVÁLIDA")

elif idade < 16:
    print("NÃO PODE VOTAR")

elif idade >= 16 and idade < 18:
    print("VOTO OPCIONAL")

elif idade >= 18 and idade < 70:
    print("VOTO OBRIGATÓRIO")

else:
    print("VOTO OPCIONAL")

time.sleep(5)