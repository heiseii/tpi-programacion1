# Muestra las opciones disponibles y devuelve el número ingresado por el usuario.
# Si el input no es un número válido, devuelve None y el bucle principal lo maneja.
def menu():
    print("""
    1. Agregar país
    2. Actualizar país
    3. Buscar país
    4. Filtrar países
    5. Ordenar países
    6. Mostrar estadísticas
    7. Salir
    """)
    try:
        opcion = int(input("Seleccione una opción: "))
        return opcion
    except (TypeError, ValueError):
        print("Opción no válida. Por favor, ingrese un número.")
        return None
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return None