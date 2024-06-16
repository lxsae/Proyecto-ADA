from utils.algortimos import quicksort_Algorit 

def equipo_con_mayor_rendimiento(equipos):
    return max(equipos, key=lambda equipo: equipo.rendimiento_promedio())

def equipo_con_menor_rendimiento(equipos):
    return min(equipos, key=lambda equipo: equipo.rendimiento_promedio())

def jugador_con_mayor_rendimiento(jugadores):
    return max(jugadores, key=lambda jugador: jugador.rendimiento)

def jugador_con_menor_rendimiento(jugadores):
    return min(jugadores, key=lambda jugador: jugador.rendimiento)

def jugador_mas_joven(jugadores):
    return min(jugadores, key=lambda jugador: jugador.edad)

def jugador_mas_veterano(jugadores):
    return max(jugadores, key=lambda jugador: jugador.edad)

def promedio_edad(jugadores):
    if jugadores:
        return sum(jugador.edad for jugador in jugadores) / len(jugadores)
    return 0

def promedio_rendimiento(jugadores):
    if jugadores:
        return sum(jugador.rendimiento for jugador in jugadores) / len(jugadores)
    return 0




def ordenar_equipos_en_sede(sede):
    sede.equipos = quicksort_Algorit(sede.equipos, key=lambda equipo: (equipo.rendimiento_promedio(), -len(equipo.jugadores)))

def ordenar_sedes(sedes):
    sedes = quicksort_Algorit(sedes, key=lambda sede: (sede.rendimiento_promedio(), -sede.total_jugadores()))
    return sedes

def ordenar_jugadores_de_todas_las_sedes(sedes):
    todos_jugadores = [jugador for sede in sedes for equipo in sede.equipos for jugador in equipo.jugadores]
    return quicksort_Algorit(todos_jugadores, key=lambda jugador: (jugador.rendimiento, jugador.edad))