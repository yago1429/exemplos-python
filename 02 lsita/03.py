import os
os.system("cls")
estudo=float(input("Digite quantas horas por dia você estuda: "))

if estudo<=2:
    print("Você estuda pouco")

elif estudo>=2 and estudo<=4:
    print("Você estuda por um tempo médio")

elif estudo>4:
    print("Você estuda muito ")
