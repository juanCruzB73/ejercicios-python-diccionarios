puntajes = {"Ana": 80, "Luis": 95, "Carla": 87}
ganador = max(puntajes, key=puntajes.get)
print(f"Ganador: {ganador} con {puntajes[ganador]} puntos")
