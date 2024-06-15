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
from utils.algortimos import quicksort_Algorit

from utils.estadisticas import (equipo_con_mayor_rendimiento, equipo_con_menor_rendimiento,
                                jugador_con_mayor_rendimiento, jugador_con_menor_rendimiento,
                                jugador_mas_joven, jugador_mas_veterano,
                                promedio_edad, promedio_rendimiento,
                                ordenar_equipos_en_sede, ordenar_sedes, ordenar_jugadores_de_todas_las_sedes)

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




if __name__ == "__main__":
    jugadores, equipos, sedes = leer_datos_desde_archivo('./datos.txt')
    
  
    # Ordenar equipos en cada sede por rendimiento
    for sede in sedes:
        ordenar_equipos_en_sede(sede)

    print("\nEquipos ordenados en cada sede:")
    for sede in sedes:
        print(f"\nSede: {sede.nombre}, Rendimiento: {sede.rendimiento_promedio():.2f}")
        for equipo in sede.equipos:
            print(f"Equipo: {equipo.deporte}, Rendimiento: {equipo.rendimiento_promedio():.2f}")
            jugadores_equipo = quicksort_Algorit(equipo.jugadores, key=lambda j: j.rendimiento) 
            ids_jugadores = {jugador.identificador 
                             for jugador in jugadores_equipo}
            print(ids_jugadores)



        
    # Ordenar jugadores por rendimiento usando quicksort_Algorit
    jugadores_ordenados = quicksort_Algorit(jugadores, key=lambda j: j.rendimiento)
    jugadores_ids_ordenados = ", ".join(f"{jugador.identificador}" for jugador in jugadores_ordenados)
    print("\nRanking de jugadores por rendimiento:")
    print(f"{{{jugadores_ids_ordenados}}}")
   


    # Obtener equipo con mayor y menor rendimiento
    todos_equipos = [equipo for sede in sedes for equipo in sede.equipos]
    equipo_mayor_rendimiento = equipo_con_mayor_rendimiento(todos_equipos)
    equipo_menor_rendimiento = equipo_con_menor_rendimiento(todos_equipos)
    print("\nEquipo con mayor rendimiento:", equipo_mayor_rendimiento)
    print("Equipo con menor rendimiento:", equipo_menor_rendimiento)
    
    # Obtener jugador con mayor y menor rendimiento
    jugador_mayor_rendimiento = jugador_con_mayor_rendimiento(jugadores)
    jugador_menor_rendimiento = jugador_con_menor_rendimiento(jugadores)
    print("\nJugador con mayor rendimiento:", jugador_mayor_rendimiento)
    print("Jugador con menor rendimiento:", jugador_menor_rendimiento)
    
    # Calcular jugador más joven
    joven = jugador_mas_joven(jugadores)
    print(f"\nJugador más joven: {joven}")

    # Calcular jugador más veterano
    veterano = jugador_mas_veterano(jugadores)
    print(f"Jugador más veterano: {veterano}")

    # Calcular promedio de edad
    edad_promedio = promedio_edad(jugadores)
    print(f"\nPromedio de edad de los jugadores: {edad_promedio:.2f}")

    # Calcular promedio de rendimiento
    rendimiento_promedio = promedio_rendimiento(jugadores)
    print(f"Promedio del rendimiento de los jugadores: {rendimiento_promedio:.2f}")
