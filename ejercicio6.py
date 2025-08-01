ingresar_cantidad=int(input("Ingresa una cantidad de notas: "))
def suma_notas():
    notas= []
    for i in range(ingresar_cantidad):
        nota = float(input(f"Ingrese la nota {i + 1}: "))
        if nota < 0:
            print("La nota no puede ser negativa. Por favor, verifique.")
            return
        notas.append(nota)


    promedio = sum(notas) / len(notas)
    nota_maxima = max(notas)
    nota_minima = min(notas)
    print(f"el promedio de las notas es: {promedio:.2f},\n la nota máxima es: {nota_maxima},\n la nota mínima es: {nota_minima}")
suma_notas()









