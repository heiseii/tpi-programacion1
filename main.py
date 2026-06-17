from menu import * #funcion del menu
from agregar_pais import * #funcion para agregar un pais
from actualizar_pais import * #funcion para actualizar un pais
from buscar_pais import * #funcion para buscar un pais
from cargar_paises import * #funcion para cargar el CSV
from filtrar_paises import * #funcion para filtrar
from ordenar_paises import * #funcion para ordenar
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
    elif opcion == 4:
        filtrar_paises(paises)
    elif opcion == 5:
        ordenar_paises(paises)
    elif opcion == 6:
        mostrar_estadisticas(paises)
    elif opcion == 7:
        print("Saliendo del programa.")
        break
    elif opcion is not None:
        print("Opción no válida. Ingrese un número del 1 al 7.")

