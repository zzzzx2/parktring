data = [
    [(180, "Airbus A320"), (150, "Boeing 737"), (300, "Boeing 777"), (220, "Airbus A330")],
    [175, 158, 290, 221],
]

def flights_overbooking(data, avion, numero):
    """Comprueba si un avión tiene más pasajeros que asientos."""
    aviones, personas = data
    for i in range(len(aviones)):
        asientos = aviones[i][0]
        tipo = aviones[i][1]
        if tipo == avion:
            if asientos < numero:
                return "Hay Overbooking"
            return "No hay Overbooking"
    return "Avion no encontrado"

def run():
    avion = input("Plane model (e.g. Boeing 737): ")
    numero = int(input("Number of passengers: "))
    print(flights_overbooking(data, avion, numero))

if __name__ == "__main__":
    run()
