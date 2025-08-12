def pesoIdeal(edad):
    """
    Calcula un rango estimado de peso ideal basado en la edad.

    Parámetros:
    anos (int): La edad de la persona en años.

    Retorna:
    str: Una recomendación al peso ideal según la edad.
    """
edad=int(input("Ingrese el número de años: "))
if edad <= 0:
    print("El número de años no puede ser negativo o tener 0. Por favor, verifique.")
elif edad > 0 and edad < 18:
    print("Usted es menor de edad.")
elif edad >= 18 and edad < 25:
    print("Usted es joven adulto.")
else:
    print("Usted es adulto.")
pesoIdeal(edad)
