peso=float(input("ingresar peso en kg: "))
altura=float(input("ingresar altura en metros: "))
if peso <= 0 and altura <= 0:
    print("El peso o la altura estan en negatico por favor verificar.")

imc = peso / (altura ** 2)
print(f"su indice de masa corporal es: {imc:.2f}")

def pesoIdeal(peso, altura):
    """
    esta funcion calcula el peso ideal de una persona segun su altura y peso
    Args:
    peso (float): peso en kg
    altura (float): altura en metros

    se raliza la oprecion peso / (altura **2) con la variable imc
    """






