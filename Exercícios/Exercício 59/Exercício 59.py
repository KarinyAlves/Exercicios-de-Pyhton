import time

# Exercício 59 - Senha até acertar

senha_correta = "1234"
tentativas = 0

senha = input("Digite a senha: ")
tentativas = tentativas + 1

while senha != senha_correta:
    print("Senha incorreta.")
    senha = input("Digite a senha: ")
    tentativas = tentativas + 1

print("ACESSO LIBERADO")
print("Tentativas:", tentativas)

time.sleep(5)
