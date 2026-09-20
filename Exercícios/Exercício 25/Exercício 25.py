import time

preco = float(input("Digite o preço do produto: "))

opcao = int(input("Digite a opção de pagamento: "))


if preco < 0:
    print("PREÇO INVÁLIDO")

elif opcao == 1:
    valor_final = preco - (preco * 0.10)
    print("Valor final:", valor_final)

elif opcao == 2:
    valor_final = preco - (preco * 0.05)
    print("Valor final:", valor_final)

elif opcao == 3:
    valor_final = preco
    print("Valor final:", valor_final)

elif opcao == 4:
    valor_final = preco + (preco * 0.08)
    print("Valor final:", valor_final)

else:
    print("OPÇÃO INVÁLIDA")

time.sleep(5)