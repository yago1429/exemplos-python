import os
os.system("cls")


saldo = 1000.0

while True:

    print("-- Caixa Eletrônico --")


    print("O que você deseja fazer?")

    print("1 -  Ver Saldo")

    print("2 - Depositar")

    print("3 - Sacar")

    print("4 - Sair do sistema")



    opção= input("Digite o que você quer fazer: ")

    if opção == "1":
        print("Seu saldo é de ", saldo)


    elif opção =="2":
        valor_deposito = float(input("Digite o quanto você depositar: "))
        saldo =valor_deposito + saldo

        print("Seu saldo é de ", saldo)


    elif opção =="3":
        valor_saque = float(input("Digite o quanto você quer sacar: "))
        if valor_saque >=1000:
            print("Saldo insuficiente")
        else:
            saldo = valor_saque - saldo

            print("Seu saldo é de ", saldo)


    elif opção =="4":

        print("Saindo do sistema...")
        break

    else:
        print("Opção invalida... Tente de novo.")