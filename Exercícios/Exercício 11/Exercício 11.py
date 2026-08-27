# Exercício 11 - Troca de valores

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))

auxiliar = a
a = b
b = auxiliar

print("\nDepois da troca:")
print(f"A: {a}")
print(f"B: {b}")