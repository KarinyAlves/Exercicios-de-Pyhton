import time

# Exercício 55 - Progressão aritmética

primeiro_termo = float(input("Digite o primeiro termo: "))
razao = float(input("Digite a razão: "))
quantidade = int(input("Digite a quantidade de termos: "))

if quantidade <= 0:
    print("QUANTIDADE INVÁLIDA")
else:
    termo = primeiro_termo
    soma = 0

    print("Sequência:", end=" ")

    for contador in range(1, quantidade + 1):
        print(termo, end=" ")
        soma = soma + termo
        termo = termo + razao

    print()
    print("Soma:", soma)

time.sleep(5)