def buscar_valor(matriz, valor):
    for Fila in range(len(matriz)):
        for Columna in range(len(matriz[Fila])):
            if matriz[Fila][Columna] == valor:
                return print(f" El valor se encontro en la fila- {Fila} columna- {Columna}")  #Retorna la posicion (fila, columna)
    return None  #Retorna None si no se encuentra el valor

#Definimos una matriz 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

#Valor a buscar.
valor_a_buscar = int(input("Introduce el valor a buscar del 1 al 9: "))  #Convertimos a entero

#Llamamos a la funcion de busqueda
resultado = buscar_valor(matriz, valor_a_buscar)
