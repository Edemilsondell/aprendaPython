print()

"""
    Argumentos nomeados e não nomeados em funções python
    Argumentos nomeado tem nome com sinal de igual
    Argumento não nomeado recebe apenas o argumento (valor)

"""

import math

def calcular_baskara(a, b, c):
    discriminante = b**2 - 4*a*c
    
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
raizes = calcular_baskara(-7, -3, 5)
print(raizes)


def  soma(x, y):
    print(x + y)

soma(10, 5)

def  mult(x, y):
    print(x * y)

mult(10, 5)

def  subtrair(x, y):
    print(x - y)

subtrair(10, 5)
