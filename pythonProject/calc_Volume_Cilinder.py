import math

def calcular_volume_cilindro(raio, altura):
    volume = math.pi * raio**2 * altura
    return volume

# Função para validar se o valor inserido é um número
def validar_numero(valor):
    return valor.isdigit()

# Entrada dos valores do raio e altura
raio = input("Digite o valor do raio do cilindro: ")
altura = input("Digite o valor da altura do cilindro: ")

# Validação dos inputs
while not validar_numero(raio) or not validar_numero(altura):
    print("Digite apenas números!")
    raio = input("Digite o valor do raio do cilindro: ")
    altura = input("Digite o valor da altura do cilindro: ")

# Conversão dos inputs para float
raio = float(raio)
altura = float(altura)

valor_pi = math.pi
# Chamada da função para calcular o volume
volume_cilindro = calcular_volume_cilindro(raio, altura)

# Impressão do resultado
print('\n============================')

print(f"O valor de π é: {valor_pi:.5f}")
print("O Raio do cilindro é:", raio)
print("A altura do cilindro é:", altura)
print("O volume do cilindro é:", volume_cilindro)
print(f"O volume do cilindro é: {volume_cilindro:.2f}")
print()
