datos = {"a": 1, "b": 2, "c": 1, "d": 3}
vistos = set()
resultado = {}

for k, v in datos.items():
    if v in vistos:
        resultado[k] = "duplicado"
    else:
        resultado[k] = v
        vistos.add(v)

print(resultado)
