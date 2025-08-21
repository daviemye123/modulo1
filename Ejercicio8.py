def verificar_palindromo():
    """
    Solicita al usuario una palabra y verifica si es un palíndromo.
    No retorna ningún valor. Muestra el resultado en pantalla.
    """
    origin = input("Ingrese una palabra u oración: ").lower().strip()
    palabra = origin.replace(" ", "")
    invertido = ""
    for i in range(len(palabra) - 1, -1, -1):
        invertido += palabra[i]
    if invertido == palabra:
        print(f"'{origin}' es un palíndromo.")
    else:
        print(f"'{origin}' no es un palíndromo.")
verificar_palindromo()