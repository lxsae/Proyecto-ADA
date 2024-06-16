from utils.algortimos import quicksort_Algorit 


def equipo_con_mayor_rendimiento2(equipos):
    return max(equipos, key=lambda equipo: equipo.rendimiento_promedio())

def equipo_con_menor_rendimiento2(equipos):
    return min(equipos, key=lambda equipo: equipo.rendimiento_promedio())

def jugador_con_mayor_rendimiento2(jugadores):
    return max(jugadores, key=lambda jugador: jugador.rendimiento)

def jugador_con_menor_rendimiento2(jugadores):
    return min(jugadores, key=lambda jugador: jugador.rendimiento)

def jugador_mas_joven2(jugadores):
    return min(jugadores, key=lambda jugador: jugador.edad)

def jugador_mas_veterano2(jugadores):
    return max(jugadores, key=lambda jugador: jugador.edad)

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

