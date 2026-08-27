#Exercício 08 - Desconto no produto - Calcule um desconto de 10% e mostre o valor do desconto e o preço final

preço = float(input("Digite o preço original do seu produto e em seguida você obterá o valor com um desconto de 10%: "))

preco_desconto = preço * 0.1

preço_final = preço - preco_desconto

print(f"O preço é R$ {preço}, o desconto é de R$ {preco_desconto}, e o valor final é R$ {preço_final}")