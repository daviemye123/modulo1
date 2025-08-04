"""
Sistema de gestión de inventario para una tienda.
Cada producto se representa como un diccionario con nombre, precio y cantidad.
El inventario completo se almacena en una lista de diccionarios.
"""

inventario = []  


def agregar_producto():
    """
    Solicita al usuario los datos de un nuevo producto y lo agrega al inventario.
    Si el producto ya existe se actualiza su cantidad.
    """
    nombre = input("Ingrese el nombre del producto: ").strip().lower()
    try:
        precio = float(input("Ingrese el precio: "))
        cantidad = int(input("Ingrese la cantidad: "))
    except ValueError:
        print("Error: ingrese un número válido.")
        return

    for producto in inventario:
        if producto["nombre"] == nombre:
            producto["cantidad"] += cantidad
            print("Producto ya existía. Se actualizó la cantidad.")
            return

    nuevo_producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    inventario.append(nuevo_producto)
    print("Producto agregado exitosamente.")


def realizar_venta():
    """
    Solicita el nombre de un producto y la cantidad a vender.
    Si hay suficiente stock, descuenta la cantidad del inventario.
    """
    nombre = input("Ingrese el nombre del producto a vender: ").strip().lower()
    try:
        cantidad = int(input("Ingrese la cantidad a vender: "))
    except ValueError:
        print("Error: cantidad inválida.")
        return

    for producto in inventario:
        if producto["nombre"] == nombre:
            if producto["cantidad"] >= cantidad:
                producto["cantidad"] -= cantidad
                total = cantidad * producto["precio"]
                print(f"Venta realizada. Total: ${total:.2f}")
                return
            else:
                print("Stock insuficiente.")
                return

    print("Producto no encontrado en el inventario.")


def mostrar_inventario():
    """
    Muestra en pantalla todos los productos del inventario con su información.
    """
    if not inventario:
        print("El inventario está vacío.")
        return

    print("\n Inventario Actual ")
    for producto in inventario:
        print(f"Nombre: {producto['nombre'].capitalize()}, "
              f"Precio: ${producto['precio']:.2f}, "
              f"Cantidad: {producto['cantidad']}")


def mostrar_menu():
    """
    Muestra un menú interactivo donde el usuario escoge la opcion.
    """
    while True:
        print("Menú de Inventario")
        print("1. Agregar producto")
        print("2. Realizar venta")
        print("3. Mostrar inventario")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            realizar_venta()
        elif opcion == "3":
            mostrar_inventario()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


mostrar_menu()
