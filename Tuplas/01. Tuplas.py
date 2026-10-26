#Tuplas em Python

print("="*60)
print("Tuplas em Python")
print("="*60 + "\n")

# Uma tupla é uma sequência de elementos imutáveis, onde uma vez criada, não pode ser alterada.

# Tem de ser ordenada, acessada por índices e pode conter diferentes tipos, além do uso de parênteses

#1. Criando tuplas
print("1. Criando tuplas")

# Tupla vazia
tupla_vazia = ()
print(f"Tupla vazia: {tupla_vazia}")

# Tupla com elementos (necessário o uso de vírgulas)
tupla_um = (42,)
print(f"Tupla com um elemento: {tupla_um}")

#Tupla com vários elementos
tupla_numeros = (1, 2, 3, 4, 5)
print(f"Tupla de números: {tupla_numeros}")

#Tupla com strings
tupla_palavras = ("Python", "é", "incrível")
print(f"Tupla de palavras: {tupla_palavras}")

#Tupla mista
tupla_mista = ("João", "5", "1.5", "True")
print(f"Tupla mista: {tupla_mista}")

#Tupla sem parênteses
tupla_implícita = 1, 2, 3
print(f"Tupla sem parênteses: {tupla_implícita}\n")

print("="*60 + "\n")