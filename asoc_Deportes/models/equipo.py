class Equipo:
    def __init__(self, deporte, sede):
        self.deporte = deporte
        self.sede = sede
        self.jugadores = []

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)

    def rendimiento_promedio(self):
        if self.jugadores:
            return sum(jugador.rendimiento for jugador in self.jugadores) / len(self.jugadores)
        return 0

    def __repr__(self):
        return f"{self.deporte}, {self.sede}, Jugadores: {len(self.jugadores)}, Rendimiento Promedio: {self.rendimiento_promedio()}"
