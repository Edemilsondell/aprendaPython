print()

"""
Tipo tupla - Uma lista imutável

"""

nomes = "Maria", "João", "Paulo" # tupla
print(type(nomes))
listaNome = [] # lista
print(type(listaNome))
listaNome.append('Ednick')
# listaNome.append('Nilson', 'Julia')
# listaNome.append("Maria", "João", "Paulo")
listaNome.append('Ana Carla, Rogério')
listaNome.append('Marcelo')
nomes = list(nomes) # converte tuple em lista
# listaNome = tuple(listaNome) # converte lista em tuple
print(nomes)

print(listaNome)
print()
lista_enumerada = enumerate(listaNome)
print(lista_enumerada)

for iten in lista_enumerada:
    print(iten)