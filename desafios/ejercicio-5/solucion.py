import string

def contar_palabras_avanzado(texto):
    
    texto = texto.lower()

    for caracter in string.punctuation + "¿¡":
        texto = texto.replace(caracter, "")

    palabras = texto.split()
    
    conteo = {}
    for palabra in palabras:
        conteo[palabra] = conteo.get(palabra, 0) + 1

    return conteo

frase = "¡Hola, mundo! Hola... ¿cómo estás, mundo?"
resultado = contar_palabras_avanzado(frase)
print(resultado)
