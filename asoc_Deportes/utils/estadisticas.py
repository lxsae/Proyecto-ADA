
from utils.algortimos import merge_sort


def estadisticas_equipos(equipos,orden):
    equipos_ordenados = merge_sort(equipos, key=lambda equipo: (equipo.rendimiento_promedio(), -len(equipo.jugadores)))
    if orden == "mayor":
        return equipos_ordenados[-1]
    else:
        return equipos_ordenados[0]

def estadisticas_jugadores(jugadores,orden):
    jugadores_ordenados = merge_sort(jugadores, key=lambda jugador: (jugador.rendimiento, -jugador.edad))
    if orden == "mayor":
        return jugadores_ordenados[-1]
    else:
        return jugadores_ordenados[0]

def jugador_edad(jugadores,orden):
    jugadores_ordenados = merge_sort(jugadores, key=lambda jugador: jugador.edad)
    if orden == "mayor":
        return jugadores_ordenados[-1]
    else:
        return jugadores_ordenados[0]

def promedio_edad(jugadores):
    if jugadores:
        return sum(jugador.edad for jugador in jugadores) / len(jugadores)
    return 0

def promedio_rendimiento(jugadores):
    if jugadores:
        return sum(jugador.rendimiento for jugador in jugadores) / len(jugadores)
    return 0




def ordenar_equipos_en_sede(sede):
    sede.equipos = merge_sort(sede.equipos, key=lambda equipo: (equipo.rendimiento_promedio(), -len(equipo.jugadores)))

def ordenar_sedes(sedes):
    sedes = merge_sort(sedes, key=lambda sede: (sede.rendimiento_promedio(), -sede.total_jugadores()))
    return sedes

