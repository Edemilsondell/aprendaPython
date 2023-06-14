"""
for + range
range --> range(start, stop, step)

"""

print()

stop = input("Digite um número inteiro para defenir o stop: ")
step = input("Digite um número inteiro para defenir o salto: ")

topo = int(stop)
salto = int(step)

lista = [] # lista vazia

number = range(0, topo, salto)

i = 0

for n in number:
    print(n)
    i = n
    lista.append(n)

print("\nLista gerada pelo for range: ",lista)

# função para somar os itens da lista
def soma_lista(lista):
    soma = 0
    for item in lista:
        soma += item
    return soma

numeros = (lista)
resultado = soma_lista(numeros)
print("Metodo de soma 1 = ", resultado)  # Output: 15

# Outra forma  para somar os itens da lista
resultSoma = (lista)
resultado = sum(resultSoma)
print("Metodo de soma 2 = ", resultado)  # Output: 15

# função para multiplicar os itens da lista
def multiplicar_lista(lista):
    produto = 1
    for item in lista:
        if item != 0:
            produto *= item
    return produto

numeros = (lista)
resultMult = multiplicar_lista(numeros)
print("\nResltado da multiplicação = ", resultMult)  # Output: 120
