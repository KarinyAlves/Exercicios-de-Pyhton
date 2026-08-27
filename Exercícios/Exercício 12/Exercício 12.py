# Exercício 12 - Custo final da compra

preco_unitario = float(input("Digite o preço unitário do produto R$: "))
quantidade = int(input("Digite a quantidade comprada: "))
frete = float(input("Digite o valor do frete R$: "))

subtotal = preco_unitario * quantidade
total = subtotal + frete

print(f"O valor subtotal é: R$ {subtotal:.2f}")
print(f"O valor total é: R$ {total:.2f}")