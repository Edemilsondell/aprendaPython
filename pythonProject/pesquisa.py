
""" import os

def buscar_arquivos_por_extensao(diretorio, extensao):
    for root, dirs, files in os.walk(diretorio):
        for file in files:
            if file.endswith(extensao):
                caminho_completo = os.path.join(root, file)
                print("Nome do arquivo:", file)
                print("Caminho completo:", caminho_completo)
                print("--------------------------")

# Exemplo de uso:
diretorio_alvo = "C:"  # Substitua pelo diretório que deseja pesquisar
extensao_alvo = ".psd"
buscar_arquivos_por_extensao(diretorio_alvo, extensao_alvo) """


""" numero =10

if numero > 1:
    if numero > 2:
        if numero > 3:
            print('Número maior que 3')
        else:
            print('Número menor que 3')
    else:
        print('Número menor que 2')
else:
    print('Número menor que 1')    
 """


import math

def calcular_volume_esfera(raio):
    volume = (4/3) * math.pi * raio**3
    return volume

def calcular_volume_cilindro(raioCL, altura):
    volume = math.pi * raioCL**2 * altura
    return volume

print()
raio = float(input("Digite o raio da esfera: "))
raioCL = float(input("Digite o raio do cilindro: "))
altura = float(input("Digite a altura do cilindro: "))

volume_cilindro = calcular_volume_cilindro(raioCL, altura)


print(40*"=")
print("O raio da esféra é ", raio)
print("O raio do cilindro é ", raioCL)
print("A altura do cilindro é ", altura)
print()

print(40*"=")
volume_esfera = calcular_volume_esfera(raio)
print("O volume da esfera é:", volume_esfera)
print("O volume do cilindro é:", volume_cilindro)
print()

print(40*"=")
numero = float(volume_esfera) #3.14159
vlc = float(volume_cilindro) #3.14159
casas_decimais = 4
resultado_formatado = "{:.{}f}".format(numero, casas_decimais)
resultado_formatado2 = "{:.{}f}".format(vlc, casas_decimais)

numero = float(volume_esfera) #1234567890.1234567890
notacao_cientifica = "{:e}".format(numero)
print("Volume Esféra em notação cientifica é", notacao_cientifica)  # Saída: 1.234568e+09


print("Volume Esféra arredondado é", resultado_formatado)  # Saída: 3.14
print("Volume cilindro arredondado é", resultado_formatado2)  # Saída: 3.14
print(40*"=")
print()