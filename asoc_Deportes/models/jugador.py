class Jugador:
    def __init__(self, identificador, nombre, edad, rendimiento):
        self.identificador = identificador
        self.nombre = nombre
        self.edad = edad
        self.rendimiento = rendimiento

    def __repr__(self):
        return f"{self.identificador}, {self.nombre}, {self.edad}, {self.rendimiento}"
