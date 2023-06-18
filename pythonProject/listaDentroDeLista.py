import os
print()
clubes = [
    ['Flamengo', 'Vasco', 'Fluminense', 'Botafogo'],
    ['Corinthians', 'São Palulo', 'Santos', 'Palmeiras'],
    ['Cruzeiro', 'Atlético', 'Grêmio', 'Internacional']
]

# print("Clubes do RJ", clubes[0])
# print("Clubes de SP", clubes[1])
# print("Clubes do MG & RS", clubes[2])
os.system("clear") # limpa o terminal
print("Clubes do RJ")
print(clubes[0][0], clubes[0][1], clubes[0][2], clubes[0][3],"\n")
print("Clubes de SP")
print(clubes[1][0], clubes[1][1], clubes[1][2], clubes[1][3],"\n")
print("Clubes do MG & RS")
print(clubes[2][0], clubes[2][1], clubes[2][2], clubes[2][3],"\n")

for lista_Clubes in clubes:
    print(f'Os Clubes da lista são:\n{lista_Clubes}')
    for clube in lista_Clubes:
        print(clube)
    print()
    