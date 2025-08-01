origin =input(str("Ingrese una palabra u oracion")).lower()
palabra = origin.replace(" ", "")

invertido = ""
for i in range(len(palabra) - 1, -1, -1):
    invertido = invertido + palabra[i]

if invertido == palabra:
    print(f"{origin} es un palíndromo")
else:
    print(f"{origin} no es un palíndromo")
