def mostrar_tabla_multiplicar():
    """
    Solicita al usuario un número y muestra su tabla de multiplicar del 1 al 10.

    La función utiliza un bucle while para multiplicar el número ingresado
    por los valores del 1 al 10 e imprime los resultados en formato tabla.

    No retorna ningún valor, solo muestra los resultados en pantalla.
    """
    try:
        tabla = int(input("Ingrese el número de la tabla que desea: "))
        contador = 0
        while contador < 10:
            contador += 1
            resultado = tabla * contador
            print(f"{tabla} x {contador} = {resultado}")
    except ValueError:
        print("Error: ingrese un número entero válido.")
#inicia
mostrar_tabla_multiplicar()





