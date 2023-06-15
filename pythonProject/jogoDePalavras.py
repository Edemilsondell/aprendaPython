print()

import os

"""
Faça um jogo para o usuário adivinhar qual é a palavra secreta.
Você vai propor uma palavra secreta e vai dar a possibilidade
para o usuário digitar apenas uma letra por vez.
Quando o usuário digitar uma letra, você vai conferir se a 
letra digitada está na palavra secreta.
Se a letra estiver na palavra, exiba a letra:
Se a letra não estiver na palavra, exiba um *:
conte quantas tentativas o usuário precisou para 
acertar a palavra secreta.

"""
palavra_Secreta = "Fla"
letras_acertadas = ""
tentativas = 0

while True:
    letra_digitada = input("Digite uma letra: ")
    tentativas += 1

    if len(letra_digitada) > 1:
        print("Digite apaenas uma letra: ")
        continue
    if letra_digitada in palavra_Secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ""
    for letra_Secreta in palavra_Secreta:
        if letra_Secreta in letras_acertadas:
            palavra_formada += letra_Secreta
            # print(letra_Secreta)
        else:
            palavra_formada += "*"

    print("Palavra Formada: ", palavra_formada)

    if palavra_formada == palavra_Secreta:
        os.system("clear") # limpa o terminal
        print()
        print("Você ganhou! ! Parabéns!")
        print("A palavra era", palavra_Secreta)
        print("Você precisou de  ", tentativas, "tentativas.")

        letras_acertadas = ""
        tentativas = 0
        break
        # sair = "s"
        # continuando = input("Digite [s] sair ou [y] para continuar: ")

        # if continuando != sair:
        #     continue
        # else:
        #     break



