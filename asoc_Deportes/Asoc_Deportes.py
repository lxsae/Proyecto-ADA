# PROYECTO FINAL ADA-I 
# Asociación Deportiva
# INTEGRANTES: 
# Ana Sofia Mezu Vargas - 2225958
# Juan Sebastian Miller Molano - 2324115 
# Nicolas Garces Larrahondo - 2180066
# Ivan Alexis Noriega - 2126012

# Clases
class Jugador:
    def __init__(self, identificador, nombre, edad, rendimiento):
        self.identificador = identificador
        self.nombre = nombre
        self.edad = edad
        self.rendimiento = rendimiento

    def __repr__(self):
        return f"{self.identificador}, {self.nombre}, {self.edad}, {self.rendimiento}"

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
        return f"{self.nombre}, Equipos: {len(self.equipos)}, Rendimiento Promedio: {self.rendimiento_promedio()}, Total Jugadores: {self.total_jugadores()}"
