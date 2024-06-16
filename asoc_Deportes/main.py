from models.jugador import Jugador
from models.equipo import Equipo
from models.sede import Sede
from utils.algortimos import quicksort_Algorit, merge_sort

from utils.estadisticas import (equipo_con_mayor_rendimiento, equipo_con_menor_rendimiento,
                                jugador_con_mayor_rendimiento, jugador_con_menor_rendimiento,
                                jugador_mas_joven, jugador_mas_veterano,
                                promedio_edad, promedio_rendimiento,
                                ordenar_equipos_en_sede, ordenar_sedes, ordenar_jugadores_de_todas_las_sedes)

from utils.estadisticas2 import (equipo_con_mayor_rendimiento2, equipo_con_menor_rendimiento2,
                                jugador_con_mayor_rendimiento2, jugador_con_menor_rendimiento2,
                                jugador_mas_joven2, jugador_mas_veterano2,
                                promedio_edad2, promedio_rendimiento2,
                                ordenar_equipos_en_sede2, ordenar_sedes2, ordenar_jugadores_de_todas_las_sedes2)


def leer_datos_desde_archivo(filename):
    jugadores = []
    equipos = {}
    sedes = {}

    with open(filename, "r") as f:
        seccion = None
        for linea in f:
            linea = linea.strip()
            if linea.startswith("#"):
                if "Jugadores" in linea:
                    seccion = "jugadores"
                elif "Equipos" in linea:
                    seccion = "equipos"
                elif "Sedes" in linea:
                    seccion = "sedes"
            elif linea:
                if seccion == "jugadores":
                    identificador, nombre, edad, rendimiento = linea.split(",")
                    jugadores.append(Jugador(int(identificador), nombre, int(edad), int(rendimiento)))
                elif seccion == "equipos":
                    nombre, ciudad, *jugadores_ids = linea.split(",")
                    equipo = Equipo(nombre, ciudad)
                    for jugador_id in jugadores_ids:
                        jugador = next(j for j in jugadores if j.identificador == int(jugador_id))
                        equipo.agregar_jugador(jugador)
                    equipos[nombre] = equipo
                elif seccion == "sedes":
                    ciudad, *equipos_nombres = linea.split(",")
                    sede = Sede(ciudad)
                    for equipo_nombre in equipos_nombres:
                        sede.agregar_equipo(equipos[equipo_nombre])
                    sedes[ciudad] = sede

    return jugadores, list(equipos.values()), list(sedes.values())


def mostrar_resultados(jugadores, equipos, sedes, metodo_nombre):
    print(f"\n--- Resultados usando {metodo_nombre} ---")
    
    # Ordenar sedes
    if metodo_nombre == "merge_sort":
        sedes_ordenadas = ordenar_sedes(sedes)
    else:
        sedes_ordenadas = ordenar_sedes2(sedes)

    print("\nSedes ordenadas:")
    for sede in sedes_ordenadas:
        print(sede)

    # Ordenar equipos en cada sede por rendimiento
    for sede in sedes:
        if metodo_nombre == "merge_sort":
            ordenar_equipos_en_sede(sede)
        else:
            ordenar_equipos_en_sede2(sede)

    print("\nEquipos ordenados en cada sede:")
    for sede in sedes:
        print(f"\nSede: {sede.nombre}, Rendimiento: {sede.rendimiento_promedio():.2f}")
        for equipo in sede.equipos:
            print(f"Equipo: {equipo.deporte}, Rendimiento: {equipo.rendimiento_promedio():.2f}")
            jugadores_equipo = merge_sort(equipo.jugadores, key=lambda j: j.rendimiento) if metodo_nombre == "merge_sort" else quicksort_Algorit(equipo.jugadores, key=lambda j: j.rendimiento)
            ids_jugadores = {jugador.identificador for jugador in jugadores_equipo}
            print(ids_jugadores)

    # Ordenar jugadores por rendimiento
    jugadores_ordenados = merge_sort(jugadores, key=lambda j: (j.rendimiento, -j.edad)) if metodo_nombre == "merge_sort" else quicksort_Algorit(jugadores, key=lambda j: (j.rendimiento, -j.edad))
    jugadores_ids_ordenados = ", ".join(f"{jugador.identificador}" for jugador in jugadores_ordenados)
    print("\nRanking de jugadores por rendimiento:")
    print(f"{{{jugadores_ids_ordenados}}}")

    # Obtener equipo con mayor y menor rendimiento
    todos_equipos = [equipo for sede in sedes for equipo in sede.equipos]
    equipo_mayor_rendimiento = equipo_con_mayor_rendimiento(todos_equipos) if metodo_nombre == "merge_sort" else equipo_con_mayor_rendimiento2(todos_equipos)
    equipo_menor_rendimiento = equipo_con_menor_rendimiento(todos_equipos) if metodo_nombre == "merge_sort" else equipo_con_menor_rendimiento2(todos_equipos)
    print("\nEquipo con mayor rendimiento:", equipo_mayor_rendimiento)
    print("Equipo con menor rendimiento:", equipo_menor_rendimiento)

    # Obtener jugador con mayor y menor rendimiento
    jugador_mayor_rendimiento = jugador_con_mayor_rendimiento(jugadores) if metodo_nombre == "merge_sort" else jugador_con_mayor_rendimiento2(jugadores)
    jugador_menor_rendimiento = jugador_con_menor_rendimiento(jugadores) if metodo_nombre == "merge_sort" else jugador_con_menor_rendimiento2(jugadores)
    print("\nJugador con mayor rendimiento:", jugador_mayor_rendimiento)
    print("Jugador con menor rendimiento:", jugador_menor_rendimiento)

    # Calcular jugador más joven
    joven = jugador_mas_joven(jugadores) if metodo_nombre == "merge_sort" else jugador_mas_joven2(jugadores)
    print(f"\nJugador más joven: {joven}")

    # Calcular jugador más veterano
    veterano = jugador_mas_veterano(jugadores) if metodo_nombre == "merge_sort" else jugador_mas_veterano2(jugadores)
    print(f"Jugador más veterano: {veterano}")

    # Calcular promedio de edad
    edad_promedio = promedio_edad(jugadores) if metodo_nombre == "merge_sort" else promedio_edad2(jugadores)
    print(f"\nPromedio de edad de los jugadores: {edad_promedio:.2f}")

    # Calcular promedio de rendimiento
    rendimiento_promedio = promedio_rendimiento(jugadores) if metodo_nombre == "merge_sort" else promedio_rendimiento2(jugadores)
    print(f"Promedio del rendimiento de los jugadores: {rendimiento_promedio:.2f}")


if __name__ == "__main__":
    jugadores, equipos, sedes = leer_datos_desde_archivo('./datos.txt')
    
    # Resultados usando merge_sort
    mostrar_resultados(jugadores, equipos, sedes, "merge_sort")

    # Resultados usando quick_sort
    mostrar_resultados(jugadores, equipos, sedes, "quick_sort")
