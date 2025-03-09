
#Iteración sobre arreglos multidimensionales utilizando bucles anidados.
#Registro de Temperaturas Diarias
#Matriz 3d

temperaturas = [
    [   # Huaquillas
        [   # Semana 1
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 25},
            {"day": "Jueves", "temp": 22},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 31},
            {"day": "Domingo", "temp": 27}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 26},
            {"day": "Martes", "temp": 24},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 21},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 32},
            {"day": "Domingo", "temp": 28}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 20},
            {"day": "Martes", "temp": 22},
            {"day": "Miércoles", "temp": 27},
            {"day": "Jueves", "temp": 25},
            {"day": "Viernes", "temp": 31},
            {"day": "Sábado", "temp": 30},
            {"day": "Domingo", "temp": 26}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 19},
            {"day": "Martes", "temp": 23},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 24},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 27}
        ]
    ],
    [   # Arenillas
        [   # Semana 1
            {"day": "Lunes", "temp": 21},
            {"day": "Martes", "temp": 19},
            {"day": "Miércoles", "temp": 24},
            {"day": "Jueves", "temp": 22},
            {"day": "Viernes", "temp": 26},
            {"day": "Sábado", "temp": 30},
            {"day": "Domingo", "temp": 25}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 20},
            {"day": "Martes", "temp": 18},
            {"day": "Miércoles", "temp": 23},
            {"day": "Jueves", "temp": 27},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 31},
            {"day": "Domingo", "temp": 28}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 22},
            {"day": "Martes", "temp": 20},
            {"day": "Miércoles", "temp": 26},
            {"day": "Jueves", "temp": 24},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 27}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 19},
            {"day": "Martes", "temp": 21},
            {"day": "Miércoles", "temp": 25},
            {"day": "Jueves", "temp": 22},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 30},
            {"day": "Domingo", "temp": 26}
        ]
    ],
    [   # Milagro
        [   # Semana 1
            {"day": "Lunes", "temp": 32},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 27},
            {"day": "Sábado", "temp": 26},
            {"day": "Domingo", "temp": 24}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 31},
            {"day": "Martes", "temp": 29},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 27},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 24},
            {"day": "Domingo", "temp": 22}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 28},
            {"day": "Miércoles", "temp": 26},
            {"day": "Jueves", "temp": 25},
            {"day": "Viernes", "temp": 24},
            {"day": "Sábado", "temp": 22},
            {"day": "Domingo", "temp": 20}
        ],
        [   # Semana 4
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

ciudades = ["Huaquillas", "Arenillas", "Milagro"]

# Mostrar las temperaturas por ciudad y semana(practica)
for ciudad_123, ciudad in enumerate(temperaturas):
    print(f"\nTemperaturas en {ciudades[ciudad_123]}:")
    for semana_1234, semana in enumerate(ciudad):
        print(f"  Semana {semana_1234 + 1}:")
        for dia in semana:
            print(f"    {dia['day']}: {dia['temp']} grados")

# Calcular y mostrar el promedio de temperaturas
print("\n Promedio de Temperaturas")
for ciudad_123, ciudad in enumerate(temperaturas):
    for semana_1234, semana in enumerate(ciudad):
        promedio = sum(dia["temp"] for dia in semana) / len(semana)
        print(f"Promedio de temperaturas en {ciudades[ciudad_123]}, Semana {semana_1234 + 1}: {promedio:.2f} grados")