import os
os.system ("cls")

while True:

    input("Press <enter> to start")
    print("Started game")


    escolha=input ("Escolha seu inicial:\n Charmander - 1 \n Squirtle - 2 \n Bulbassauro - 3 \n:")

    if escolha == "1":
        print("Você escolheu Charmander")
        meu_pok="Charmander"
    elif escolha == "2":
        print("Você escolheu Squirtle")
        meu_pok="Squirtle"
    else:
        print("Você escolheu bulbassauro")
        meu_pok="Bulbassauro"



    input("Press (enter) para continuar:")
    print("escolha do outro jogador")

    import random

    pokemons = ["Charmander", "Squirtle", "Bulbassauro"]

    escolha_bot = random.choice(pokemons)

    while escolha_bot == meu_pok:
        escolha_bot = random.choice(pokemons)


    print(f"O outro jogador escolheu:", escolha_bot)


    hp_jogador= 100
    hp_bot = 100
    turno= 1

    print(f"Batalha iniciada: {meu_pok} VS {escolha_bot}")

    while hp_jogador > 0 and hp_bot > 0:
        print(f"/n turno {turno} ")
        print(f"Seu HP: {hp_jogador} | HP Rival: {hp_bot}")
        print("-" * 25)

        #seu turno

        print("O que deseja fazer:")
        print("Atacar - 1")
        print("Curar - 2")
        print("fugir - 3")
        acao=input("Escolha a ação: ")
        if acao =="1":
            hp_bot -=10
            print(f"Você escolheu atacar, o {escolha_bot}")

        elif acao =="2":
            hp_jogador +=5
            print("O usou cura, +5 de hp")

        else:
            print("Você fugiu... covarde")
            break


        if hp_bot <= 0:
            print(f"Inimigou desmaiou")
            break


        acao_bot=random.choice(["atacar", "curar", "fugir"])

        if acao_bot =="atacar":
            hp_jogador -=10
            print(f"O rival escolheu atacar, o {meu_pok}")

        elif acao_bot =="curar":
            hp_bot +=5
            print("Rival usou cura, +5 de hp")

        else:
            print("Rival fugiu... covarde")
            break
        turno +=1



    if hp_jogador <= 0:
        print("\n[ DERROTA ] Seu Pokémon desmaiou!")

    elif  hp_bot <= 0:
            print("\n[ VITÓRIA ] Você derrotou o rival!")
    input("\nPressione <enter> para recomeçar")