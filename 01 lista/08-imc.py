import os
os.system("cls")
peso=float(input("Digite seu peso: "))
altura=float(input("Digite sua altura:"))
imc= peso / (altura **2)

if imc<=16.9:
    print("Você está muito abaixo do peso, seu imc é", imc)

elif imc>=17 and imc<=18.4:
    print("Você está abaixo do peso, seu imc é: ", imc)

elif imc>=18.5 and imc<=24.9:
    print("Você está com o peso normal, seu imc é: ", imc)

elif imc>=25 and imc<=29.9:
    print("Você está acima do peso, seu imc é: ", imc)

elif imc>=30 and imc<=34.9:
    print("Você está com obesidade grau 1, seu imc é:", imc)


elif imc>=35 and imc<=40:
    print("Você está com obesidade grau 2, seu imc é: ", imc)

else:
    print("Você está com obesidade grau 3, seu imc é: ", imc)
    