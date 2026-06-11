#funciones principales:
#def menu():
#def cargar_paises(nombre_archivo)

#funciones de manejo de datos:
#1 - def agregar_pais(paises, nombre, poblacion, superficie, continente)
#2 - def actualizar_pais(paises, nombre, poblacion=None, superficie=None, continente=None)
#3 - def buscar_pais(paises, nombre)

#funciones de filtrado (4) y ordenamiento (5):
#def filtrar_por_continente(paises, continente) (4)
#def filtrar_por_poblacion(paises, min_poblacion=None, max_poblacion=None) (4)
#def filtrar_por_superficie(paises, min_superficie=None, max_superficie=None) (4)
#def ordenar_por_nombre(paises, ascendente=True) (5)
#def ordenar_por_poblacion(paises, ascendente=True) (5)
#def ordenar_por_superficie(paises, ascendente=True) (5)

#funciones de mostrar estadisiticas (6):
#def pais_mas_poblado(paises) (6)
#def pais_menos_poblado(paises) (6)
#def promedio_poblacion(paises) (6)
#def promedio_superficie(paises) (6)
#def paises_por_continente(paises) (6)

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
    try:
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
    except KeyError as e:
        print(f"Error: La columna {e} no se encuentra en el archivo CSV.")
    except csv.Error as e:
        print(f"Error al leer el archivo CSV: {e}")
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error al cargar los países: {e}")
    return paises

#funcion para agregar un nuevo pais a la lista de paises (1)
def agregar_pais(paises, nombre, poblacion, superficie, continente):
    try:    
        pais = {
            'nombre': nombre,
            'poblacion': poblacion,
            'superficie': superficie,
            'continente': continente
        }
        paises.append(pais)
        return paises
    except Exception as e:
        print(f"Ocurrió un error al agregar el país: {e}")
        return paises

def actualizar_pais(paises, nombre, poblacion=None, superficie=None, continente=None):
    try:
        for pais in paises:
            if pais['nombre'] == nombre:
                if poblacion is not None:
                    pais['poblacion'] = poblacion
                if superficie is not None:
                    pais['superficie'] = superficie
                if continente is not None:
                    pais['continente'] = continente
                return paises
        return paises
    except Exception as e:
        print(f"Ocurrió un error al actualizar el país: {e}")
        return paises

