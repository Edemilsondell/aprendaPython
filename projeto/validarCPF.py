
import random
import re
import sys
print()

# 10  9    8   7    6   5   4    3  2 1
# 9   1    1   9    2   4   3    8  0 4
# 90  9    8   63   12  20  12  24  0 4
# print(2780 % 11)
# print(2380 % 11)
# print(2420 % 11)
# cpf = '91192438043'
# cpf = '83883573019'

""" gerar_cpf = ''
for i in range(9):
    gerar_cpf += str(random.randint(0,9))

print(gerar_cpf)
 """

entrada = input('Digite um CPF: ')
cpf = re.sub(
    r'[^0-9]',
    '',
    entrada
)

dados_repetidos = entrada == entrada[0] * len(entrada)

if dados_repetidos:
    print('Você enviou dados repetidos.')
    print('Processo encerrado.')
    sys.exit()

# print(entrada)
# print(cpf)
# gerando o primeiro digito do cpf
# cpf = '31221773070'
# cpf = gerar_cpf

nove_digitos = cpf[:9]  # percorre os indices até o nono digito
contador_regressivo_1 = 10

resultado_digito_1 = 0

for digito_1 in nove_digitos:
    resultado_digito_1 += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
print("O primeiro digito é ", digito_1)

# gerando o segundo digito do cpf

# cpf = '91192438043'
# cpf = '83883573019'
# cpf = '31221773070'

dez_digitos = cpf[:9] + str(digito_1)# percorre os indices até o décimo digito
# print(cpf)  
contador_regressivo_2 = 11

resultado_digito_2 = 0

for digito_2 in dez_digitos:
    resultado_digito_2 += int(digito_2) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0
print("O segundo digito é ", digito_2)

cpf_gerado = f'{nove_digitos}{digito_1}{digito_2}'

if cpf == cpf_gerado:
    print(f'{entrada} é um CPF válido.')
else:
    print('CPF é inválido.')
