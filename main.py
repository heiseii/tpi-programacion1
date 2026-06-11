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
from mostrar_estadisticas import *
from menu import *
import csv 

#funcion | 1 |
#cargar los paises desde un archivo csv
def agregar_pais():
    try:
        with open('paises.csv', 'a', newline='') as archivo:
            escritor = csv.writer(archivo)

            #Input del nombre
            nombre = str(input("Ingrese el nombre del pais: "))
            nombre.strip().capitalize()
            if buscar_pais(paises, nombre):
                print("Error: El pais ya existe en la lista. Elija la opcion 2 si quiere actualizarlo.")
                return
            elif not nombre.isalpha():
                print("Error: El nombre del pais debe contener letras.")
                return
            
            #Input de la poblacion
            poblacion = int(input("Ingrese la poblacion del pais: "))
            if poblacion < 0:
                print("Error: La poblacion no puede ser negativa.")
                return
            elif poblacion == 0:
                print("Error: La poblacion no puede ser cero.")
                return
            elif not isinstance(poblacion, int):
                print("Error: La poblacion debe ser un numero entero.")
                return
            
            #Input de la superficie
            superficie = int(input("Ingrese la superficie del pais: "))
            if poblacion < 0:
                print("Error: La superficie no puede ser negativa.")
                return
            elif poblacion == 0:
                print("Error: La superficie no puede ser cero.")
                return
            elif not isinstance(poblacion, int):
                print("Error: La superficie debe ser un numero entero.")
                return
            
            #Input del continente
            continente = str(input("Ingrese el continente del pais: "))
            continente.strip().capitalize()
            if not continente.isalpha():
                print("Error: El continente debe contener letras.")
                return

            nombre = nombre.strip().capitalize()
            continente = continente.strip().capitalize()
            escritor.writerow([nombre, poblacion, superficie, continente])
            print("Pais agregado correctamente.")
    except KeyError:
        print("Error: Los datos ingresados no son validos.")
    except FileNotFoundError:
        print("Error: No se encontro el archivo")
    except Exception as e:
        print(f"Ocurrio un error al agregar el pais: {e}")
            

#funcion | 2 |
#actualizar los datos de un pais
def actualizar_pais():
    try:
        busqueda = input("Ingrese el nombre del pais a actualizar: ").strip().capitalize()
        pais = buscar_pais(paises, busqueda)
    except KeyError:
        print("Los datos ingresados no son validos.")
    except FileNotFoundError:
        print("No se encontro el archivo")
    except Exception as e:
        print(f"Ocurrio un error al actualizar el pais: {e}")
    
        print("Que quiere actualizar?")
        opcion = input("""
        1. Poblacion
        2. Superficie
        """)
        if opcion == "1":
            pais['poblacion'] = int(input("Ingrese la nueva poblacion del pais: "))
            if pais['poblacion'] < 0:
                print("Error: La poblacion no puede ser negativa.")
                return
            elif pais['poblacion'] == 0:
                print("Error: La poblacion no puede ser cero.")
                return
            elif not isinstance(pais['poblacion'], int):
                print("Error: La poblacion debe ser un numero entero.")
                return
        elif opcion == "2":
            pais['superficie'] = int(input("Ingrese la nueva superficie del pais: "))
    else:
            print("Opcion no valida.")

            
    
#funcion para buscar un pais en la lista de paises (3)
def buscar_pais(paises, nombre):
    try:
        busqueda = input("Ingrese el nombre del pais a buscar: ").strip().capitalize()
        if not busqueda.isalpha():
            print("Error: El nombre del pais debe contener letras.")
            return
    except KeyError:
        print("Los datos ingresados no son validos.")
    except FileNotFoundError:
        print("No se encontro el archivo")
    except Exception as e:
        print(f"Ocurrio un error al buscar el pais: {e}")
    else:
        return next((pais for pais in paises if pais['nombre'] == busqueda), None)
    

#menu
def cargar_paises(nombre_archivo):
    paises = []
    with open(nombre_archivo, 'r', newline='') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            pais = {
                'nombre': fila[0],
                'poblacion': (fila[1]),
                'superficie': (fila[2]),
                'continente': fila[3]
            }
            paises.append(pais)
    return paises

paises = cargar_paises('paises.csv')
while True:
    opcion = menu()
    if opcion == 1:
        agregar_pais()
    elif opcion == 2:
        actualizar_pais()
    elif opcion == 3:
        buscar_pais(paises)
    #elif opcion == 4:
        #filtrar_por_continente(paises)
    #elif opcion == 5:
        #filtrar_por_poblacion(paises)
    elif opcion == 6:
        mostrar_estadisticas(paises)
    elif opcion == 7:
        break
    
    