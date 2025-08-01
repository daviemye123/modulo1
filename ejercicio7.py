agregar=[]
while True:
    opciones = int(input("\n1=Agregar item a la lista\n2=Eliminar item de la lista\n3= ver lista de compras\n4=salir del programa \n Ingrese una opcion: "))

    if opciones < 1 or opciones > 4:
        print("Opción no valida. Intente de nuevo.")
        continue

    elif opciones == 1:
        item = input("Ingrese el item a agregar: ")
        agregar.append(item)
        print(f"Se agregó '{item}' a la lista. Lista actual: {agregar}")

    elif opciones == 2:
        if len(agregar) == 0:
            print("No hay items en la lista para eliminar.")
        else:
            print(f"Items actuales: {agregar}")
            item = input("Ingrese el item a eliminar: ")

            if item in agregar:
                agregar.remove(item)
                print(f"Se eliminó '{item}' de la lista.")
            else:
                print(f"Error: '{item}' no se encontró en la lista.")
    elif opciones == 3:
        print(f"Lista de compras actual: {agregar}")
    elif opciones == 4:
        print("Saliendo del programa. ¡Hasta luego!")
        break


