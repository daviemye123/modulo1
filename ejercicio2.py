anos=int(input("Ingrese el número de años: "))
if anos <= 0:
    print("El número de años no puede ser negativo o tener 0. Por favor, verifique.")
elif anos > 0 and anos < 18:
    print("Usted es menor de edad.")
elif anos >= 18 and anos < 25:
    print("Usted es joven adulto.")
else:
    print("Usted es adulto.")