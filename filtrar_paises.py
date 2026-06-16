# filtrar_paises.py

def filtrar_por_continente(paises, continente):
    """
    Filtra la lista de países por un continente específico (insensible a mayúsculas).
    """
    resultado = []
    for pais in paises:
        if pais['continente'].lower() == continente.lower():
            resultado.append(pais)
    return resultado


def filtrar_por_poblacion(paises, min_poblacion=None, max_poblacion=None):
    """
    Filtra los países que están dentro del rango de población especificado.
    """
    resultado = []
    for pais in paises:
        cumple_min = True
        cumple_max = True
        
        if min_poblacion is not None and pais['poblacion'] < min_poblacion:
            cumple_min = False
        if max_poblacion is not None and pais['poblacion'] > max_poblacion:
            cumple_max = False
            
        if cumple_min and cumple_max:
            resultado.append(pais)
    return resultado


def filtrar_por_superficie(paises, min_superficie=None, max_superficie=None):
    """
    Filtra los países que están dentro del rango de superficie especificado.
    """
    resultado = []
    for pais in paises:
        cumple_min = True
        cumple_max = True
        
        if min_superficie is not None and pais['superficie'] < min_superficie:
            cumple_min = False
        if max_superficie is not None and pais['superficie'] > max_superficie:
            cumple_max = False
            
        if cumple_min and cumple_max:
            resultado.append(pais)
    return resultado


# --- Ejemplo de uso local (opcional) ---
if __name__ == "__main__":
    # Datos de prueba de ejemplo
    datos_prueba = [
        {'nombre': 'Argentina', 'continente': 'América', 'poblacion': 46000000, 'superficie': 2780000},
        {'nombre': 'Uruguay', 'continente': 'América', 'poblacion': 3500000, 'superficie': 176000},
        {'nombre': 'Francia', 'continente': 'Europa', 'poblacion': 68000000, 'superficie': 551000},
    ]
    
    print("Países en América:")
    print(filtrar_por_continente(datos_prueba, 'América'))
    
    print("\nPaíses con más de 40 millones de habitantes:")
    print(filtrar_por_poblacion(datos_prueba, min_poblacion=40000000))