import csv
import json
import funciones

# Programa principal
def main():
    lista_jugadores = []
    ruta_archivo = "I:\\workspace_ani\\UTN_Programacion_2023\\Programacion_1\\python\\Programacion_1\\parcial\\primer_parcial_UTN\\dt.json"
    lista_jugadores = funciones.abrir_archivo_json(ruta_archivo)
    while True:
        funciones.mostrar_menu_principal(lista_jugadores)
        opcion = input("\t\033[96mIngrese la opción deseada:\033[0m ")
        print(" ")
        funciones.ejecutar_opcion(opcion, lista_jugadores)
        if opcion == "3":
            break
main()

