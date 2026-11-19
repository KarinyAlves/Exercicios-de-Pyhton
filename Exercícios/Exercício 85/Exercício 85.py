import time

# Exercício 85 - Função de média

def media3(primeira_nota, segunda_nota, terceira_nota):
    media = (primeira_nota + segunda_nota + terceira_nota) / 3
    return media


print("Média:", format(media3(8, 7, 6), ".2f"))
print("Média:", format(media3(10, 9, 8), ".2f"))
print("Média:", format(media3(5.5, 6.5, 7), ".2f"))

time.sleep(5)
