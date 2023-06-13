"""
Exercicio
Peça ao usuário para digitar seu nome.
Peça ao usuário para digitar sua idade.
Se nome e idade for digitado:
....Exiba:
........Seu nome é {nome}
........Sua idade é {idade}
........Seu nome invertido é {nome invertido}
........Seu nome contém (ou não) espaços
........Seu nome tem {n} letras
........A primeira letra do seu nome é {letra}
........A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
....exiba "Desculpe, você deixou campos vazios."
"""

nome = input("Digite seu nome:")
idade = input("Digite sua idade:")

if nome and idade:

    print(30*"=")
    print("Seu nome é ", nome)
    print("Sua idade é ", idade)
    print("Seu nome possui ", len(nome), "caracter.")
    print(30*"=")
    print(nome[0:len(nome):1])
    print()
    print("A prmeira letra do seu nome é ", nome[0])
    print("A última letra do seu nome é ", nome[-1])
    print("Seu nome invertido é ", nome[-1::-1])
    print(30*"=")
    print(nome[0:len(nome):1])

    if ' ' in nome:
        print("Seu nome contém espaço.")
    else:
        print("Seu nome não contém espaço.")

    print("Seu nome invertido é ", nome[::-1])
    print("Meu nome é:", nome[0:])
    print("Minha idade é:", idade)
    print(f'A ultima letra do meu nome é: {nome[-1]}')

else:
    print("Você não prencheu todos os campos:")