import json
import re
import csv
import os

def abrir_archivo_json(ruta_archivo: str) -> list:
    '''
    recibe un archivo
    devuelve una lista
    '''
    with open(ruta_archivo, "r") as archivo:
        contenido_archivo_json = json.load(archivo)
    return contenido_archivo_json["jugadores"]


def guardar_archivo_json(ruta_archivo, contenido_archivo_json):
    with open(ruta_archivo, "w") as archivo:
        json.dump(contenido_archivo_json, archivo)

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

def mostrar_jugador(lista: list) -> list:
    '''
    recibe una lista y devuelve una lista
    recibe un str
    devuelve lista
    '''
    print("\033[93mLos mejores jugadores de la NBA:\033[0m")
    indice = 1
    mensaje = None
    for jugador in lista:
        mensaje = "\033[92m{0}-\033[0m {1} - {2}".format(indice, jugador["nombre"], jugador["posicion"])
        indice += 1
        print(mensaje)
    print(" ")
    return lista

def jugadores_que_coinciden(lista: list) -> list:
    '''
    recibe una lista de jugadores coincidentes
    devuelve lista ordenada en Nombre y Posicion del jugador
    '''
    if lista:
        print("Jugadores que coinciden con el patrón:")
        for jugador in lista:
            print("Nombre: \033[91m{0}\033[0m - Posicion: \033[91m{1}\033[0m".format(jugador["nombre"], jugador["posicion"]))
    else:
        print("No se encontraron jugadores que coincidan con el patrón.")
    return lista

def imprimir_estadistica_de_jugador (jugador_seleccionado: dict) -> list:
    '''
    recibe un diccionario y devuelve una lista con las estadisticas de los jugadores seleccionados
    devuelve una lista ordenada
    '''
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
    while True:
        pregunta_guardar_estadisticas_txt_01 = input("\033[96mDesea guardar las estadisticas en un archivo CSV?: \033[0m Si/No ")
        if pregunta_guardar_estadisticas_txt_01.lower() == "si":
            while True:
                nombre_de_guardado = input("\033[96mCon qué nombre quiere guardar el archivo?: \033[0m ")
                ruta_archivo = "I:\\workspace_ani\\UTN_Programacion_2023\\Programacion_1\\python\\Programacion_1\\parcial\\primer_parcial_UTN\\{0}.csv".format(nombre_de_guardado)
                if archivo_existe(ruta_archivo):
                    respuesta = input("\033[91mYA EXISTE ESE ARCHIVO. Quiere reemplazarlo? Si/No: \033[0m")
                    if respuesta.lower() == "si":
                        guardar_estadisticas_jugador(jugador_seleccionado, ruta_archivo)
                        break
                    elif respuesta.lower() == "no":
                        continue
                else:
                    guardar_estadisticas_jugador(jugador_seleccionado, ruta_archivo)
                    break
        break


def elegir_jugador(lista: list):
    respuesta = input("\033[96mElija un jugador por su nombre: \033[0m")
    jugadores_coincidentes = []
    patron = r"(?=.*{0}).*{1}".format(respuesta[0], ".*".join(respuesta[1:]))
    for jugador in lista:
        if re.match(patron, jugador["nombre"], re.IGNORECASE):
            jugadores_coincidentes.append(jugador)
    return jugadores_coincidentes

def mostrar_estadisticas_jugador(lista: list) -> list:
    '''
    recibe una lista
    muestra el menu
    devuelve una lista con la opcion elegida
    '''
    jugadores_coincidentes = elegir_jugador(lista)

    while True:
        if len(jugadores_coincidentes) == 1:
            jugador_seleccionado = jugadores_coincidentes[0]
            #print("\033[92mlista 01\033[0m", jugadores_coincidentes)
            imprimir_estadistica_de_jugador(jugador_seleccionado)
            print(" ")
            break
        elif len(jugadores_coincidentes) > 1:
            mostrar_jugador(jugadores_coincidentes)
            #print("\033[92mlista 01\033[0m", jugadores_coincidentes)
            #print("\033[92mlista 02\033[0m", jugadores_coincidentes)
            jugadores_coincidentes = elegir_jugador(jugadores_coincidentes)
            if len(jugadores_coincidentes) == 1:
                jugador_seleccionado = jugadores_coincidentes[0]
                #print("\033[92mlista 02\033[0m", jugadores_coincidentes)
                imprimir_estadistica_de_jugador(jugador_seleccionado)
                break
            break
        else:
            print("No hubo coincidencia")
            break

def archivo_existe(ruta_archivo):
    return os.path.exists(ruta_archivo) and os.path.isfile(ruta_archivo)

def guardar_estadisticas_jugador(jugador_seleccionado, ruta_archivo):
    with open(ruta_archivo, 'w') as archivo_csv:
        guardador_csv = csv.writer(archivo_csv)

        guardador_csv.writerow(['Nombre', 'Temporadas', 'Puntos totales', 'Promedio de puntos por partido',
                                'Rebotes totales', 'Promedio de rebotes por partido', 'Asistencias totales',
                                'Promedio de asistencias por partido', 'Robos totales', 'Bloqueos totales',
                                'Porcentaje de tiros de campo', 'Porcentaje de tiros libres',
                                'Porcentaje de tiros triples'])

        guardador_csv.writerow([jugador_seleccionado['nombre'], jugador_seleccionado['estadisticas']['temporadas'],
                                jugador_seleccionado['estadisticas']['puntos_totales'],
                                jugador_seleccionado['estadisticas']['promedio_puntos_por_partido'],
                                jugador_seleccionado['estadisticas']['rebotes_totales'],
                                jugador_seleccionado['estadisticas']['promedio_rebotes_por_partido'],
                                jugador_seleccionado['estadisticas']['asistencias_totales'],
                                jugador_seleccionado['estadisticas']['promedio_asistencias_por_partido'],
                                jugador_seleccionado['estadisticas']['robos_totales'],
                                jugador_seleccionado['estadisticas']['bloqueos_totales'],
                                jugador_seleccionado['estadisticas']['porcentaje_tiros_de_campo'],
                                jugador_seleccionado['estadisticas']['porcentaje_tiros_libres'],
                                jugador_seleccionado['estadisticas']['porcentaje_tiros_triples']])
    print("\n\033[96mArchivo guardado de manera exitosa\033[0m")
    print("\033[96mRuta del archivo:\033[0m\n {0}\n".format(ruta_archivo))


def ejecutar_opcion(opcion: str, lista_jugadores: list):
    '''
    recibe una opcion en str
    ejecuta la opcion elejida
    '''
    if opcion == "1":
        mostrar_jugador(lista_jugadores)
    elif opcion == "2":
        mostrar_jugador(lista_jugadores)
        mostrar_estadisticas_jugador(lista_jugadores)
    elif opcion == "3":
        print("Saliendo del programa...")
    else:
        print("Opción inválida.")


# Programa principal
def main():
    lista_jugadores = []
    ruta_archivo = "I:\\workspace_ani\\UTN_Programacion_2023\\Programacion_1\\python\\Programacion_1\\parcial\\primer_parcial_UTN\\dt.json"
    lista_jugadores = abrir_archivo_json(ruta_archivo)
    while True:
        mostrar_menu_principal(lista_jugadores)
        opcion = input("\t\033[96mIngrese la opción deseada:\033[0m ")
        print(" ")
        ejecutar_opcion(opcion, lista_jugadores)
        if opcion == "3":
            break
main()
