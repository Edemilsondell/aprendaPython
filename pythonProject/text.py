print()
import random

qtdM = input("Digite quantos sorteio para Mega:")
mega = int(qtdM)
qtdL = input("Digite quantos sorteio para LotoFácil:")
lotoF = int(qtdL)
qtd_sorteio = 1
while qtd_sorteio <= mega:

    numero = random.randint(1, 60)
    print(qtd_sorteio,"º Sorteio para mega sena.")
    # print("="*37)

    contador = 0


    lista_MegaSena = []  # Lista para armazenar os números sorteados

    for i in range(6):
        sorteio = random.randint(1, 60)
        contador += 1
        resp = sorteio
        lista_MegaSena.append(sorteio)  # Adiciona o número sorteado na lista
        # print("Sorteio Número", contador, "--->>", resp)
        # cont = sorteio

    # print("="*37)
    # print(lista_MegaSena)

    listaM = lista_MegaSena  # Exemplo de lista desordenada
    listaM.sort()  # Ordena a lista em ordem crescente

    # print("Números sorteados Para Mega sena.")
    print(listaM)
    print("="*27)
    # print("Foran sorteadas 6 dezenas. Boa Sorte.")
    print()

    # print("O contador é:", qtd_sorteio)
    qtd_sorteio += 1

print("Foran sorteadas 6 dezenas em cada sorteio. Boa Sorte.")
print("Fim do sorteio da mega sena")
print()
print("/-----/"*8)
print()

###########################################################################
# Sortei da loto fácil

qtd_sorteioL = 1
while qtd_sorteioL <= lotoF:

    lista_LotoFacil = []  # Lista para armazenar os números sorteados

    cont = 0

    # Realizar o sorteio de 5 números aleatórios
    print(qtd_sorteioL,"º Sorteio para LotoFácil.")
    # print("="*37)

    for i in range(15):
        numero = random.randint(1, 25)  # Sorteia um número entre 1 e 100
        cont += 1
        lista_LotoFacil.append(numero)  # Adiciona o número sorteado na lista
        # print("Sorteio Número", cont, "-->>", numero)
        # n = cont

    # Imprimir os números sorteados
    # print("Sorteio para LotoFácil.")

    # print("="*37)

    lista = lista_LotoFacil  # Exemplo de lista desordenada
    lista.sort()  # Ordena a lista em ordem crescente

    # print("Números sorteados para LotoFácil.")
    print(lista)  # Saída: [1, 2, 3, 4, 5]
    print("="*55)
    # print("Foran sorteadas 15 dezenas. Boa Sorte.")
    print()



    # print("O contador é:", qtd_sorteioL)
    qtd_sorteioL += 1

print("Foran sorteadas 15 dezenas em cada sorteio. Boa Sorte.")
print("Fim do sorteio da LotoFácil")
