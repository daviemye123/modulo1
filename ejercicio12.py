factores_conversion = {
    "metro": 1.0,
    "pie": 3.28084,
    "centimetro": 100.0,
    "pulgada": 39.3701,
    "kilometro": 0.001,
    "milla": 0.000621371
}

def convertir(cantidad, unidad_origen, unidad_destino):
    """
    Convierte una cantidad de una unidad a otra  dependiendo de la cantidad a la que se quiera pasar se hara diferente operacion.
    """
    if unidad_origen not in factores_conversion:
        print(f"Error: unidad de origen '{unidad_origen}' no reconocida.")
        return None

    if unidad_destino not in factores_conversion:
        print(f"Error: unidad de destino '{unidad_destino}' no reconocida.")
        return None

    cantidad_en_metros = cantidad / factores_conversion[unidad_origen]
    resultado = cantidad_en_metros * factores_conversion[unidad_destino]
    return resultado


if __name__ == "__main__":
    print("Conversor de unidades (longitud)")
    cantidad = float(input("Ingrese la cantidad: "))
    unidad_origen = input("Unidad de origen: ").lower()
    unidad_destino = input("Unidad de destino: ").lower()

    resultado = convertir(cantidad, unidad_origen, unidad_destino)

    if resultado is not None:
        print(f"{cantidad} {unidad_origen} equivalen a {resultado:.4f} {unidad_destino}")

