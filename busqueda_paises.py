#funciones principales:
#def menu():
#def cargar_paises(nombre_archivo)

#funciones de manejo de datos:
#def agregar_pais(paises, nombre, poblacion, superficie, continente)
#def actualizar_pais(paises, nombre, poblacion=None, superficie=None, continente=None)
#def buscar_pais(paises, nombre)

#funciones de filtrado y ordenamiento:
#def filtrar_por_continente(paises, continente)
#def filtrar_por_poblacion(paises, min_poblacion=None, max_poblacion=None)
#def filtrar_por_superficie(paises, min_superficie=None, max_superficie=None)
#def ordenar_por_nombre(paises, ascendente=True)
#def ordenar_por_poblacion(paises, ascendente=True)
#def ordenar_por_superficie(paises, ascendente=True)

#funciones de mostrar estadisiticas:
#def pais_mas_poblado(paises)
#def pais_menos_poblado(paises)
#def promedio_poblacion(paises)
#def promedio_superficie(paises)
#def paises_por_continente(paises)

import csv 

def menu(): #funcion para mostrar el menu y obtener la opcion del usuario
    print("""
    1. Agregar país
    2. Actualizar país
    3. Buscar país
    4. Filtrar paises
    5. Ordenar paises
    6. Mostrar estadísticas
    7. Salir
    """)

    try: #manejo de errores para la entrada del usuario
        opcion = int(input("Seleccione una opción: "))
        return opcion
    except ValueError:
        print("Opción no válida. Por favor, ingrese un número.")
        return None
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return None
    
    #Aca irian las funciones con las condicionales

#funcion para cargar los paises desde un archivo csv
def cargar_paises(nombre_archivo): 
    paises = [] #lista vacia para almacenar los paises
    with open(nombre_archivo, mode='r', encoding='utf-8') as archivo:
        lector_csv = csv.DictReader(archivo)
        for fila in lector_csv:
            pais = {
                'nombre': str(fila['nombre']),
                'poblacion': int(fila['poblacion']),
                'superficie': int(fila['superficie']),
                'continente': str(fila['continente'])
            }
            paises.append(pais)
    return paises