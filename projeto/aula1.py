""" print("\nText!")
print(4*8)
print(744/2)
print(1284+720)
print(25-6)
print("Parabéns.") """

def multiplo_de(numero, multiplo):
    resultado = numero % multiplo == 0
    print(f'{numero} é múltiplo de {multiplo} ?', end=' ')
    print(resultado)
     
     
multiplo_de(16, 8)
multiplo_de(15, 3)
multiplo_de(10, 2)
multiplo_de(72, 3)
