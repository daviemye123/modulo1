def peso_ideal():
    """
    Calcula el índice de masa corporal de una persona según su peso y altura.
    Solicita al usuario que ingrese su peso en kg y altura en metros,usando la fórmula: IMC = peso / (altura ** 2).
    No retorna ningún valor ya que lo imprime.
    """
    try:
        peso = float(input("Ingrese su peso en kg: "))
        altura = float(input("Ingrese su altura en metros: "))
    except ValueError:
        print("Error: Por favor, ingrese un número válido para el peso y la altura.")
        return
    if peso <= 0 or altura <= 0:
        print("El peso y la altura deben ser mayores a cero. Por favor, verifique.")
        return
    imc = peso / (altura ** 2)
    if imc < 18.5:
        print("Bajo de peso")
    elif imc >= 18.5 and imc <= 24.9:
        print("Peso normal")
    elif imc >= 25 and imc <= 29.9:
        print("Sobrepeso")
    elif imc >= 30 and imc <= 34.9:
        print("gordo ")
    elif imc >= 35 and imc <= 39.9:
        print("gordo super II")
    print(f"Su índice de masa corporal (IMC) es: {imc:.2f}")
# Inicia la ejecución
peso_ideal()