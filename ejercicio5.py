numero_secreto=7
while True:
    numero=int(input("Adivina el numero: "))
    if numero < numero_secreto:
        print("El numero es menor al secreto, intente de nuevo.")
    elif numero > numero_secreto:
        print("El numero es mayor al secreto, intente de nuevo.")
    else:
        print(f"Felicidades, el numero secreto es {numero_secreto}.")
        break

