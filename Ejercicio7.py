lista_compras = []


def agregar_item():
    """
    Solicita al usuario un ítem y lo agrega a la lista de compras.
    Muestrando los productos actuales.
    """
    item = input("Ingrese el ítem a agregar: ")
    lista_compras.append(item)
    print(f"Se agregó '{item}' a la lista.")
    print(f"Lista actual: {lista_compras}")


def eliminar_item():
    """
    Muestra los ítems actuales y permite eliminar uno si existe.
    Valida que la lista no esté vacía antes de intentar eliminar.
    """
    if not lista_compras:
        print("No hay ítems en la lista para eliminar.")
        return

    print(f"Ítems actuales: {lista_compras}")
    item = input("Ingrese el ítem a eliminar: ")

    if item in lista_compras:
        lista_compras.remove(item)
        print(f"Se eliminó '{item}' de la lista.")
    else:
        print(f"Error: '{item}' no se encontró en la lista.")


def ver_lista():
    """
    Muestra la lista de compras actual.
    """
    if lista_compras:
        print(f"Lista de compras actual: {lista_compras}")
    else:
        print("La lista de compras está vacía.")


def menu_principal():
    """
    Muestra el menú principal y permite al usuario seleccionar opciones
    hasta que elija salir del programa.
    """
    while True:
        try:
            opcion = int(input(
                "\n1 = Agregar ítem a la lista\n"
                "2 = Eliminar ítem de la lista\n"
                "3 = Ver lista de compras\n"
                "4 = Salir del programa\n"
                "Ingrese una opción: "
            ))
        except ValueError:
            print("Error: ingrese un número válido.")
            continue

        if opcion == 1:
            agregar_item()
        elif opcion == 2:
            eliminar_item()
        elif opcion == 3:
            ver_lista()
        elif opcion == 4:
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
#inicia
menu_principal()


