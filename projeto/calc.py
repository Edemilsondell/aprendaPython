import math

def calcular_volume_cilindro(raio, altura):
    volume = math.pi * raio**2 * altura
    return volume

# Exemplo de uso da função
print()
raio = float(input("Digite o raio do cilindro: "))
altura = float(input("Digite a altura do cilindro: "))

print()
print(50*"=")
print("O Raio do cilindro é ", raio, ":")
print("A altura do cilindro é ", altura, ":")

volume_cilindro = calcular_volume_cilindro(raio, altura)
print()
print(50*"=")
print("O volume do cilindro é:", volume_cilindro)
print()
print(50*"=")
volumeC = f'O volume arredondado do cilindro é: {volume_cilindro:.2f}'
print(volumeC)
print()

# Convertendo o resultado em notação cientifica
numero_decimal = volume_cilindro # 123456.789
notacao_cientifica = "{:.2e}".format(numero_decimal)
print("Resultado em notação cientifica: ", notacao_cientifica)
