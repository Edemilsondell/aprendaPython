"""
Iterando strings com while

"""

print()

nome = input("Digite seu Nome; ")

indice = 0
novo_nome = ""
while indice < len(nome):
    print("/", nome[indice])
    letra = nome[indice]
    novo_nome += f'={letra}'
    indice += 1
novo_nome += "="
print()


print(len(nome))
print(nome[2])
print(nome[-1])
print(nome[::-1])
print(novo_nome)