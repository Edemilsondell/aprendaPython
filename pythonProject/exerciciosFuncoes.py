# Exercicios
# Crie funções que duplicam, triplicão e quadruplicam
# O número recebido com parametro

########################################################

""" def duplicar(numero):
    return numero * 2

def triplicar(numero):
    return numero * 3

def quaduplicar(numero):
    return numero * 4

def quintuplicar(numero):
    return numero * 5


namber1 = input("Por favor, Digite um número inteiro.")

n1 = int(namber1)
# duplicar(n1)
# duplicado = duplicar(n1)
# print(duplicado)

print(duplicar(n1))
print(triplicar(n1))
print(quaduplicar(n1))
print(quintuplicar(n1)) """

#############################################################

# Função para criar outras funções

def criar_muitiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

namber2 = input("Por favor, Digite um número inteiro.")
n2 = int(namber2)

mult = input("Quer multiplicar por quanto?.")
mult1 = int(mult)

multAleatorio = criar_muitiplicador(mult1)
duplicar = criar_muitiplicador(2)
triplicar = criar_muitiplicador(3)
quaduplicar = criar_muitiplicador(4)
quintuplicar = criar_muitiplicador(5)

print(multAleatorio(n2))
print(duplicar(n2))
print(triplicar(n2))
print(quaduplicar(n2))
print(quintuplicar(n2)) 