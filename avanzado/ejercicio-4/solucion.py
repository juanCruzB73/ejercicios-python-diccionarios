palabras = ["perro", "sol", "gato", "luz", "pez"]
agrupado = {}

for palabra in palabras:
    l = len(palabra)
    agrupado.setdefault(l, []).append(palabra)

print(agrupado)
