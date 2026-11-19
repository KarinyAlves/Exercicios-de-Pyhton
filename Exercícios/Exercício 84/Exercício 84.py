import time

# Exercício 84 - Função par ou ímpar

def ehPar(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


print(ehPar(8))
print(ehPar(13))
print(ehPar(0))
print(ehPar(-4))

time.sleep(5)