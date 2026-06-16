#Funcion para mostrar estadisticas: 
# pais mas poblado, pais menos poblado, promedio poblacion, promedio superficie
def mostrar_estadisticas(paises):
    if not paises:
        print("No hay países cargados.")
        return

    print("\nEstadísticas:")
    print(f"País más poblado: {pais_mas_poblado(paises)}")
    print(f"País menos poblado: {pais_menos_poblado(paises)}")
    print(f"Promedio población: {promedio_poblacion(paises):,.0f} habitantes.")
    print(f"Promedio superficie: {promedio_superficie(paises):,.0f}")
    
    print("\n  Países por continente:")
    conteo = paises_por_continente(paises)
    for continente, nombres in conteo.items():
        print(f"    {continente}: {len(nombres)} país/es -> {', '.join(nombres)}")


def pais_mas_poblado(paises): #funcion para obtener el pais mas poblado
    return max(paises, key=lambda p: p['poblacion'])['nombre']


def pais_menos_poblado(paises): #funcion para obtener el pais menos poblado 
    return min(paises, key=lambda p: p['poblacion'])['nombre']


def promedio_poblacion(paises): #funcion para obtener el promedio de poblacion
    # Usamos la lista en memoria, no re-leemos el CSV
    total = sum(p['poblacion'] for p in paises)
    return total / len(paises)


def promedio_superficie(paises): #funcion para obtener el promedio de superficie
    total = sum(p['superficie'] for p in paises)
    return total / len(paises)

#funcion para obtener los paises por continente
def paises_por_continente(paises): 
    resultado = {}
    for pais in paises:
        continente = pais['continente']
        if continente not in resultado:
            resultado[continente] = []
        resultado[continente].append(pais['nombre'])
    return resultado