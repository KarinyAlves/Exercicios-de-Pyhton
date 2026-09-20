import time

lado_um = float(input("Digite o primeiro lado: "))

lado_dois = float(input("Digite o segundo lado: "))

lado_tres = float(input("Digite o terceiro lado: "))


if lado_um <= 0 or lado_dois <= 0 or lado_tres <= 0:
    print("MEDIDA INVÁLIDA")

elif lado_um < lado_dois + lado_tres and lado_dois < lado_um + lado_tres and lado_tres < lado_um + lado_dois:
    print("FORMAM")

else:
    print("NÃO FORMAM")
    
time.sleep(5)