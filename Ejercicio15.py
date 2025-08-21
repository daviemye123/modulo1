def calcular_promedio(calificaciones):
    """
    Calcula el promedio de una lista de calificaciones.
    Parámetros:
        calificaciones del diccionario estudiantes (list).
        realiza la suma de las calificaciones y divide por la cantidad de calificaciones.
        suma(calificaciones) / len(calificaciones).
    Retorna:
       devuelgve los valores del promedio de las calificaciones.
       si la lista está vacía, retorna 0.0. con if not.
    """
    if not calificaciones:
        return 0.0
    return sum(calificaciones) / len(calificaciones)
def obtener_estado(promedio):
    """
    Determina el estado del estudiante según su promedio.
    Parámetros:
    Si el promedio es mayor o igual a 3.0, retorna "Aprobado", de lo contrario "Reprobado".

    Retorna:
        str: "Aprobado" si promedio >= 3.0, de lo contrario "Reprobado".
    """
    return "Aprobado" if promedio >= 3.0 else "Reprobado"


def generar_reporte(estudiantes):
    """
    Genera e imprime un reporte de calificaciones para todos los estudiantes.

    Parámetros:
        llama al diccionario con nombres como claves y listas
                            de calificaciones como valores.

    Retorna:
        None: Solo imprime el reporte.
    """
    print("\nReporte de Calificaciones:")
    print("-" * 30)
    for nombre, calificaciones in estudiantes.items():
        promedio = calcular_promedio(calificaciones)
        estado = obtener_estado(promedio)
        print(f"- Estudiante: {nombre}, Promedio: {promedio:.2f}, Estado: {estado}")
    print("-" * 30)
# Diccionario principal de estudiantes y calificaciones
estudiantes = {
    "el rosas": [4.0, 4.5, 5.0],
    "david": [2.5, 3.0, 2.9],
    "carlos": [3.5, 3.8, 4.0],
    "diego": [1.8, 2.0, 2.5],
    "andres": [5.0, 4.8, 4.9]
}
generar_reporte(estudiantes)
