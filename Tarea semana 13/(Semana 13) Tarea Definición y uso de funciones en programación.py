def calcular_promedio_por_semana_y_total(temperaturas):
    # Inicializa listas para almacenar los promedios semanales y totales
    promedios_semanales = []
    promedios_totales = []

    # Recorre cada ciudad en la lista de temperaturas
    for ciudad in temperaturas:
        # Inicializa una lista para almacenar los promedios semanales de la ciudad
        promedios_ciudad = []
        suma_total = 0  # Variable para acumular la suma total de temperaturas
        total_dias = 0   # Variable para contar el total de días

        # Recorre cada semana de la ciudad
        for semana in ciudad:
            # Suma las temperaturas de cada día en la semana
            suma_temperaturas = sum(dia["temp"] for dia in semana)
            # Calcula el promedio de la semana
            promedio_semana = suma_temperaturas / len(semana) if len(semana) > 0 else 0
            # Agrega el promedio semanal a la lista de promedios de la ciudad
            promedios_ciudad.append(promedio_semana)
            # Acumula la suma total de temperaturas
            suma_total += suma_temperaturas
            # Acumula el total de días
            total_dias += len(semana)

        # Calcula el promedio total de la ciudad
        promedio_total = suma_total / total_dias if total_dias > 0 else 0
        # Agrega la lista de promedios semanales a la lista de promedios semanales de todas las ciudades
        promedios_semanales.append(promedios_ciudad)
        # Agrega el promedio total de la ciudad a la lista de promedios totales
        promedios_totales.append(promedio_total)

    # Devuelve las listas de promedios semanales y promedios totales
    return promedios_semanales, promedios_totales


# Datos de temperaturas
temperaturas = [
    [  # Huaquillas
        [  # Semana 1
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 25},
            {"day": "Jueves", "temp": 22},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 31},
            {"day": "Domingo", "temp": 27}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 26},
            {"day": "Martes", "temp": 24},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 21},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 32},
            {"day": "Domingo", "temp": 28}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 20},
            {"day": "Martes", "temp": 22},
            {"day": "Miércoles", "temp": 27},
            {"day": "Jueves", "temp": 25},
            {"day": "Viernes", "temp": 31},
            {"day": "Sábado", "temp": 30},
            {"day": "Domingo", "temp": 26}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 19},
            {"day": "Martes", "temp": 23},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 24},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 27}
        ]
    ],
    [  # Arenillas
        [  # Semana 1
            {"day": "Lunes", "temp": 21},
            {"day": "Martes", "temp": 19},
            {"day": "Miércoles", "temp": 24},
            {"day": "Jueves", "temp": 22},
            {"day": "Viernes", "temp": 26},
            {"day": "Sábado", "temp": 30},
            {"day": "Domingo", "temp": 25}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 20},
            {"day": "Martes", "temp": 18},
            {"day": "Miércoles", "temp": 23},
            {"day": "Jueves", "temp": 27},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 31},
            {"day": "Domingo", "temp": 28}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 22},
            {"day": "Martes", "temp": 20},
            {"day": "Miércoles", "temp": 26},
            {"day": "Jueves", "temp": 24},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 27}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 19},
            {"day": "Martes", "temp": 21},
            {"day": "Miércoles", "temp": 25},
            {"day": "Jueves", "temp": 22},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 30},
            {"day": "Domingo", "temp": 26}
        ]
    ],
    [  # Milagro
        [  # Semana 1
            {"day": "Lunes", "temp": 32},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 27},
            {"day": "Sábado", "temp": 26},
            {"day": "Domingo", "temp": 24}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 31},
            {"day": "Martes", "temp": 29},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 27},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 24},
            {"day": "Domingo", "temp": 22}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 28},
            {"day": "Miércoles", "temp": 26},
            {"day": "Jueves", "temp": 25},
            {"day": "Viernes", "temp": 24},
            {"day": "Sábado", "temp": 22},
            {"day": "Domingo", "temp": 20}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 27},
            {"day": "Miércoles", "temp": 25},
            {"day": "Jueves", "temp": 24},
            {"day": "Viernes", "temp": 22},
            {"day": "Sábado", "temp": 21},
            {"day": "Domingo", "temp": 20}
        ]
    ]
]

# Calcular promedios por semana y total
promedios_semanales, promedios_totales = calcular_promedio_por_semana_y_total(temperaturas)

# Mostrar resultados
ciudades = ["Huaquillas", "Arenillas", "Milagro"]
for i, ciudad in enumerate(ciudades):
    print(f"Promedios semanales de {ciudad}:")
    for semana_num, promedio in enumerate(promedios_semanales[i], start=1):
        print(f"  Semana {semana_num}: {promedio:.2f} °C")
    print(f"Promedio total de {ciudad}: {promedios_totales[i]:.2f} °C\n")