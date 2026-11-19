import time

# Exercício 89 - Validação de nota

def notaValida(nota):
    if nota >= 0 and nota <= 10:
        return True
    else:
        return False


print(notaValida(7.5))
print(notaValida(8))
print(notaValida(10))
print(notaValida(-1))
print(notaValida(10.1))

time.sleep(5)