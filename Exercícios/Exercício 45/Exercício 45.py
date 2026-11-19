import time

# Exercício 45 - Sequência de Fibonacci

quantidade = int(input("Digite a quantidade de termos: "))

if quantidade < 2:
    print("A QUANTIDADE DEVE SER MAIOR OU IGUAL A 2")
else:
    primeiro = 0
    segundo = 1

    print(primeiro, segundo, end=" ")

    for contador in range(2, quantidade):
        proximo = primeiro + segundo
        print(proximo, end=" ")

        primeiro = segundo
        segundo = proximo

time.sleep(5)
