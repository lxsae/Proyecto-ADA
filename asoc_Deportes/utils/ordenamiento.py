def ordenar_jugadores_por_rendimiento_y_edad(jugadores):
    return sorted(jugadores, key=lambda jugador: (-jugador.rendimiento, jugador.edad))

def ordenar_equipos_por_rendimiento_y_numero_jugadores(equipos):
    return sorted(equipos, key=lambda equipo: (-equipo.rendimiento_promedio(), len(equipo.jugadores)))

def ordenar_sedes_por_rendimiento_y_total_jugadores(sedes):
    return sorted(sedes, key=lambda sede: (-sede.rendimiento_promedio(), -sede.total_jugadores()))
