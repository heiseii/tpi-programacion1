#Funciones de ordenamiento
def ordenar_paises(paises): #Ordena la lista de países.
    if not paises:
        print("No hay países cargados.")
        return
    else:
        print("""
        1. Ordenar por nombre
        2. Ordenar por población
        3. Ordenar por superficie (ascendente)
        4. Ordenar por superficie (descendente)
        5. Cancelar
        """)
        try:
            opcion = int(input("Seleccione una opcion: "))
            if opcion == 1:
                ordenar_por_nombre(paises)
            elif opcion == 2:
                ordenar_por_poblacion(paises)
            elif opcion == 3:
                ordenar_por_superficie_asc(paises)
            elif opcion == 4:
                ordenar_por_superficie_desc(paises)
            elif opcion == 5:
                print("Volviendo al menu principal.")
                return
            else:
                print("Opcion no valida.")
        except (TypeError, ValueError):
            print("Opcion no valida.")
        except Exception as e:
            print(f"Ocurrio un error: {e}")
        

def ordenar_por_nombre(paises): #Ordena la lista de países por nombre.
    paises.sort(key=lambda x: x['nombre'].lower())
    for pais in paises:
        print(f"Nombre: {pais['nombre']} | Población: {pais['poblacion']:,} | Superficie: {pais['superficie']:,} km² | Continente: {pais['continente']}")

def ordenar_por_poblacion(paises): #Ordena la lista de países por población.
    paises.sort(key=lambda x: x['poblacion'], reverse=True)
    for pais in paises:
        print(f"Nombre: {pais['nombre']} | Población: {pais['poblacion']:,} | Superficie: {pais['superficie']:,} km² | Continente: {pais['continente']}")

def ordenar_por_superficie_asc(paises): #Ordena la lista de países por superficie (ascendente).
    paises.sort(key=lambda x: x['superficie'])
    for pais in paises:
        print(f"Nombre: {pais['nombre']} | Población: {pais['poblacion']:,} | Superficie: {pais['superficie']:,} km² | Continente: {pais['continente']}")

def ordenar_por_superficie_desc(paises): #Ordena la lista de países por superficie (descendente).
    paises.sort(key=lambda x: x['superficie'], reverse=True)
    for pais in paises:
        print(f"Nombre: {pais['nombre']} | Población: {pais['poblacion']:,} | Superficie: {pais['superficie']:,} km² | Continente: {pais['continente']}")

