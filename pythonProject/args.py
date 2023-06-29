"""
args - Argumentos não nomeados
*-- *args (Empacotamento e Desempacotamento)

"""

# Lembrete de desempacotamento

x, y, *resto = 1, 2, 3, 4

print(x, y, resto)

def mult(x, y):
    print(x * y)
    
mult(5, 8)

# Exemplo com args

def soma(*args):
    total = 0
    for n in args:
        total += n
    return total
    # print(total)
respSoma = soma(1, 2, 5, 4, 8, 5)
print("A soma total é ", respSoma,'\n')

def multiplica(*args):
    total = 1
    for n in args:
        total *= n
    return total
    # print(total)
resp = multiplica(3, 5, 9, 29, 31)
print("A multiplicação total é ", resp,'\n')



def par_Impar(resp):
    multiplo_de_dois = resp % 2 == 0
    if multiplo_de_dois:
        return f'{resp} é um multiplo de 2.\n'
    return f'{resp} não é um multiplo de 2.\n'
print(par_Impar(resp))


def parImpar():
    if resp % 2 != 0:
        print(resp, "É um número ímpar.")
    else:
        print(resp, "É um número par.")
parImpar()


