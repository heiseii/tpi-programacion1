import csv
# Función para cargar el CSV.
# Lee el archivo CSV y devuelve una lista de diccionarios con los datos de los países.
def cargar_paises(nombre_archivo): #funcion para cargar el CSV
    paises = []
    try: 
        with open(nombre_archivo, 'r', newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)  #dictreader para leer el csv
            for fila in lector:
                try:
                    pais = { 
                        'nombre': fila['nombre'].strip(),
                        'poblacion': int(fila['poblacion']),    
                        'superficie': int(fila['superficie']),  
                        'continente': fila['continente'].strip()
                    }
                    paises.append(pais)
                except (ValueError, KeyError) as e:
                    print(f"Advertencia: fila inválida en el CSV ignorada ({e})")
    except FileNotFoundError:
        print(f"Advertencia: No se encontró '{nombre_archivo}'. Se empieza con lista vacía.")
    return paises