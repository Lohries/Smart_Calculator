import pytesseract

# Configurar o caminho para o executável do Tesseract
pytesseract.pytesseract.tesseract_cmd = 'tesseract'

# Caminho para a imagem que você deseja processar
imagem_path = 'image_path.png'

# Realizar OCR na imagem
texto_extraido = pytesseract.image_to_string(imagem_path)

# Imprimir o texto extraído da imagem
print(texto_extraido)
