import csv
#Función para guardar el CSV
#Guarda el CSV de la lista de paises en un archivo llamado paises.csv
def guardar_paises(paises):
    with open('paises.csv', 'w', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(['nombre', 'poblacion', 'superficie', 'continente'])
        for p in paises:
            escritor.writerow([p['nombre'], p['poblacion'], p['superficie'], p['continente']])

# Función para agregar un país
def agregar_pais(paises):
    try:
        nombre = input("Ingrese el nombre del pais: ").strip().capitalize()
        if not nombre:
            print("Error: El nombre no puede estar vacío.")
            return
        
        # Verificar si ya existe (búsqueda exacta)
        if any(p['nombre'].lower() == nombre.lower() for p in paises):
            print("Error: El pais ya existe. Use la opción 2 para actualizarlo.")
            return
        
        # Input de poblacion
        poblacion_input = input("Ingrese la poblacion del pais: ").strip()
        if not poblacion_input.isdigit():
            print("Error: La poblacion debe ser un número entero positivo.")
            return
        poblacion = int(poblacion_input)
        if poblacion <= 0:
            print("Error: La poblacion debe ser mayor a cero.")
            return
        
        # Input de superficie
        superficie_input = input("Ingrese la superficie del pais (km²): ").strip()
        if not superficie_input.isdigit():
            print("Error: La superficie debe ser un número entero positivo.")
            return
        superficie = int(superficie_input)
        if superficie <= 0:
            print("Error: La superficie debe ser mayor a cero.")
            return
        
        # Input de continente
        continente = input("Ingrese el continente del pais: ").strip().capitalize()
        if not continente:
            print("Error: El continente no puede estar vacío.")
            return
        
        # Agregar a la lista en memoria y guardar en CSV
        paises.append({
            'nombre': nombre,
            'poblacion': poblacion,
            'superficie': superficie,
            'continente': continente
        })
        guardar_paises(paises)
        print(f"País '{nombre}' agregado correctamente.")

    except ValueError as e:
        print(f"Ocurrió un error al agregar el pais: {e}")
    except KeyError as e:
        print(f"Ocurrió un error al agregar el pais: {e}")
    except Exception as e:
        print(f"Ocurrió un error al agregar el pais: {e}")
