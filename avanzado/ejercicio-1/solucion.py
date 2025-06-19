def contar_frecuencia(cadena):
    frecuencia = {}
    for c in cadena:
        frecuencia[c] = frecuencia.get(c, 0) + 1
    return frecuencia

print(contar_frecuencia("banana"))
