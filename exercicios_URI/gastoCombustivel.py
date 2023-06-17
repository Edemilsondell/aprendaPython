print()

"""
Joaozinho quer calcular e mostrar a quantidade de litros 
de combustível gastos em uma viagem, ao utilizar um 
automóvel que faz 12 KM/L. Para isso, ele gostaria que 
você o auxiliasse através de um simples programa. Para 
efetuar o cálculo, deve-se fornecer o tempo gasto na viagem 
(em horas) e a velocidade média durante a mesma (em km/h). Assim, 
pode-se obter distância percorrida e, em seguida, calcular
quantos litros seriam necessários. Mostre o valor com 3 casas 
decimais após o ponto.
"""
#############################################################

tempo = input("Digite o tempo gasto em horas na viagem:\n")
t = float(tempo)

velocidadeMedia = input("Digite a velocidade Media no percursso:\n")
vlm = float(velocidadeMedia)
consumo = (t * vlm)/12 # Km/L

print(f"O consumo total é {consumo:.2f} litros.")
print(f"{consumo:.2f}\n")

############################################################

# idade em dias
idade_dias = input("Digite a quantidade de dias:\n")

dias = int(idade_dias)
ano = (dias // 365)
resto = (dias % 365)
mes = resto // 30
rd = resto % 30

print()
print(ano, "ano(s)")
print(mes, "mes(es)")
print(rd, "dia(s)")

print()    
print(f"{dias} tem {ano} anos {mes} mes(s) e {rd} dia(s)")


