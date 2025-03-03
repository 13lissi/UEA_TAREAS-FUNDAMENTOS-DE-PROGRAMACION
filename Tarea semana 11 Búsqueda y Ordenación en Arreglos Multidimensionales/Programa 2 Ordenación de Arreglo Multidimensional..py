def bubble_sort(fila):
    # Ordena una fila en orden ascendente usando el algoritmo Bubble Sort.
    numero = len(fila)
    for i in range(numero):
        for j in range(0, numero - i - 1):
            if fila[j] > fila[j + 1]:
                # Intercambiar si el elemento encontrado es mayor que el siguiente
                fila[j], fila[j + 1] = fila[j + 1], fila[j]


def ordenar_fila(matriz, fila_index):
    # Ordena una fila especifica de la matriz.
    if 0 <= fila_index < len(matriz):
        bubble_sort(matriz[fila_index])
    else:
        print("Indice de fila fuera de rango no te emociones.")


# Definimos una matriz 4x4 con valores numéricos
matriz = [
    [9, 2, 5, 15],
    [4, 8, 1, 21],
    [7, 3, 6, 17]
]

# Mostramos la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Solicitar al usuario que elija una fila para ordenar
try:
    fila_a_ordenar = int(input("Introduce el numero de la fila que deseas ordenar (0, 1 o 2): "))

    # Ordenamos la fila específica
    ordenar_fila(matriz, fila_a_ordenar)

    # Mostramos la matriz con la fila ordenada
    print("\nMatriz con la fila ordenada:")
    for fila in matriz:
        print(fila)
# Agregamos para manejar error y para practicar jeje.
except ValueError:
    print("Por favor, introduce un número entero válido.")
except IndexError:
    print("Índice de fila fuera de rango. Debe ser 0, 1 o 2.")
