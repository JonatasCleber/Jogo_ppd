from random import randint
import os
from time import sleep


while True:
    os.system("clear")
    def espaco():
    	print("\n")
    
    
    def me_apoia():
        print("-"*40)
        print("me apoie no pix, para eu poder trazer scripts com apis")
        print("pix: jonatascleber123@gmail.com")
        print("-"*40)
    me_apoia()
    print("="*30)    
    print("""
    [1] Para Pedra
    [2] Para Papel
    [3] Para Tesoura
    """)
    print("="*30)
    
    espaco()
    jogador = int(input("Pedra, Papel ou Tesoura? "))
    npc = randint(1, 3)
    os.system("clear")
    me_apoia()
    
    espaco()
    if jogador == 1:
        if npc == 1:
            print("Empate! Eu também escolhi pedra.")
        elif npc == 2:
            print("Você jogou pedra e eu joguei papel...")
            print("Ganhei de você.")
        elif npc == 3:
            print("Você jogou pedra e eu joguei tesoura...")
            print("Parabéns! Você ganhou.")
    
    elif jogador == 2:
        if npc == 1:
            print("Você jogou papel e eu joguei pedra...")
            print("Parabéns! Você ganhou.")
        elif npc == 2:
            print("Empate! Eu também escolhi papel.")
        elif npc == 3:
            print("Você jogou papel e eu joguei tesoura...")
            print("Ganhei de você.")
    
    elif jogador == 3:
        if npc == 1:
            print("Você jogou tesoura e eu joguei pedra...")
            print("Ganhei de você.")
        elif npc == 2:
            print("Você jogou tesoura e eu joguei papel...")
            print("Parabéns! Você ganhou.")
        elif npc == 3:
            print("Empate! Eu também escolhi tesoura.")
            
    else:
        print("Opção inválida!")
        continue
    espaco()
    saida = input("Deseja continuar? [S/N]: ").lower()
    if saida == 'n':
        print("Saindo...")
        break
    elif saida == 's':
        continue
os.system("clear")
print("pix: jonatascleber123@gmail.com")
print("Volte sempre!")
