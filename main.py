from mostrar_estadisticas import *
from menu import *
import csv 


def agregar_pais(paises):
    try:
        nombre = input("Ingrese el nombre del pais: ").strip().capitalize()
        if not nombre:
            print("Error: El nombre no puede estar vacío.")
            return
# Verificar si ya existe (búsqueda exacta)
        if any(p['nombre'].lower() == nombre.lower() for p in paises):
            print("Error: El pais ya existe. Use la opción 2 para actualizarlo.")
            return
#Input de poblacion
        poblacion_input = input("Ingrese la poblacion del pais: ").strip()
        if not poblacion_input.isdigit():
            print("Error: La poblacion debe ser un número entero positivo.")
            return
        poblacion = int(poblacion_input)
        if poblacion <= 0:
            print("Error: La poblacion debe ser mayor a cero.")
            return
#input de superficie
        superficie_input = input("Ingrese la superficie del pais (km²): ").strip()
        if not superficie_input.isdigit():
            print("Error: La superficie debe ser un número entero positivo.")
            return
        superficie = int(superficie_input)
        if superficie <= 0:
            print("Error: La superficie debe ser mayor a cero.")
            return
#input de continente
        continente = input("Ingrese el continente del pais: ").strip().capitalize()
        if not continente:
            print("Error: El continente no puede estar vacío.")
            return

# Escribir en CSV
        with open('paises.csv', 'a', newline='', encoding='utf-8') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow([nombre, poblacion, superficie, continente])

        # Agregar a la lista en memoria también
        paises.append({
            'nombre': nombre,
            'poblacion': poblacion,
            'superficie': superficie,
            'continente': continente
        })
        print(f"País '{nombre}' agregado correctamente.")
    except ValueError as e:
        print(f"Ocurrió un error al agregar el pais: {e}")
    except KeyError as e:
        print(f"Ocurrió un error al agregar el pais: {e}")
    except Exception as e:
        print(f"Ocurrió un error al agregar el pais: {e}")


def actualizar_pais(paises):
    try:
        busqueda = input("Ingrese el nombre del pais a actualizar: ").strip().capitalize()
        pais = next((p for p in paises if p['nombre'].lower() == busqueda.lower()), None)
        
        if pais is None:
            print(f"No se encontró el país '{busqueda}'.")
            return

        print("¿Qué desea actualizar?")
        print("  1. Población")
        print("  2. Superficie")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            nueva_input = input("Ingrese la nueva población: ").strip()
            if not nueva_input.isdigit() or int(nueva_input) <= 0:
                print("Error: La población debe ser un número entero mayor a cero.")
                return
            pais['poblacion'] = int(nueva_input)
            print("Población actualizada correctamente.")

        elif opcion == "2":
            nueva_input = input("Ingrese la nueva superficie (km²): ").strip()
            if not nueva_input.isdigit() or int(nueva_input) <= 0:
                print("Error: La superficie debe ser un número entero mayor a cero.")
                return
            pais['superficie'] = int(nueva_input)
            print("Superficie actualizada correctamente.")

        else:
            print("Opción no válida.")
            return

        #Reescribir el CSV completo con los datos actualizados
        guardar_paises(paises)
    except StopIteration:
        print(f"No se encontró el país '{busqueda}'.")
    except ValueError:
        print("Opción no válida. Por favor, ingrese un número.")
    except TypeError:
        print("Opción no válida. Por favor, ingrese un número.")
    except Exception as e:
        print(f"Ocurrió un error al actualizar el pais: {e}")


def buscar_pais(paises):
    try:
        busqueda = input("Ingrese el nombre del pais a buscar: ").strip().capitalize()
        if not busqueda:
            print("Error: Debe ingresar un nombre.")
            return

        # Búsqueda parcial o exacta
        resultados = [p for p in paises if busqueda.lower() in p['nombre'].lower()]

        if not resultados:
            print(f"No se encontraron países con '{busqueda}'.")
        else:
            print(f"\nSe encontraron {len(resultados)} resultado(s):")
            for p in resultados:
                print(f"  Nombre: {p['nombre']} | Población: {p['poblacion']:,} | Superficie: {p['superficie']:,} km² | Continente: {p['continente']}")

    except Exception as e:
        print(f"Ocurrió un error al buscar el pais: {e}")


def cargar_paises(nombre_archivo):
    paises = []
    try:
        with open(nombre_archivo, 'r', newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)  # DictReader saltea el encabezado automáticamente
            for fila in lector:
                try:
                    pais = {
                        'nombre': fila['nombre'].strip(),
                        'poblacion': int(fila['poblacion']),    # Convertir a int acá
                        'superficie': int(fila['superficie']),  # Convertir a int acá
                        'continente': fila['continente'].strip()
                    }
                    paises.append(pais)
                except (ValueError, KeyError) as e:
                    print(f"Advertencia: fila inválida en el CSV ignorada ({e})")
    except FileNotFoundError:
        print(f"Advertencia: No se encontró '{nombre_archivo}'. Se empieza con lista vacía.")
    return paises


def guardar_paises(paises):
    with open('paises.csv', 'w', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(['nombre', 'poblacion', 'superficie', 'continente'])
        for p in paises:
            escritor.writerow([p['nombre'], p['poblacion'], p['superficie'], p['continente']])


# --- Programa principal ---
paises = cargar_paises('paises.csv')

while True:
    opcion = menu()
    if opcion == 1:
        agregar_pais(paises)
    elif opcion == 2:
        actualizar_pais(paises)
    elif opcion == 3:
        buscar_pais(paises)
    # elif opcion == 4:
    #     filtrar(paises)
    # elif opcion == 5:
    #     ordenar(paises)
    elif opcion == 6:
        mostrar_estadisticas(paises)
    elif opcion == 7:
        print("Saliendo del programa. ¡Hasta luego!")
        break
    elif opcion is not None:
        print("Opción no válida. Ingrese un número del 1 al 7.")

#funciones principales:
#def menu():
#def cargar_paises(nombre_archivo)

#funciones de manejo de datos:
#1 - def agregar_pais(paises, nombre, poblacion, superficie, continente) (Hecho)
#2 - def actualizar_pais(paises, nombre, poblacion=None, superficie=None, continente=None)
#3 - def buscar_pais(paises, nombre)

#funciones de filtrado (4) y ordenamiento (5):
#def filtrar_por_continente(paises, continente) (4)
#def filtrar_por_poblacion(paises, min_poblacion=None, max_poblacion=None) (4)
#def filtrar_por_superficie(paises, min_superficie=None, max_superficie=None) (4)
#def ordenar_por_nombre(paises, ascendente=True) (5)
#def ordenar_por_poblacion(paises, ascendente=True) (5)
#def ordenar_por_superficie(paises, ascendente=True) (5)

#funciones de mostrar estadisiticas (6): (Hecho)
#def pais_mas_poblado(paises) (6)
#def pais_menos_poblado(paises) (6)
#def promedio_poblacion(paises) (6)
#def promedio_superficie(paises) (6)
#def paises_por_continente(paises) (6)