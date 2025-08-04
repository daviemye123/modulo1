def peso_ideal():
    """
    Calcula el índice de masa corporal de una persona según su peso y altura.

    Solicita al usuario que ingrese su peso en kg y altura en metros,usando la fórmula: IMC = peso / (altura ** 2).

    No retorna ningún valor ya que lo imprime.
    """
    peso = input("Ingrese su peso en kg: ")
    altura = input("Ingrese su altura en metros: ")

    if peso.replace('.', '', 1).isdigit() and altura.replace('.', '', 1).isdigit():
        peso = float(peso)
        altura = float(altura)

        if peso <= 0 or altura <= 0:
            print("Error: El peso y la altura deben ser mayores que cero.")
            return

        imc = peso / (altura ** 2)
        print(f"Su índice de masa corporal es: {imc:.2f}")
    else:
        print("Entrada inválida. Solo se permiten números positivos.")

# inicia
peso_ideal()









