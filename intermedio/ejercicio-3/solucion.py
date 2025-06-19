#8. Buscar una clave
diccionario = {"a": 1, "b": 2, "c": 3}

def existe_clave(dic, clave):
    return clave in dic

print(existe_clave(diccionario, "a"))
print(existe_clave(diccionario, "z"))
