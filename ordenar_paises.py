# ordenar_paises.py

def ordenar_por_nombre(paises, ascendente=True):
    """
    Ordena la lista de países alfabéticamente por nombre.
    """
    return sorted(paises, key=lambda x: x['nombre'].lower(), reverse=not ascendente)


def ordenar_por_poblacion(paises, ascendente=True):
    """
    Ordena la lista de países según su población.
    """
    return sorted(paises, key=lambda x: x['poblacion'], reverse=not ascendente)


def ordenar_por_superficie(paises, ascendente=True):
    """
    Ordena la lista de países según su superficie.
    """
    return sorted(paises, key=lambda x: x['superficie'], reverse=not ascendente)


# --- Ejemplo de uso local (opcional) ---
if __name__ == "__main__":
    # Datos de prueba de ejemplo
    datos_prueba = [
        {'nombre': 'Uruguay', 'continente': 'América', 'poblacion': 3500000, 'superficie': 176000},
        {'nombre': 'Argentina', 'continente': 'América', 'poblacion': 46000000, 'superficie': 2780000},
        {'nombre': 'Francia', 'continente': 'Europa', 'poblacion': 68000000, 'superficie': 551000},
    ]
    
    print("Ordenados por población (Descendente):")
    paises_ordenados = ordenar_por_poblacion(datos_prueba, ascendente=False)
    for p in paises_ordenados:
        print(f"{p['nombre']}: {p['poblacion']} habitantes.")