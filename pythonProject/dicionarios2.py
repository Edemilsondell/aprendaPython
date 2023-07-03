# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
pessoa = {
    'nome': 'Edemilson',
    'sobrenome': 'Da Mata',
    'idade': 44,
    'peso': 78,
    'altura': 1.67,
}

pessoa.setdefault('idade', 0)
print(pessoa['nome'])
print(pessoa['sobrenome'])
print(pessoa['idade'])
print(pessoa['altura'])
print(pessoa['peso'])
print(len(pessoa))
print(list(pessoa.keys())) # Retorna lista
print(tuple(pessoa.keys())) # Retorna tupla
print(list(pessoa.values()))
print(list(pessoa.items()))

# for valor in pessoa.values():
#     print(valor)

# for chave, valor in pessoa.items():
#     print(chave, valor)