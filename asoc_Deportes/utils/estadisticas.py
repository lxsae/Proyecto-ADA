
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
    if orden == "mayor":
        return maximum(jugadores, key=lambda jugador: jugador.edad)
    else:
        return minimum(jugadores, key=lambda jugador: jugador.edad)

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



def maximum(list, key=lambda x: x):
    if not list:
        return None

    max_value = list[0]
    max_element = list[0]

    for elm in list:
        if key(elm) > key(max_value):
            max_value = elm
            max_element = elm

    return max_element

def minimum(list, key=lambda x: x):
    if not list:
        return None

    min_value = list[0]
    min_element = list[0]

    for elm in list:
        if key(elm) < key(min_value):
            min_value = elm
            min_element = elm

    return min_element

