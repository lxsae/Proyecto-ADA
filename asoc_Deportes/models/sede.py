class Sede:
    def __init__(self, nombre):
        self.nombre = nombre
        self.equipos = []

    def agregar_equipo(self, equipo):
        self.equipos.append(equipo)

    def rendimiento_promedio(self):
        if self.equipos:
            return sum(equipo.rendimiento_promedio() for equipo in self.equipos) / len(self.equipos)
        return 0

    def total_jugadores(self):
        return sum(len(equipo.jugadores) for equipo in self.equipos)

    def __repr__(self):
        return f"Sede, {self.nombre},Rendimiento : {self.rendimiento_promedio()}"
