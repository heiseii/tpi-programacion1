# filtrar_paises.py
def filtrar_paises(paises):
    if not paises:
        print("No hay países cargados.")
        return
    else:
        try:
            print("""
                  1. Filtrar por continente
                  2. Filtrar por población
                  3. Filtrar por superficie
                  4. Cancelar
                  """)
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                continente = input("Ingrese el continente: ")
                filtrar_por_continente(paises, continente)
            elif opcion == "2":
                min_poblacion = input("Ingrese la población minima: ")
                max_poblacion = input("Ingrese la población maxima: ")
                filtrar_por_poblacion(paises, min_poblacion, max_poblacion)
            elif opcion == "3":
                min_superficie = input("Ingrese la superficie minima: ")
                max_superficie = input("Ingrese la superficie maxima: ")
                filtrar_por_superficie(paises, min_superficie, max_superficie)
            elif opcion == "4":
                print("Volviendo al menu principal.")
                return
            else:
                print("Opcion no valida.")
                return
        except (TypeError, ValueError):
            print("Opcion no valida.")
        except Exception as e:
            print(f"Ocurrio un error: {e}")

def filtrar_por_continente(paises, continente):
    for pais in paises:
        if pais['continente'].lower() == continente.strip().lower():
            print(f"Nombre: {pais['nombre']} | Población: {pais['poblacion']:,} | Superficie: {pais['superficie']:,} km² | Continente: {pais['continente']}")

def filtrar_por_poblacion(paises, min_poblacion, max_poblacion):
    if not min_poblacion.isdigit() or not max_poblacion.isdigit():
        print("Error: Los valores deben ser números enteros positivos.")
        return
    for pais in paises:
        if pais['poblacion'] >= int(min_poblacion) and pais['poblacion'] <= int(max_poblacion):
            print(f"Nombre: {pais['nombre']} | Población: {pais['poblacion']:,} | Superficie: {pais['superficie']:,} km² | Continente: {pais['continente']}")

def filtrar_por_superficie(paises, min_superficie, max_superficie):
    if not min_superficie.isdigit() or not max_superficie.isdigit():
        print("Error: Los valores deben ser números enteros positivos.")
        return
    for pais in paises:
        if pais['superficie'] >= int(min_superficie) and pais['superficie'] <= int(max_superficie):
            print(f"Nombre: {pais['nombre']} | Población: {pais['poblacion']:,} | Superficie: {pais['superficie']:,} km² | Continente: {pais['continente']}")