# Recorre la lista de países y devuelve todos los que contengan
# el término ingresado en su nombre, ya sea de forma parcial o exacta.
def buscar_pais(paises): 
    try: 
#input de la busqueda
        busqueda = input("Ingrese el nombre del pais a buscar: ").strip().capitalize()
        if not busqueda:
            print("Error: Debe ingresar un nombre.")
            return

#busqueda parcial o exacta
        resultados = [p for p in paises if busqueda.lower() in p['nombre'].lower()]

        if not resultados:
            print(f"No se encontraron países con '{busqueda}'.")
        else:
            print(f"\nSe encontraron {len(resultados)} resultado(s):")
            for p in resultados:
                print(f"  Nombre: {p['nombre']} | Población: {p['poblacion']:,} | Superficie: {p['superficie']:,} km² | Continente: {p['continente']}")

    except Exception as e:
        print(f"Ocurrió un error al buscar el pais: {e}")
