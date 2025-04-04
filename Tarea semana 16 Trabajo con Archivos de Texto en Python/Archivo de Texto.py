print("Escritura de Archivo de Texto\n")

# Abrimos o creamos si no existe, el archivo my_notes.txt en modo escritura ('w')
with open('my_notes.txt', 'w', encoding= "utf-8") as file:
    # Escribimos las lineas en el archivo
    file.write("Taylor Swift, objeto de estudio.\n")
    file.write("La académica considera que enseñar a Swift en las universidades\n")
    file.write("hace que las personas se cuestionen aquello que se considera,\n")
    file.write("o que ellos consideran, como “clásico” u “obra maestra”.\n")

# Lectura de Archivo de Texto

# Abrimos el archivo my_notes.txt en modo lectura ('r')
with open('my_notes.txt', 'r', encoding= "utf-8" ) as file: # Usamos el encoding para que pueda leer comas y ñ
    # Leemos el contenido del archivo línea por línea
    for line in file:
        # Mostramos cada línea leída en la consola
        print(line.strip())  # strip() se usa para eliminar el salto de línea al final

# No es necesario cerrar el archivo manualmente cuando se usa 'with',
# ya que se cierra automáticamente al salir del bloque.