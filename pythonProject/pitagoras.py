import re
import os
import math

print()


# Funçção Para calcular pitágoras
def calcular_pitagoras(cateto1, cateto2):
    hipotenusa = math.sqrt(cateto1**2 + cateto2**2)
    return hipotenusa

###################################################################

# condição que testa se o usuário digitou apenas numeros.
a = input("Digite o Valor do cateto adjascente:")

if re.match(r'^[0-9.]+$', a):
    cateto1 = float(a)
else:
    print("\nPor favor, Digite apenas com números.")
    a = input("Digite o Valor do cateto adjascente:")

b = input("Digite o Valor do cateto oposto:")

if re.match(r'^[0-9.]+$', b):
    cateto2 = float(b)
else:
    print("\nPor favor, Digite apenas com números.")
    b = input("Digite o Valor do cateto oposto:")
#######################################################################

os.system("cls") # Limpa o terminal

cateto1 = float(a)
cateto2 = float(b)

casas_decimais = 2 # variável que define o numero de casas decimais

hipotenusa = calcular_pitagoras(cateto1, cateto2)
adj_formatado = "{:.{}f}".format(cateto1, casas_decimais)
opo_formatado = "{:.{}f}".format(cateto2, casas_decimais)
resultado_formatado = "{:.{}f}".format(hipotenusa, casas_decimais)
# print("A hipotenusa é:", hipotenusa)
print()
print("O cateto adjascente é", adj_formatado)  # Saída: 3.14
print("O cateto oposto é", opo_formatado,)  # Saída: 3.14
print("A hipotenusa é", resultado_formatado, "\n")  # Saída: 3.14



##################################################################
""" valor = input("Digite um valor: ")

if "." in valor:
    try:
        float_valor = float(valor)
        print("O valor digitado é um número float.")
    except ValueError:
        print("O valor digitado não é um número.")
else:
    try:
        int_valor = int(valor)
        print("O valor digitado é um número inteiro.")
    except ValueError:
        print("O valor digitado não é um número.") """

#####################################################
""" valor = input("Digite um valor: ")

if valor.isdigit():
    print("O usuário digitou apenas números.")
else:
    print("O usuário não digitou apenas números.") """

####################################################

