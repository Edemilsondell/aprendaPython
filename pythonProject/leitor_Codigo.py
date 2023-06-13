import cv2
from pyzbar import pyzbar

def decode_barcodes(image):
    # Carrega a imagem
    img = cv2.imread(image)

    # Converte a imagem para tons de cinza
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detecta os códigos de barras na imagem
    barcodes = pyzbar.decode(gray)

    # Itera sobre os códigos de barras encontrados
    for barcode in barcodes:
        # Extrai as coordenadas do código de barras
        (x, y, w, h) = barcode.rect

        # Desenha uma caixa ao redor do código de barras
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Decodifica o valor do código de barras
        barcode_data = barcode.data.decode("utf-8")
        barcode_type = barcode.type

        # Exibe o valor do código de barras
        print("Tipo: {}, Valor: {}".format(barcode_type, barcode_data))

    # Exibe a imagem com as caixas ao redor dos códigos de barras
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Caminho para a imagem contendo o código de barras
image_path = "caminho/para/imagem.jpg"

# Chama a função para decodificar os códigos de barras na imagem
decode_barcodes(image_path)
