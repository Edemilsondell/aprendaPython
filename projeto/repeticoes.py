print()

"""
Repetições
While (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim.

"""

# Operadores de Atribuição
# = += *= /= //= **= %=
cont = 0

while cont < 5:
    cont += 1 
    print(cont, " ======= Vamos lá")
print("Fim.")

qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=} {coluna=}')
        coluna += 1
    linha += 1

print("Fim.")