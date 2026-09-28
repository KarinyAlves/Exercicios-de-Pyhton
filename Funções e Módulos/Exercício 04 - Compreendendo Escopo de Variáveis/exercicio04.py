# Observe atentamente o código em Python abaixo e responda às questões sem executar o programa no computador:
# x = 10 

# def alterar_valor():
    # x = 5 #
    # print(f"Valor dentro da função: {x}")

# alterar_valor()
# print(f"Valor fora da função: {x}")

# a) Qual será a saída exata impressa no console ao executar este código?
# RESPOSTA A: Será 10

# b) Explique por que o valor de x fora da função não é alterado para 5, utilizando o conceito de Escopo de Variáveis (distinção entre escopo local e escopo global).
# Resposta: o escopo local é quando se ccriam variáveis dentro deuma função e apenas ali existem enquanto a função está sendo executada. Quando se trata de varáveis criadas no corpo principais, globais, estas são acessíveis em quaisquer partes.


x = 10
def alterar_valor():
    x = 5
    print(f"Valor dentro da função: {x}")

alterar_valor()
print(f"Valor fora da função: {x}")