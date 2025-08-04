def contar_palabras(texto):
    """
    Cuenta la frecuencia de cada palabra en un texto.

    Convierte el texto a minúsculas y separa las palabras por espacios.
    Devuelve un diccionario donde las claves son las palabras y los valores
    son la cantidad de veces que aparecen en el texto.

    Parámetros:
        texto (str): Texto de entrada del cual se contarán las palabras.

    Retorna:
        dict: Diccionario con la frecuencia de cada palabra.
    """
    texto = texto.lower()
    palabras = texto.split()
    frecuencia = {}

    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

    return frecuencia


texto_usuario = input("Ingresa un texto: ")
resultado = contar_palabras(texto_usuario)
print("Frecuencia de palabras:")
print(resultado)

