import csv
import json
import os

def cargar_csv(ruta):
    try:
        with open(ruta, mode='r', encoding='utf-8') as archivo_csv:
            lector = csv.DictReader(archivo_csv)
            datos = list(lector)
        print(f" CSV cargado correctamente: {len(datos)} registros encontrados.")
        return datos
    except FileNotFoundError:
        print("Archivo no encontrado. Verifica la ruta.")
        return []
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return []

def exportar_json(datos, ruta_salida):
    try:
        with open(ruta_salida, mode='w', encoding='utf-8') as archivo_json:
            json.dump(datos, archivo_json, indent=4, ensure_ascii=False)
        print(f"Datos exportados a JSON: {ruta_salida}")
    except Exception as e:
        print(f"Error al exportar JSON: {e}")

def menu():
    datos_cargados = []

    while True:
        print("\nMenu de archivos")
        print("1. Cargar archivo CSV")
        print("2. Exportar a JSON")
        print("3. Salir")
        opcion = input("Selecciona una opcion 1-3: ")

        if opcion == '1':
            ruta = input("Ingresa la ruta del archivo CSV: ").strip()
            datos_cargados = cargar_csv(ruta)

        elif opcion == '2':
            if not datos_cargados:
                print("No hay datos cargados. Primero carga un archivo CSV.")
                continue
            salida = input("Ingresa el nombre del archivo JSON: ").strip()
            exportar_json(datos_cargados, salida)

        elif opcion == '3':
            print("Saliendo del programa")
            break

        else:
            print("Opcion no valida. Intenta nuevamente")

if __name__ == '__main__':
    menu()
