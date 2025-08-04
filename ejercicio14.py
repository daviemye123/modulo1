"""
Simulación de un cajero automático que permite consultar saldo,
realizar depósitos y retiros con validaciones básicas.
"""

saldo = 1000.0


def consultar_saldo():
    """
    Muestra el saldo actual disponible en la cuenta.
    """
    print(f"Saldo actual: ${saldo:.2f}")


def depositar():
    """
    Solicita al usuario una cantidad a depositar y la suma al saldo.
    Verifica que la cantidad sea positiva.
    """
    global saldo
    try:
        cantidad = float(input("Ingrese la cantidad a depositar: "))
        if cantidad <= 0:
            print("La cantidad debe ser mayor a cero.")
            return
        saldo += cantidad
        print(f"Depósito exitoso. Nuevo saldo: ${saldo:.2f}")
    except ValueError:
        print("Error: ingrese un número válido.")


def retirar():
    """
    Solicita una cantidad a retirar y la descuenta del saldo si hay fondos suficientes.
    Verifica que la cantidad sea válida.
    """
    global saldo
    try:
        cantidad = float(input("Ingrese la cantidad a retirar: "))
        if cantidad <= 0:
            print("La cantidad debe ser mayor a cero.")
            return
        if cantidad > saldo:
            print("Fondos insuficientes.")
            return
        saldo -= cantidad
        print(f"Retiro exitoso. Nuevo saldo: ${saldo:.2f}")
    except ValueError:
        print("Error: ingrese un número válido.")


def mostrar_menu():
    """
    Muestra el menú interactivo del cajero y
    permite al usuario realizar operaciones hasta que decida salir.
    """
    while True:
        print("\nCajero Automático ")
        print("1. Consultar saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            consultar_saldo()
        elif opcion == "2":
            depositar()
        elif opcion == "3":
            retirar()
        elif opcion == "4":
            print("Gracias por usar el cajero. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


mostrar_menu()
