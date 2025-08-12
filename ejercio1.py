def peso_ideal():
    """
    Calcula el índice de masa corporal de una persona según su peso y altura.

    Solicita al usuario que ingrese su peso en kg y altura en metros,usando la fórmula: IMC = peso / (altura ** 2).

    No retorna ningún valor ya que lo imprime.
    """
    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: "))
    if peso <= 0 or altura <= 0:
        print("El peso y la altura deben ser mayores a cero. Por favor, verifique.")
        return
    imc=peso / (altura ** 2)
    print(f"Su índice de masa corporal (IMC) es: {imc:.2f}")
# inicia
peso_ideal()









