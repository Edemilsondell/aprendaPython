print()

"""
Lista em python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
conhecimentos reutilizáveis - indices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +

"""

#..............+01234
#..............-54321
string = "ABCDE" # 5 caracteres
lista1 = []
lista1.append(string)
print(lista1)
print(lista1[0])
# print(lista1[1])
# print(lista1[2])



#print(bool([])) ..#false
# print(lista, type(lista)) #..[] <class 'list'>
#.........0.....1.......2......3....4
#.........-5...-4......-3.....-2....-1
lista = [123, 2, 2, 6, 85, 9, 8, 54, 1.2]

e = 8
qtd = lista.count(e)

# print(lista[2])
# print(lista[-3])
# print(lista[0], type(lista[0]))
# print(lista[1], type(lista[1]))
# print(lista[2], type(lista[2]))
# print(lista[3], type(lista[3]))
# print(lista[4], type(lista[4]))

lista.append(100)
lista.append(10)
# lista.pop()
# lista.append('Fla')
# lista.append('olá')
lista.count(e)
print(qtd)
print(lista)
# lista.pop()
lista.reverse()
print(lista)
lista.sort()
print(lista)
lista.insert(3, 80)
print(lista)

print()

listaB = lista1 + lista
print("\n",listaB)

indices = range(len(listaB))


for indice in indices:
    print(indice, " ==>",listaB[indice], type(listaB[indice]))
print()

for nome in listaB:  
    print(nome,"--->>", type(nome))




