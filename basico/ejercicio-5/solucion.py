#5.Eliminar una clave
persona = {"nombre": "Juan", "edad": 30, "ciudad": "Buenos Aires"}
del persona["ciudad"]  # o persona.pop("ciudad", None)
print(persona)
