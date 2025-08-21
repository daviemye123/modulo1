def comparar_listas(lista1, lista2):
    """
    Recibe dos listas y devuelve una tupla con tres conjuntos:
    Elementos que están en ambas listas.
    Elementos que solo están en la primera lista los separa de la segunda lista.
    """
    set1 = set(lista1)
    set2 = set(lista2)

    en_ambas = set1 & set2
    solo_en_primera = set1 - set2
    solo_en_segunda = set2 - set1

    return (en_ambas, solo_en_primera, solo_en_segunda)


# Parte interactiva
entrada1 = input("Ingresa los elementos de la primera lista separados por coma: ")
entrada2 = input("Ingresa los elementos de la segunda lista separados por coma: ")

lista1 = entrada1.split(",")
lista2 = entrada2.split(",")

resultado = comparar_listas(lista1, lista2)

print("\nElementos en ambas listas:", resultado[0])
print("Solo en la primera lista:", resultado[1])
print("Solo en la segunda lista:", resultado[2])

