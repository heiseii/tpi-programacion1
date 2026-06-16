from menu import * #funcion del menu
from agregar_pais import * #funcion para agregar un pais
from actualizar_pais import * #funcion para actualizar un pais
from buscar_pais import * #funcion para buscar un pais
from cargar_paises import * #funcion para cargar el CSV
#from filtrar_paises import * #funcion para filtrar
#from ordenar_paises import * #funcion para ordenar
from mostrar_estadisticas import * #funcion para mostrar estadisticas

# Punto de entrada del programa. Carga los datos del CSV y ejecuta el menú en bucle
# hasta que el usuario elija salir.
# Programa / menu principal 
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
    #     filtrar_paises(paises)
    # elif opcion == 5:
    #     ordenar_paises(paises)
    elif opcion == 6:
        mostrar_estadisticas(paises)
    elif opcion == 7:
        print("Saliendo del programa.")
        break
    elif opcion is not None:
        print("Opción no válida. Ingrese un número del 1 al 7.")

#funciones principales:
#def menu(): (Hecho)
#def cargar_paises(nombre_archivo) (Hecho)

#funciones de manejo de datos:
#1 - def agregar_pais(paises, nombre, poblacion, superficie, continente) (Hecho)
#2 - def actualizar_pais(paises, nombre, poblacion=None, superficie=None, continente=None) (Hecho)
#3 - def buscar_pais(paises, nombre) (Hecho)

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