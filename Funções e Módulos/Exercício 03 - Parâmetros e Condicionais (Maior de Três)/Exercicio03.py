def encontrar_maior(a, b, c):
    return max (a,b,c)

primeiro = int(input("Digite o primeiro numero: "))
segundo = int(input("Digite o primeiro numero: "))
terceiro = int(input("Digite o primeiro numero: "))

resultado = encontrar_maior (primeiro, segundo, terceiro)

print(f"O maior número é: {resultado}, e os números são {primeiro}, {segundo} e {terceiro}")