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
    except TypeError:
        print("Opción no válida. Por favor, ingrese un número.")
        return None
    except ValueError:
        print("Opción no válida. Por favor, ingrese un número.")
        return None
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return None
