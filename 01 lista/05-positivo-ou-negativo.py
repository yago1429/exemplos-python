import os
os.system("cls")

numero = float(input("digite um número: "))
if numero > 0:
    print("Seu número é positivo")
elif numero < 0:
    print("Seu número é negativo")
else:
    print("Seu número é neutro")