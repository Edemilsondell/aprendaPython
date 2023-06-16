print()

def buscar_palavra(texto, palavra):
    palavras = texto.split()  # Separar as palavras do texto em uma lista
    
    for p in palavras:
        if p == palavra:
            return True  # A palavra foi encontrada
    
    return False  # A palavra não foi encontrada

# Exemplo de uso
texto = ("Este é um exemplo de texto para buscar palavras."
        "O trecho padrão original de Lorem Ipsum, usado desde o"
        "século XVI, está reproduzido abaixo para os interessados."
        "Seções 1.10.32 e 1.10.33 de Finibus Bonorum et Malorum" 
        "de Cicero também foram reproduzidas abaixo em sua forma"
        "exata original, acompanhada das versões para o inglês da"
        "tradução feita por H. Rackham em 1914.")
palavra_desejada = input("Digite a palavra que deseja encontrar:\n\n") #"exemplo"

if buscar_palavra(texto, palavra_desejada):
    print("\nA palavra foi encontrada no texto.\n")
    print("A palavra desejada é",'"'+palavra_desejada+'"',".")
else:
    print("A palavra não foi encontrada no texto.")

####################################################
####################################################

def buscar_palavra_arquivo(nome_arquivo, palavra):
    with open(nome_arquivo, 'r') as arquivo:
        texto = arquivo.read()
        palavras = texto.split()

        for p in palavras:
            if p == palavra:
                return True

    return False
try:
    # Exemplo de uso
    nome_arquivo = input("Digite o nome do arquivo:\n\n") # Nome do arquivo que será lido
    # nome_arquivo = 'Comandos.txt'  # Nome do arquivo que será lido
    palavra_desejada = input("Digite a palavra que deseja encontrar:\n\n") #"exemplo"
    # palavra_desejada = 'install'  # Palavra que será buscada

    if buscar_palavra_arquivo(nome_arquivo, palavra_desejada):
        print("A palavra foi encontrada no arquivo.")
        print("A palavra desejada é",'"'+palavra_desejada+'"',".")
    else:
        print("A palavra não foi encontrada no arquivo.")
except Exception as e:
    
    print("Ocorreu uma exceção:", str(e))