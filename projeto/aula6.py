# if / elif / else
# se / se não se / se não

number1 = input("Digite o primeiro valor. ")
number2 = input("Digite o segundo valor. ")
number3 = input("Digite o terceiro valor. ")


n1 = int(number1)
n2 = int(number2)
n3 = int(number3)

#print(n1, n2, n3)

if isinstance(n1 and n2 and n3, int):
    print("Esses foram os números digitado: ", n1, n2, n3)
    print(f'A soma dos números é: {n1 + n2 + n3}')
else:
    print("Não é possivel somar.")  

