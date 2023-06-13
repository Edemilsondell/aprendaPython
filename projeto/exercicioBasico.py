"""
Faça um programa que peça ao usuário para digitart um número inteiro,
informe se este número é par ou impar.
Caso o usuário não digite um número inteiro, 
informe que não é um número inteiro.

"""
#================================================
""" valor = input("Digite um valor: ")

if valor.isdigit():
    # O valor é um número inteiro
    valor_inteiro = int(valor)
    # Faça algo com o número inteiro, se necessário
    print("O valor é um número inteiro.", valor_inteiro)
else:
    # O valor não é um número inteiro
    # Execute a condição desejada
    print("O valor não é um número inteiro.") """
#===================================================


print()
n_int = input("Por favor, digite um número inteiro:")
print()

if n_int.isdigit():
    inteiro = int(n_int)
    print("O numero digitado foi ", inteiro)
    if inteiro % 2 != 0:
        print(inteiro, " é um numero inteiro.")
        print("O número digitado é impar")
    else:
        print(inteiro, "Este é um numero inteiro.")
        print("O número digitado é par")
else:
    print("O número digitado precisa ser um inteiro.")