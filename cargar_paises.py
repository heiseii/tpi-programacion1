import csv
# Lee el archivo CSV y construye la lista de diccionarios que usa el programa.
# Si el archivo no existe, inicia con una lista vacía.
# Si una fila tiene formato inválido, la ignora y continúa con las demás.
def cargar_paises(nombre_archivo): 
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