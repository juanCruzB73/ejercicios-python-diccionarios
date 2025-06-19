#13. Diccionario con listas
notas = {
    "Matemática": [7, 8, 9],
    "Historia": [6, 5, 7],
    "Biología": [10, 9, 10]
}

for materia, lista in notas.items():
    promedio = sum(lista) / len(lista)
    print(f"{materia}: promedio = {promedio:.2f}")
