# Calcular o IMC

nome = 'Ednick'
altura = 1.67
peso = 82
imc = peso / (altura ** 2)
result = round(imc, 2)

# f-string
# formatando texto em uma variável
# e imprimindo na tela
ln1 = f'{nome} tem {altura} metros de altura.'
ln2 = f'Pesa {peso} quilos.'
ln3 = f'Seu IMC é {imc:.2f}'

print(ln1)
print(ln2)
print(ln3)

print('==================================')

print("Ednick tem ", altura, "metros de altura.")
print("Pesa ", peso, "quilos.")
#print("Seu IMC é ", imc)
print("Seu IMC é ", result)

