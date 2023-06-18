import os

print()
"""
    Faça uma lista de compras
    O usuário deve ter a possibilidade de 
    inserir, apagar e listar itens na lista
    Não permita que o programa quebre com 
    erros de indices inexixtentes.

"""

lista_compras = []

def mostrar_lista():
    if lista_compras:
        os.system("clear") # limpa o terminal
        print("Lista de Compras:")
        for i, item in enumerate(lista_compras, start=1):
            print(f"{i}. {item}")
    else:
        os.system("clear") # limpa o terminal
        print("A lista de compras está vazia.")
        

def inserir_item():
    item = input("Digite o item a ser adicionado: ")
    lista_compras.append(item)
    print(f"{item} foi adicionado à lista de compras.")
    os.system("clear") # limpa o terminal


def apagar_item():
    mostrar_lista()
    if lista_compras:
        try:
            indice = int(input("Digite o número do item a ser removido: "))
            if 1 <= indice <= len(lista_compras):
                item_removido = lista_compras.pop(indice - 1)
                print(f"{item_removido} foi removido da lista de compras.")
            else:
                print("Número de item inválido.")
        except ValueError:
            print("Entrada inválida. Digite um número válido.")
    else:
        print("A lista de compras está vazia.")

while True:
    print("\nOpções:")
    print("l. Mostrar lista de compras")
    print("i. Inserir item")
    print("a. Apagar item")
    print("s. Sair")
    
    opcao = input("Digite o número da opção desejada: ")
    
    if opcao == "l":
        mostrar_lista()
    elif opcao == "i":
        inserir_item()
    elif opcao == "a":
        apagar_item()
    elif opcao == "s":
        os.system("clear") # limpa o terminal
        print("Programa encerrado...")
        break
    else:
        print("Opção inválida. Digite um número válido.")
