primeiro_valor = float(input("Primeiro valor: "))
segundo_valor = float(input("Segundo valor: "))

if primeiro_valor > segundo_valor:
    print(f"Maior valor: {primeiro_valor}")
elif segundo_valor > primeiro_valor:
    print(f"Maior valor: {segundo_valor}")
else:
    print("VALORES IGUAIS")