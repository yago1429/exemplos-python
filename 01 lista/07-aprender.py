import os
os.system("cls")

nivel=int(input("Digite seu nivel de professor (1, 2 ou 3): "))
aulas=int(input("Digite quantas aulas por semana: "))
if nivel==1:
    Salario=12.00 * aulas
    print("Seu salário é de: ", Salario)

elif nivel==2:
    salario=17.00 * aulas
    print("Seu salário é de: ", salario)

elif nivel==3:
    salario= 25.00 * aulas
    print("Seu salário é de: ", salario)
