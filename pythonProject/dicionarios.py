# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#     'nome': 'Edemilson',
#     'sobrenome': 'Da Mata',
#     'idade': 44,
#     'altura': 1.67,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }
# pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')
pessoa = {
    'nome': 'Edemilson',
    'sobrenome': 'Da Mata',
    'idade': 44,
    'altura': 1.67,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ],
}
# print(pessoa, type(pessoa))
print(pessoa['nome'])
print(pessoa['sobrenome'])

print()

for chave in pessoa:
    print(chave, pessoa[chave])

print()

pessoa2 = {}

pessoa2['nome'] = "Ednick"
pessoa2['sobrenome'] = "Damata"
pessoa2['idade'] = "45"

lista = []

print(pessoa2)
print("\n",pessoa2['nome'])
print("",pessoa2['sobrenome'])
print("",pessoa2['idade'])













