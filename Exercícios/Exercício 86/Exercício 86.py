
import time

# Exercício 86 - Função de conversão de temperatura

def celsiusParaFahrenheit(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit


print(celsiusParaFahrenheit(0))
print(celsiusParaFahrenheit(25))
print(celsiusParaFahrenheit(-40))

time.sleep(5)
