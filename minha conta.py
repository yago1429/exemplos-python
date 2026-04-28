import os
os.system("cls")

def valor_da_conta():
    Valor = float(input("Digite o valor da Conta em R$: "))
    pessoas = (int(input("Digite quantas pessoas será dividido: ")))
    resultado = Valor / pessoas
    print(f"O valor por pessoa é de R$: ", resultado)
print("Seja bem vindo ao App Minha Conta!")

valor_da_conta()