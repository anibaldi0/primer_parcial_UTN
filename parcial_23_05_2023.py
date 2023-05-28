import json
import re
import csv

def abrir_archivo_json(ruta_archivo: str) -> list:
    '''
    recibe un archivo
    devuelve una lista
    '''
    with open(ruta_archivo, "r") as archivo:
        contenido = json.load(archivo)
    return contenido["jugadores"]

def guardar_archivo_json(ruta_archivo, contenido):
    with open(ruta_archivo, "w") as archivo:
        json.dump(contenido, archivo)

def mostrar_jugador(lista: list) -> list:
    '''
    recibe una lista y devuelve una lista
    recibe un str
    devuelve lista
    '''
    print("\033[93mLos mejores jugadores de la NBA:\033[0m")
    contador = 1
    mensaje = None
    for jugador in lista:
        mensaje = "\033[92m{0}-\033[0m {1} - {2}".format(contador, jugador["nombre"], jugador["posicion"])
        contador += 1
        print(mensaje)
    print(" ")

def mostrar_menu_principal(lista: list) -> None:
    '''
    recibe una lista
    recibe str
    devuelve opcion elejiga
    '''
    print("\n\t\033[96mMenu opciones: \033[0m")
    print("1- Mostrar jugadores ")
    print("2- Seleccione un jugador para ver sus estadisticas: ")
    print("3- Logros del jugador")
    print("4- Mostrar promedio de puntos por partido del Dream Team")


def mostrar_submenu_jugador(lista: list) -> None:
    '''
    recibe una lista
    muestra el menu
    devuelve la opcion elejida
    '''
    respuesta = input("\033[96mElija un jugador por su nombre: \033[0m")
    jugadores_coincidentes = []

    # Construir el patrón regex para buscar palabras con letras faltantes
    patron = r"(?=.*{0}).*{1}".format(respuesta[0], ".*".join(respuesta[1:]))

    # Buscar coincidencias en la lista de jugadores
    for jugador in lista:
        if re.match(patron, jugador["nombre"], re.IGNORECASE):
            jugadores_coincidentes.append(jugador)

    if jugadores_coincidentes:
        # Mostrar los jugadores coincidentes
        print("Jugadores que coinciden con el patrón:")
        for jugador in jugadores_coincidentes:
            print("Nombre: \033[91m{0}\033[0m - Posicion: \033[91m{1}\033[0m".format(jugador["nombre"], jugador["posicion"]))
            # Mostrar el resto de estadísticas, logros, etc.
    else:
        print("No se encontraron jugadores que coincidan con el patrón.")

    if len(jugadores_coincidentes) == 1:
        jugador_seleccionado = jugadores_coincidentes[0]
        print("\nEstadísticas del jugador \033[92m{0}\033[0m:".format(jugador_seleccionado["nombre"]))
        print("Temporadas jugadas: \033[92m{0}\033[0m".format(jugador_seleccionado["estadisticas"]["temporadas"]))
        print("Puntos totales: \033[92m{0}\033[0m".format(jugador_seleccionado["estadisticas"]["puntos_totales"]))
        print("Promedio de puntos por partido: \033[92m{0}\033[0m".format(jugador_seleccionado["estadisticas"]["promedio_puntos_por_partido"]))
        print("Rebotes totales: \033[92m{0}\033[0m".format(jugador_seleccionado["estadisticas"]["rebotes_totales"]))
        print("Promedio de rebotes por partido: \033[92m{0}\033[0m".format(jugador_seleccionado["estadisticas"]["promedio_rebotes_por_partido"]))
        print("Asistencias totales: \033[92m{0}\033[0m".format(jugador_seleccionado["estadisticas"]["asistencias_totales"]))
        print("Promedio de asistencias por partido: \033[92m{0}\033[0m".format(jugador_seleccionado["estadisticas"]["promedio_asistencias_por_partido"]))
        print("Robos totales: \033[92m{0}\033[0m".format(jugador_seleccionado["estadisticas"]["robos_totales"]))
        print("Bloqueos totales: \033[92m{0}\033[0m".format(jugador_seleccionado["estadisticas"]["bloqueos_totales"]))
        print("Porcentaje de tiros de campo: \033[92m{0}\033[0m".format(jugador_seleccionado["estadisticas"]["porcentaje_tiros_de_campo"]))
        print("Porcentaje de tiros libres: \033[92m{0}\033[0m".format(jugador_seleccionado["estadisticas"]["porcentaje_tiros_libres"]))
        print("Porcentaje de tiros triples: \033[92m{0}\033[0m".format(jugador_seleccionado["estadisticas"]["porcentaje_tiros_triples"]))
        pregunta_guardar_estadisticas_txt = input("\033[91mDesea guardar las estadisticas en un archivo CSV?: \033[0m")
        if pregunta_guardar_estadisticas_txt == True:
            guardar_estadisticas_jugador(ruta_archivo="")
        print(" ")
    else:
        print("No hubo coincidencia")

