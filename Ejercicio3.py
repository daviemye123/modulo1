def frase_vocales_consonantes():
    """
    Solicita una frase al usuario y cuenta la cantidad de vocales y consonantes.

    La función convierte la frase a minúsculas, luego analiza cada carácter:
    - Si es una vocal, incrementa el contador de vocales.
    - Si es una letra pero no vocal, se considera consonante.
    Imprime la cantidad total de vocales y consonantes encontradas.

    No devuelve ningún valor; solo imprime el resultado.
    """
    frase = input("Introduce una frase: ")
    vocales = "aeiouáéíóúü"
    contador_vocales = 0
    contador_consonantes = 0

    for caracter in frase.lower():
        if caracter in vocales:
            contador_vocales += 1
        elif caracter:
            contador_consonantes += 1

    print(f"Cantidad de vocales: {contador_vocales}")
    print(f"Cantidad de consonantes: {contador_consonantes}")
# inicia la función
frase_vocales_consonantes()






