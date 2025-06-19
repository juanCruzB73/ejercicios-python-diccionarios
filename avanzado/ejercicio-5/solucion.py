alumnos = {
    "alumno1": {"nombre": "Lucía", "edad": 20, "notas": [9, 8, 10]},
    "alumno2": {"nombre": "Tomás", "edad": 22, "notas": [7, 6, 8]},
}

for clave, datos in alumnos.items():
    print(f"{clave}: {datos}")
