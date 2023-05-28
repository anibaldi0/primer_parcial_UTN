import json
import re
import csv

def abrir_archivo_json(ruta_archivo: str) -> list:
    '''
    Recibe la ruta de un archivo JSON y devuelve una lista de jugadores.
    '''
    with open(ruta_archivo, "r") as archivo:
        contenido_archivo_json = json.load(archivo)
    return contenido_archivo_json["jugadores"]

def guardar_archivo_json(ruta_archivo: str, contenido_archivo_json: dict):
    '''
    Guarda el contenido de un archivo JSON en la ruta especificada.
    '''
    with open(ruta_archivo, "w") as archivo:
        json.dump(contenido_archivo_json, archivo)

def mostrar_jugadores(lista: list) -> None:
    '''
    Muestra los nombres y posiciones de los jugadores en la consola.
    '''
    print("\033[93mLos mejores jugadores de la NBA:\033[0m")
    contador = 1
    for jugador in lista:
        mensaje = "\033[92m{0}-\033[0m {1} - {2}".format(contador, jugador["nombre"], jugador["posicion"])
        contador += 1
        print(mensaje)
    print(" ")

def mostrar_menu_principal(lista: list) -> None:
    '''
    Muestra el menú principal en la consola.
    '''
    print("\n\t\033[96mMenu opciones: \033[0m")
    print("1- Mostrar jugadores")
    print("2- Seleccione un jugador para ver sus estadisticas")
    print("3- Logros del jugador")
    print("4- Mostrar promedio de puntos por partido del Dream Team")

def jugadores_que_coinciden(lista: list, patron: str) -> None:
    '''
    Muestra los jugadores que coinciden con el patrón en la consola.
    '''
    jugadores_coincidentes = [jugador for jugador in lista if re.match(patron, jugador["nombre"], re.IGNORECASE)]
    if jugadores_coincidentes:
        print("Jugadores que coinciden con el patrón:")
        for jugador in jugadores_coincidentes:
            print("Nombre: \033[91m{0}\033[0m - Posicion: \033[91m{1}\033[0m".format(jugador["nombre"], jugador["posicion"]))
    else:
        print("No se encontraron jugadores que coincidan con el patrón.")

def mostrar_estadisticas_jugador(lista: list) -> None:
    '''
    Muestra las estadísticas de un jugador seleccionado.
    '''
    respuesta = input("\033[96mElija un jugador por su nombre: \033[0m")
    patron = r"(?=.*{0}).*{1}".format(respuesta[0], ".*".join(respuesta[1:]))

    jugadores_coincidentes = [jugador for jugador in lista if re.match(patron, jugador["nombre"], re.IGNORECASE)]
    if len(jugadores_coincidentes) == 1:
        jugador_seleccionado = jugadores_coincidentes[0]
        print("\nEstadísticas del jugador \033[92m{0}\033[0m:".format(jugador_seleccionado["nombre"]))
        print("Temporadas jugadas: \033[92m{0}\033[0m".format(jugador_seleccionado["estadisticas"]["temporadas"]))
        print("Puntos totales: \033[92m{0}\033[0m".format(jugador_seleccionado["estadisticas"]["puntos"]))
        print("Asistencias totales: \033[92m{0}\033[0m".format(jugador_seleccionado["estadisticas"]["asistencias"]))
        print("Rebotes totales: \033[92m{0}\033[0m".format(jugador_seleccionado["estadisticas"]["rebotes"]))
    elif len(jugadores_coincidentes) > 1:
        jugadores_que_coinciden(jugadores_coincidentes, patron)
    else:
        print("No se encontraron jugadores que coincidan con el nombre.")

def calcular_promedio_puntos(jugadores: list) -> float:
    '''
    Calcula el promedio de puntos por partido del Dream Team.
    '''
    total_puntos = sum(jugador["estadisticas"]["puntos"] for jugador in jugadores)
    total_partidos = sum(jugador["estadisticas"]["partidos"] for jugador in jugadores)
    promedio_puntos = total_puntos / total_partidos
    return promedio_puntos

def mostrar_promedio_puntos_dream_team(lista: list) -> None:
    '''
    Muestra el promedio de puntos por partido del Dream Team.
    '''
    jugadores_dream_team = [jugador for jugador in lista if jugador["dream_team"]]
    promedio_puntos = calcular_promedio_puntos(jugadores_dream_team)
    print("\nPromedio de puntos por partido del Dream Team: \033[92m{0}\033[0m".format(promedio_puntos))

def guardar_estadisticas_jugador(lista: list, ruta_archivo: str) -> None:
    '''
    Guarda las estadísticas de un jugador en un archivo CSV.
    '''
    respuesta = input("\033[96mElija un jugador por su nombre: \033[0m")
    patron = r"(?=.*{0}).*{1}".format(respuesta[0], ".*".join(respuesta[1:]))

    jugadores_coincidentes = [jugador for jugador in lista if re.match(patron, jugador["nombre"], re.IGNORECASE)]
    if len(jugadores_coincidentes) == 1:
        jugador_seleccionado = jugadores_coincidentes[0]
        nombre_archivo = "{0}.csv".format(jugador_seleccionado["nombre"])
        with open(nombre_archivo, "w", newline="") as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            escritor_csv.writerow(["Temporadas", "Puntos", "Asistencias", "Rebotes"])
            escritor_csv.writerow([
                jugador_seleccionado["estadisticas"]["temporadas"],
                jugador_seleccionado["estadisticas"]["puntos"],
                jugador_seleccionado["estadisticas"]["asistencias"],
                jugador_seleccionado["estadisticas"]["rebotes"]
            ])
        print("Las estadísticas del jugador se han guardado en el archivo CSV.")
    elif len(jugadores_coincidentes) > 1:
        jugadores_que_coinciden(jugadores_coincidentes, patron)
    else:
        print("No se encontraron jugadores que coincidan con el nombre.")

def ejecutar_opcion(opcion: str, lista_jugadores: list) -> None:
    '''
    Ejecuta la opción seleccionada por el usuario en el menú principal.
    '''
    if opcion == "1":
        mostrar_jugadores(lista_jugadores)
    elif opcion == "2":
        mostrar_estadisticas_jugador(lista_jugadores)
    elif opcion == "3":
        guardar_estadisticas_jugador(lista_jugadores, "estadisticas_jugador.csv")
    elif opcion == "4":
        mostrar_promedio_puntos_dream_team(lista_jugadores)
    else:
        print("Opción inválida. Por favor, elija una opción válida.")

def main() -> None:
    '''
    Función principal del programa.
    '''
    ruta_archivo_json = "I:\\workspace_ani\\UTN_Programacion_2023\\Programacion_1\\python\\Programacion_1\\parcial\\primer_parcial_UTN\\dt.json"
    lista_jugadores = abrir_archivo_json(ruta_archivo_json)

    while True:
        mostrar_menu_principal(lista_jugadores)
        opcion = input("\033[96mIngrese una opción: \033[0m")
        if opcion.lower() == "q":
            break
        ejecutar_opcion(opcion, lista_jugadores)

    guardar_archivo_json(ruta_archivo_json, {"jugadores": lista_jugadores})

if __name__ == "__main__":
    main()
