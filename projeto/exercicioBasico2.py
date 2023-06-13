"""
Faça um programa que pergunte a hora para o usuário,
baseando-se no horário descrito, exiba a saudação apropriada.
Bom Dia de 0-11, Boa Tarde de 12-17 e Boa Noite de 18-23

"""
from datetime import datetime

print()

horas = input("Por Favor, Você pode me dizer quê horas são? ")
horario_str = int(horas)

print("Sim. São exatamente ", horario_str, "Horas.")

""" horario_obj = datetime.strptime(horario_str, "%H:%M").time()
print("Sim. São exatamente ", horario_obj)
 """
try:
    h = int(horario_str)

    if h >= 0 and h <= 11:
        print("Obrigado, tenha um bom dia.")
    elif h >=12 and h <= 17:
        print("Obrigado, tenha uma boa Tarde.")
    elif h >=18 and h <= 23:
        print("Obrigado, tenha uma boa Noite.")
    else:
        print("Desculpe, Não conheço essa hora..")
except:
        print("Por favor , digite apenas numeros.")
    
