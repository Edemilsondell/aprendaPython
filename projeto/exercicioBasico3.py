print()

"""
Faça um programa que peça o primeiro nome do usuário.
Se o nome tiver 4 letras ou menos, escreva "Seu nome é curto"
Se o nome tiver entre 5 e 6 letras, escreva "Seu nome é normal"
Se o nome tiver mais que 6 letras, escreva "Seu nome é muito grande"

"""

usuario = input("Por favor, Digite seu primeiro nome.")
print(40*"=")
char = len(usuario)

if char > 1:
    print(f'Seu nome é: {usuario}')
    print("Seu nome possui ", len(usuario), "caracter.")
    if char >0 and char <=4:
        print("Seu nome é curto.")
    elif char >4 and char <=6:
        print("Seu nome é normal.")
    else:
        print("Seu nome é muito grande.")

else:
    print("Por favor, Digite mais de uma letra.")