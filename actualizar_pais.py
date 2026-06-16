from guardar_paises import *
#Busca un país por nombre exacto y permite modificar su población o superficie.
#Si el país no existe, informa al usuario. Al terminar, reescribe el CSV completo.
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


