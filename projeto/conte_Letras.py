"""
Qual é a letra que apareceu mais vezez na busca?

"""

print()

frase = "O Python é uma linguagem de programação " \
    "multiparadoggma. " \
    "O python foi criado por Guido Van rossum ."

# tamanho_str = len(frase)
# print(tamanho_str)

qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ""

i = 0


while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == " ":
        i += 1
        continue
    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(
    "A letra que apareceu mais vezes foi "
    f'"{letra_apareceu_mais_vezes}" que apareceu'
    f' {qtd_apareceu_mais_vezes} x'
)

print("="*30)
    
start = 0
end = 10
while start < end:
    print(start)
    start += 1

print("="*30)

start = 0
end = 10
while start < end:
    start += 1
    print(start)

linhas = 2
colunas = 2
 
print("="*30)

linha = 1
while linha <= linhas:
    coluna = 1
    while coluna <= colunas:
        print(linha, coluna)
        coluna += 1
    linha += 1
