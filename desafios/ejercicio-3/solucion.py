palabras = ["roma", "amor", "omar", "ramo"]
grupo = {}

for palabra in palabras:
    clave = "".join(sorted(palabra))
    grupo.setdefault(clave, []).append(palabra)

print(grupo)