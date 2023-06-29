print()

"""
    Argumentos nomeados e não nomeados em funções python
    Argumentos nomeado tem nome com sinal de igual
    Argumento não nomeado recebe apenas o argumento (valor)

"""

import math

a = input("Digite um numero para A:")
b = input("Digite um numero para B:")
c = input("Digite um numero para C:")

ax = int(a)
bx = int(b)
cx = int(c)

def calcular_baskara(a, b, c):
    discriminante = b**2 - 4*a*c
    print("\nDelta = ", discriminante)
    
    if discriminante > 0:
        raiz1 = (-b + math.sqrt(discriminante)) / (2*a)
        raiz2 = (-b - math.sqrt(discriminante)) / (2*a)
        return raiz1, raiz2
    elif discriminante == 0:
        raiz = -b / (2*a)
        return raiz
    else:
        return "Não existem raízes reais."

# Exemplo de uso da função
# raizes = calcular_baskara(-7, 3, 5)
# calcular_baskara(ax, bx, cx)
raizes = calcular_baskara(ax, bx, cx)
print(raizes)

# def  soma(x, y):
#     print(x + y)

# soma(10, 5)

# def  mult(x, y):
#     print(x * y)

# mult(10, 5)

# def  subtrair(x, y):
#     print(x - y)

# subtrair(10, 5)
