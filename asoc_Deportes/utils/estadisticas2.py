from utils.algortimos import quicksort_Algorit 


def estadisticas_equipos2(equipos,orden):
    equipos_ordenados = quicksort_Algorit(equipos, key=lambda equipo: (equipo.rendimiento_promedio(), -len(equipo.jugadores)))
    if orden == "mayor":
        return equipos_ordenados[-1]
    else:
        return equipos_ordenados[0]

def estadisticas_jugadores2(jugadores,orden):
    jugadores_ordenados = quicksort_Algorit(jugadores, key=lambda jugador: (jugador.rendimiento, -jugador.edad))
    if orden == "mayor":
        return jugadores_ordenados[-1]
    else:
        return jugadores_ordenados[0]

def jugador_edad2(jugadores,orden):
    if orden == "mayor":
        return maximum2(jugadores, key=lambda jugador: jugador.edad)
    else:
        return minimum2(jugadores, key=lambda jugador: jugador.edad)


def promedio_edad2(jugadores):
    if jugadores:
        return sum(jugador.edad for jugador in jugadores) / len(jugadores)
    return 0

def promedio_rendimiento2(jugadores):
    if jugadores:
        return sum(jugador.rendimiento for jugador in jugadores) / len(jugadores)
    return 0

def ordenar_equipos_en_sede2(sede):
    sede.equipos = quicksort_Algorit(sede.equipos, key=lambda equipo: (equipo.rendimiento_promedio(), -len(equipo.jugadores)))

def ordenar_sedes2(sedes):
    sedes = quicksort_Algorit(sedes, key=lambda sede: (sede.rendimiento_promedio(), -sede.total_jugadores()))
    return sedes

def maximum2(list, key=lambda x: x):
    if not list:
        return None

    max_value = list[0]
    max_element = list[0]

    for elm in list:
        if key(elm) > key(max_value):
            max_value = elm
            max_element = elm

    return max_element

def minimum2(list, key=lambda x: x):
    if not list:
        return None

    min_value = list[0]
    min_element = list[0]

    for elm in list:
        if key(elm) < key(min_value):
            min_value = elm
            min_element = elm

    return min_element