"""
Calculadora com while

"""

print()

while True:
    number_1 = input("Digite um número: ")
    number_2 = input("Digite outro número: ")
    operador = input("Digite um opperador (+-/*): ")

    numeros_validos = None

    n1_float = 0
    n2_float = 0
    try:
        n1_float = float(number_1)
        n2_float = float(number_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print("algum número digitado não é válido. ")
        continue

    operadores_validos = "+-/*"
    # se opredor não estiver entre operadores validos
    if operador not in operadores_validos:
        print("Este operador não é válido. ")
        continue

    if len(operador) > 1:
        print("Digite apenas um operador. ")
        continue

    ###########################################################
    if operador == "+":
        print(f'{ n1_float} + {n2_float } =', n1_float + n2_float)
    elif operador == "-":
        print(f'{ n1_float} - {n2_float } =', n1_float - n2_float)
    elif operador == "*":
        print(f'{ n1_float} * {n2_float } =', n1_float * n2_float)
    elif operador == "/":
        print(f'{ n1_float} / {n2_float } =', n1_float / n2_float)
    ###########################################################



    sair = input("Quer sair? [s]im: ").lower().startswith("s")

    if sair is True:
        break
