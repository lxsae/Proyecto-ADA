import timeit

from models.jugador import Jugador
from models.equipo import Equipo
from models.sede import Sede
from utils.algortimos import quicksort_Algorit, merge_sort

from utils.estadisticas import (estadisticas_equipos, estadisticas_jugadores, jugador_edad,
                                promedio_edad, promedio_rendimiento,
                                ordenar_equipos_en_sede, ordenar_sedes)

from utils.estadisticas2 import (estadisticas_equipos2, estadisticas_jugadores2, jugador_edad2,
                                promedio_edad2, promedio_rendimiento2,
                                ordenar_equipos_en_sede2, ordenar_sedes2)


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

    start_time = timeit.default_timer()

    # Ordenar sedes
    if metodo_nombre == "merge_sort":
        start_sedes = timeit.default_timer()
        sedes_ordenadas = ordenar_sedes(sedes)
        end_sedes = timeit.default_timer()
    else:
        start_sedes = timeit.default_timer()
        sedes_ordenadas = ordenar_sedes2(sedes)
        end_sedes = timeit.default_timer()

    print(f"\nTiempo de ejecución para ordenar sedes: {(end_sedes - start_sedes) * 1000:.6f} ms")

    print("\nSedes ordenadas:")
    for sede in sedes_ordenadas:
        print(sede)

    # Ordenar equipos en cada sede por rendimiento
    start_equipos = timeit.default_timer()
    for sede in sedes:
        if metodo_nombre == "merge_sort":
            ordenar_equipos_en_sede(sede)
        else:
            ordenar_equipos_en_sede2(sede)
    end_equipos = timeit.default_timer()
    print(f"\nTiempo de ejecución para ordenar equipos: {(end_equipos - start_equipos) * 1000:.6f} ms")

    print("\nEquipos ordenados en cada sede:")
    for sede in sedes:
        print(f"\nSede: {sede.nombre}, Rendimiento: {sede.rendimiento_promedio():.2f}")
        for equipo in sede.equipos:
            print(f"Equipo: {equipo.deporte}, Rendimiento: {equipo.rendimiento_promedio():.2f}")
            jugadores_equipo = merge_sort(equipo.jugadores, key=lambda j: (j.rendimiento, -j.edad)) if metodo_nombre == "merge_sort" else quicksort_Algorit(equipo.jugadores, key=lambda j: (j.rendimiento, -j.edad))
            jugadores_ids_ordenados = ", ".join(f"{jugador.identificador}" for jugador in jugadores_equipo)
            print(f"{{{jugadores_ids_ordenados}}}")

    # Ordenar jugadores por rendimiento
    start_jugadores = timeit.default_timer()
    jugadores_ordenados = merge_sort(jugadores, key=lambda j: (j.rendimiento, -j.edad)) if metodo_nombre == "merge_sort" else quicksort_Algorit(jugadores, key=lambda j: (j.rendimiento, -j.edad))
    end_jugadores = timeit.default_timer()
    print(f"\nTiempo de ejecución para ordenar jugadores: {(end_jugadores - start_jugadores) * 1000:.6f} ms")

    jugadores_ids_ordenados = ", ".join(f"{jugador.identificador}" for jugador in jugadores_ordenados)
    print("\nRanking de jugadores por rendimiento:")
    print(f"{{{jugadores_ids_ordenados}}}")

    # Obtener equipo con mayor y menor rendimiento
    start_estadisticas_equipos = timeit.default_timer()
    todos_equipos = [equipo for sede in sedes for equipo in sede.equipos]
    equipo_mayor_rendimiento = estadisticas_equipos(todos_equipos, "mayor") if metodo_nombre == "merge_sort" else estadisticas_equipos2(todos_equipos, "mayor")
    equipo_menor_rendimiento = estadisticas_equipos(todos_equipos, "menor") if metodo_nombre == "merge_sort" else estadisticas_equipos2(todos_equipos, "menor")
    end_estadisticas_equipos = timeit.default_timer()
    print(f"\nTiempo de ejecución para obtener estadísticas de equipos: {(end_estadisticas_equipos - start_estadisticas_equipos) * 1000:.6f} ms")

    print("\nEquipo con mayor rendimiento:", equipo_mayor_rendimiento)
    print("Equipo con menor rendimiento:", equipo_menor_rendimiento)

    # Obtener jugador con mayor y menor rendimiento
    start_estadisticas_jugadores = timeit.default_timer()
    jugador_mayor_rendimiento = estadisticas_jugadores(jugadores, "mayor") if metodo_nombre == "merge_sort" else estadisticas_jugadores2(jugadores, "mayor")
    jugador_menor_rendimiento = estadisticas_jugadores(jugadores, "menor") if metodo_nombre == "merge_sort" else estadisticas_jugadores2(jugadores, "menor")
    end_estadisticas_jugadores = timeit.default_timer()
    print(f"\nTiempo de ejecución para obtener estadísticas de jugadores: {(end_estadisticas_jugadores - start_estadisticas_jugadores) * 1000:.6f} ms")

    print("\nJugador con mayor rendimiento:", jugador_mayor_rendimiento)
    print("Jugador con menor rendimiento:", jugador_menor_rendimiento)

    # Calcular jugador más joven
    start_jugador_edad = timeit.default_timer()
    joven = jugador_edad(jugadores, "menor") if metodo_nombre == "merge_sort" else jugador_edad2(jugadores, "menor")
    end_jugador_edad = timeit.default_timer()
    print(f"\nTiempo de ejecución para calcular jugador más joven: {(end_jugador_edad - start_jugador_edad) * 1000:.6f} ms")
    print(f"\nJugador más joven: {joven}")

    # Calcular jugador más veterano
    start_jugador_edad = timeit.default_timer()
    veterano = jugador_edad(jugadores, "mayor") if metodo_nombre == "merge_sort" else jugador_edad2(jugadores, "mayor")
    end_jugador_edad = timeit.default_timer()
    print(f"Tiempo de ejecución para calcular jugador más veterano: {(end_jugador_edad - start_jugador_edad) * 1000:.6f} ms")
    print(f"Jugador más veterano: {veterano}")

    # Calcular promedio de edad
    start_promedio_edad = timeit.default_timer()
    edad_promedio = promedio_edad(jugadores) if metodo_nombre == "merge_sort" else promedio_edad2(jugadores)
    end_promedio_edad = timeit.default_timer()
    print(f"\nTiempo de ejecución para calcular promedio de edad: {(end_promedio_edad - start_promedio_edad) * 1000:.6f} ms")
    print(f"\nPromedio de edad de los jugadores: {edad_promedio:.2f}")

    # Calcular promedio de rendimiento
    rendimiento_promedio = promedio_rendimiento(jugadores) if metodo_nombre == "merge_sort" else promedio_rendimiento2(jugadores)
    print(f"Promedio del rendimiento de los jugadores: {rendimiento_promedio:.2f}")

    end_time = timeit.default_timer()  # Tomar el tiempo de finalización
    tiempo_ejecucion = end_time - start_time

    print(f"\nTiempo de ejecución del algoritmo {metodo_nombre}: {tiempo_ejecucion * 1000:.6f} ms")


if __name__ == "__main__":
    jugadores, equipos, sedes = leer_datos_desde_archivo('./testing/pruebas/datos1.txt')

    # Resultados usando merge_sort
    mostrar_resultados(jugadores, equipos, sedes, "merge_sort")

    # Resultados usando quick_sort
    mostrar_resultados(jugadores, equipos, sedes, "quick_sort")