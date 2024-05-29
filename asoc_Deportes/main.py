# PROYECTO FINAL ADA-I 
# Asociación Deportiva
# INTEGRANTES: 
# Ana Sofia Mezu Vargas - 2225958
# Juan Sebastian Miller Molano - 2324115 
# Nicolas Garces Larrahondo - 2180066
# Ivan Alexis Noriega - 2126012


from models.jugador import Jugador
from models.equipo import Equipo
from models.sede import Sede

from utils.estadisticas import (equipo_con_mayor_rendimiento, equipo_con_menor_rendimiento,
                                jugador_con_mayor_rendimiento, jugador_con_menor_rendimiento,
                                jugador_mas_joven, jugador_mas_veterano,
                                promedio_edad, promedio_rendimiento,
                                ordenar_equipos_en_sede, ordenar_sedes, ordenar_jugadores_de_todas_las_sedes)

if __name__ == "__main__":
    # Crear jugadores
    jugadores = [
        Jugador(10, "Daniel Ruiz", 17, 60),
        Jugador(5, "Martina Martinez", 30, 50),
        Jugador(3, "Ana Lopez", 20, 70),
        Jugador(1, "Carlos Perez", 26, 61)
    ]

    # Crear equipos y agregar jugadores
    equipo1 = Equipo("Futbol", "Cali")
    equipo1.agregar_jugador(jugadores[0])
    equipo1.agregar_jugador(jugadores[1])

    equipo2 = Equipo("Baloncesto", "Cali")
    equipo2.agregar_jugador(jugadores[2])
    equipo2.agregar_jugador(jugadores[3])

    equipo3 = Equipo("Voleibol", "Medellin")
    equipo3.agregar_jugador(Jugador(4, "Lucas Martinez", 22, 65))
    equipo3.agregar_jugador(Jugador(6, "Maria Fernanda", 28, 55))

    # Crear sedes y agregar equipos
    sede1 = Sede("Cali")
    sede1.agregar_equipo(equipo1)
    sede1.agregar_equipo(equipo2)

    sede2 = Sede("Medellin")
    sede2.agregar_equipo(equipo3)

    # Listado de sedes
    sedes = [sede1, sede2]

    # Ordenar equipos en cada sede
    for sede in sedes:
        ordenar_equipos_en_sede(sede)

    print("Equipos ordenados en cada sede:")
    for sede in sedes:
        print(sede)
        for equipo in sede.equipos:
            print(equipo)

    # Ordenar sedes
    sedes_ordenadas = ordenar_sedes(sedes)
    print("\nSedes ordenadas:")
    for sede in sedes_ordenadas:
        print(sede)

    # Ordenar todos los jugadores de todas las sedes por rendimiento
    jugadores_ordenados = ordenar_jugadores_de_todas_las_sedes(sedes)
    print("\nJugadores ordenados por rendimiento:")
    for jugador in jugadores_ordenados:
        print(jugador)

    # Obtener equipo con mayor y menor rendimiento
    todos_equipos = [equipo for sede in sedes for equipo in sede.equipos]
    equipo_mayor_rendimiento = equipo_con_mayor_rendimiento(todos_equipos)
    equipo_menor_rendimiento = equipo_con_menor_rendimiento(todos_equipos)
    print("Equipo con mayor rendimiento:", equipo_mayor_rendimiento)
    print("Equipo con menor rendimiento:", equipo_menor_rendimiento)
    
    # Obtener jugador con mayor y menor rendimiento
    jugador_mayor_rendimiento = jugador_con_mayor_rendimiento(jugadores)
    jugador_menor_rendimiento = jugador_con_menor_rendimiento(jugadores)
    print("Jugador con mayor rendimiento:", jugador_mayor_rendimiento)
    print("Jugador con menor rendimiento:", jugador_menor_rendimiento)
    
    # Calcular jugador más joven
    joven = jugador_mas_joven(jugadores)
    print(f"Jugador más joven: {joven}")

    # Calcular jugador más veterano
    veterano = jugador_mas_veterano(jugadores)
    print(f"Jugador más veterano: {veterano}")

    # Calcular promedio de edad
    edad_promedio = promedio_edad(jugadores)
    print(f"Promedio de edad de los jugadores: {edad_promedio:.2f}")

    # Calcular promedio de rendimiento
    rendimiento_promedio = promedio_rendimiento(jugadores)
    print(f"Promedio del rendimiento de los jugadores: {rendimiento_promedio:.2f}")
