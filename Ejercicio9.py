agenda = {}
def agregar_contacto():
    """
    Solicita al usuario el nombre y número del nuevo contacto.
    Si el nombre ya existe, pregunta si desea sobrescribirlo.
    """
    nombre = input("Ingrese el nombre del contacto: ").strip().capitalize()
    telefono = int(input("Ingrese el número de teléfono: "))

    if nombre in agenda:
        confirmar = input(f"'{nombre}' ya existe. ¿Desea actualizar el número? (s/n): ").lower()
        if confirmar != "s":
            print("Operación cancelada.")
            return

    agenda[nombre] = telefono
    print(f"Contacto '{nombre}' guardado correctamente.")
def buscar_contacto():
    """
    Solicita al usuario el nombre del contacto para buscar y muestra su número de teléfono si existe.
    """
    nombre = input("Ingrese el nombre del contacto a buscar: ").strip().capitalize()
    if nombre in agenda:
        print(f"Teléfono de {nombre}: {agenda[nombre]}")
    else:
        print(f"No se encontró ningún contacto con el nombre '{nombre}'.")
def mostrar_contactos():
    """
    muestra todos los contactos.
    """
    if not agenda:
        print("La agenda está vacía.")
        return
    print("\n Contactos guardados")
    for nombre, telefono in agenda.items():
        print(f"{nombre}: {telefono}")
def menu_agenda():
    """
    Muestra un menú interactivo para que el usuario gestione su agenda.
    pudiedno selecionar entre agregar, buscar, mostrar contactos o salir.
    """
    while True:
        print("\n=== Menú de Agenda ===")
        print("1. Agregar nuevo contacto")
        print("2. Buscar contacto")
        print("3. Mostrar todos los contactos")
        print("4. Salir")
        opcion = input("Seleccione una opción (1-4): ")
        if opcion == "1":
            agregar_contacto()
        elif opcion == "2":
            buscar_contacto()
        elif opcion == "3":
            mostrar_contactos()
        elif opcion == "4":
            print("Saliendo de la agenda.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
menu_agenda()