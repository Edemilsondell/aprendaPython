number1 = input(' Digite um número: ')
number2 = input(' Digite outro número: ')

tamanho = input(' Digite uma Palavra: ')

print()

if number1 > number2:
    print(' O primeiro valor é maior que o segundo valor.')
elif number1 == number2:
    print(' Os valores são iguais. ')
else:
    print(' O segundo valor é maior que o primeiro valor.')

if number1 > number2:
    print("", number1, "é maior que ", number2, ".")
elif number1 < number2:
    print("", number1, "é menor que ", number2, ".")
else:

    print("", number1, "é igual ao ", number2, ".")

if 0 and 1:
    print('', True and 1)

if 1 and 1:
    print('', True and 1 and False)

print(" A palavra digitada foi :", tamanho)
print(" A palavra digitada é formada por ",len(tamanho), "caracter.")