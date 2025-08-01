def frase_vocales_consonantes():
    """
    Esta función cuenta la cantidad de vocales y consonantes en una frase ingresada por el usuario.
    """
frase= input("Introduce una frase: ")

vocales="aeiouáéíóúü"
contador_vocales = 0
contador_consonantes = 0

for i in frase.lower():
    if i in vocales:
        contador_vocales += 1
    elif i.isalpha():
        contador_consonantes += 1
print(f"Cantidad de vocales: {contador_vocales}, cantidad de consonantes: {contador_consonantes}")

