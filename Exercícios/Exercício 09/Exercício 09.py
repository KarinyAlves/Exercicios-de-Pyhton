#Exercicio 9 - Reajuste salarial
#Leia o salário atual ed um funcionário. Calcule um aumento de 15% e mostre o valor do aumento e o novo salário

salarioAtual = float(input("Informe o salário atual do funcionário R$: "))
aumento = salarioAtual * 0.15
novoSalario = salarioAtual + aumento

print(f"o salario atual do funcionário é R$ {salarioAtual}, o valor de aumento é R$ {aumento}, e o novo salário é R$ {novoSalario}")