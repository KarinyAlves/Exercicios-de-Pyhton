tupla_info = ("Pedrinho", "15", "91506789064")
print(f"Nome, idade e CPF: {tupla_info}\n")

try:
    tupla_info[0] = "Fernanda"
except TypeError as e:
    print(f"Erro: {e}\n")

print("Tentando adicionar:")
try:
    tupla_info.append("Brasileira")
except AttributeError as e:
    print(f"Erro: Tuplas não têm append\n")
