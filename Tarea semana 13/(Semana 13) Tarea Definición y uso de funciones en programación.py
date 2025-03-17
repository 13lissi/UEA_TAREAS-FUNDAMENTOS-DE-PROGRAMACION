import random


def calcular_temperatura_promedio(datos_temperaturas):
    """
    Calcula la temperatura promedio de varias ciudades durante un período de tiempo.

    :param datos_temperaturas: dict, donde las claves son nombres de ciudades y los valores son listas de temperaturas.
    :return: dict, donde las claves son nombres de ciudades y los valores son las temperaturas promedio.
    """
    # Inicializamos un diccionario vacío para almacenar los promedios de cada ciudad
    promedios = {}

    # Iteramos sobre cada ciudad y sus respectivas temperaturas
    for ciudad, temperaturas in datos_temperaturas.items():
        # Verificamos si la lista de temperaturas está vacía
        if len(temperaturas) == 0:
            # Si no hay datos, asignamos None al promedio de esa ciudad
            promedios[ciudad] = None
        else:
            # Calculamos el promedio sumando las temperaturas y dividiendo por la cantidad de temperaturas
            promedio = sum(temperaturas) / len(temperaturas)
            # Almacenamos el promedio en el diccionario con la ciudad como clave
            promedios[ciudad] = promedio

    # Devolvemos el diccionario con los promedios de cada ciudad
    return promedios


# Definimos las ciudades
ciudades = ["Huaquilla", "Guayaquil", "Cuenca"]

# Generamos una matriz 3x3 de temperaturas aleatorias entre 15 y 38 grados
temperaturas_matriz = [[random.randint(15, 38) for _ in range(3)] for _ in range(3)]

# Convertimos la matriz en un diccionario
datos_temperaturas = {
    ciudades[0]: temperaturas_matriz[0],
    ciudades[1]: temperaturas_matriz[1],
    ciudades[2]: temperaturas_matriz[2]
}

# Llamamos a la función y almacenamos los resultados
resultados = calcular_temperatura_promedio(datos_temperaturas)

# Imprimimos la matriz de temperaturas y los resultados
print("Matriz de temperaturas (3x3):")
for fila in temperaturas_matriz:
    print(fila)

print("\nTemperaturas promedio por ciudad:")
print(resultados)