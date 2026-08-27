#Exercicio 10 - Salário com comissão
#Leia o salário fixo de um vendedor e o total vendido no mês. Calcule uma comissão de 4% sobre as vendas e mostre a comissão e o salário total

salarioFixo = float(input("Informe o salário fixo R$: "))
totalVendido = float(input("Informe o total vendido R$: "))

comissao = totalVendido * 0.04
salarioTotal = comissao + salarioFixo

print(f"A comissão corresponde a R$ {comissao} e o salario total corresponde a {salarioTotal}")