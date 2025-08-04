def adivinar_numero():
    """
    El número secreto está predeterminado. El programa pedirá al usuario ingresar
    un número y dará pistas sobre si es mayor o menor que el número secreto.
    El juego continúa hasta que el usuario adivine.
    usuando un bucle while y dejando numero secreto fuere del bucle.

    No retorna ningún valor. Imprime mensajes en pantalla.
    """
    numero_secreto = 7
    while True:
        numero = int(input("Adivina el número: "))
        if numero < numero_secreto:
            print("El número es menor al secreto, intente de nuevo.")
        elif numero > numero_secreto:
            print("El número es mayor al secreto, intente de nuevo.")
        else:
            print(f"¡Felicidades! El número secreto es {numero_secreto}.")
            break
adivinar_numero()

