print()

texto = "Edemilson"

lisText = []  # Lista vazia
lisText2 = []  # Lista vazia

for letra in texto:
    print(letra)
    lisText.append(letra)  # Adiciona a string "texto" à lista


lisText2.append(texto)  # Adiciona o número 10 à lista

print(lisText)  # Saída: [10, "texto"]
print(lisText2)  # Saída: [10, "texto"]
