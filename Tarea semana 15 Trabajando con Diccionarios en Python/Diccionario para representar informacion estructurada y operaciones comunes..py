print("Diccionario  informacion personal de Taylor Swift \n")

informacion_personal = {
    "nombre": "Taylor Swift",
    "edad": 36,
    "ciudad": "Huaquillas"
}

# Acceder al valor asociado con la clave "ciudad" y modificarlo
informacion_personal["ciudad"] = "Quito"  # Cambiamos la ciudad a Quito

# Agregar una nueva clave-valor al diccionario que represente la "Profesion"
informacion_personal["Profesion"] = "Cantante"  # Agregamos Profesion

# Verificar si la clave "telefono" existe en el diccionario
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0991510222"  # Si no existe, la agregamos

# Eliminar la clave "edad" del diccionario
if "edad" in informacion_personal:
    del informacion_personal["edad"]  # Eliminamos la clave "edad"

# Imprimir el diccionario final
print(informacion_personal)