def guardar_estadisticas_jugador(jugador, ruta_archivo):
    # Crear o abrir el archivo CSV en modo de escritura
    with open(ruta_archivo, mode='w', newline='') as archivo_csv:
        # Crear el escritor CSV
        escritor_csv = csv.writer(archivo_csv)

        # Escribir la cabecera del archivo CSV
        escritor_csv.writerow(['Nombre', 'Temporadas', 'Puntos totales', 'Promedio de puntos por partido',
                                'Rebotes totales', 'Promedio de rebotes por partido', 'Asistencias totales',
                                'Promedio de asistencias por partido', 'Robos totales', 'Bloqueos totales',
                                'Porcentaje de tiros de campo', 'Porcentaje de tiros libres',
                                'Porcentaje de tiros triples'])

        # Escribir las estadísticas del jugador
        escritor_csv.writerow([jugador['nombre'], jugador['estadisticas']['temporadas'],
                                jugador['estadisticas']['puntos_totales'],
                                jugador['estadisticas']['promedio_puntos_por_partido'],
                                jugador['estadisticas']['rebotes_totales'],
                                jugador['estadisticas']['promedio_rebotes_por_partido'],
                                jugador['estadisticas']['asistencias_totales'],
                                jugador['estadisticas']['promedio_asistencias_por_partido'],
                                jugador['estadisticas']['robos_totales'],
                                jugador['estadisticas']['bloqueos_totales'],
                                jugador['estadisticas']['porcentaje_tiros_de_campo'],
                                jugador['estadisticas']['porcentaje_tiros_libres'],
                                jugador['estadisticas']['porcentaje_tiros_triples']])
    print("Estadísticas del jugador guardadas en el archivo CSV: {}".format(ruta_archivo))


def ejecutar_opcion(opcion: str, lista_jugadores: list):
    '''
    recibe una opcion en str
    ejecuta la opcion elejida
    '''
    if opcion == "1":
        mostrar_jugador(lista_jugadores)
    elif opcion == "2":
        mostrar_jugador(lista_jugadores)
        mostrar_submenu_jugador(lista_jugadores)  # Pasa la lista de jugadores como argumento
    elif opcion == "3":
        print("Saliendo del programa...")
    else:
        print("Opción inválida.")


# Programa principal
def main():
    lista_jugadores = []
    ruta_archivo = "I:\\workspace_ani\\UTN_Programacion_2023\\Programacion_1\\python\\Programacion_1\\parcial\\dt.json"
    lista_jugadores = abrir_archivo_json(ruta_archivo)
    while True:
        mostrar_menu_principal(lista_jugadores)
        opcion = input("\t\033[96mIngrese la opción deseada:\033[0m ")
        print(" ")
        ejecutar_opcion(opcion, lista_jugadores)
        if opcion == "3":
            break
main()
