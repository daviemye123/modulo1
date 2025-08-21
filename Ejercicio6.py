def suma_notas():
    """
    Solicita al usuario una cantidad de notas, las ingresa
    y calcula el promedio, la nota máxima y la nota mínima.

    La función valida que las notas no sean negativas. Si se detecta una nota inválida,
    se muestra un mensaje de error y se detiene el proceso.

    No retorna ningún valor; imprime los resultados en pantalla.
    """
    try:
        cantidad = int(input("Ingresa una cantidad de notas: "))
        if cantidad <= 0:
            print("La cantidad debe ser mayor a cero.")
            return
    except ValueError:
        print("Error: ingrese un número entero válido.")
        return

    notas = []

    for i in range(cantidad):
        try:
            nota = float(input(f"Ingrese la nota {i + 1}: "))
            if nota < 0:
                print("La nota no puede ser negativa. Por favor, verifique.")
                return
            notas.append(nota)
        except ValueError:
            print("Error: ingrese un número válido.")
            return

    promedio = sum(notas) / len(notas)
    nota_maxima = max(notas)
    nota_minima = min(notas)

    print(f"\nResultados:")
    print(f"- Promedio de las notas: {promedio:.2f}")
    print(f"- Nota máxima: {nota_maxima}")
    print(f"- Nota mínima: {nota_minima}")
suma_notas()









