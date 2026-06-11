#Funcion para mostrar estadisticas (6)
import csv
def mostrar_estadisticas(paises):
    print("\nEstadísticas:")
    print(f"Pais mas poblado: {pais_mas_poblado(paises)}")
    print(f"Pais menos poblado: {pais_menos_poblado(paises)}")
    print(f"Promedio de poblacion: {promedio_poblacion(paises)}")
    print(f"Promedio de superficie: {promedio_superficie(paises)}")
    print(f"Paises por continente: {paises_por_continente(paises)}")

def pais_mas_poblado(paises):
    return max(paises, key=lambda pais: pais['poblacion'])['nombre']

def pais_menos_poblado(paises):
    return min(paises, key=lambda pais: pais['poblacion'])['nombre']

def promedio_poblacion(paises):
    with open('paises.csv', 'r', newline='') as archivo:
        lector = csv.reader(archivo)
        poblaciones = [int(fila[1]) for fila in lector]
        print("Poblaciones:", poblaciones)  # Print the poblaciones list
        return sum(poblaciones) / len(poblaciones)

def promedio_superficie(paises):
    total_superficie = sum(pais['superficie'] for pais in paises)
    print("Total superficie:", total_superficie)  # Print the total superficie
    return total_superficie / len(paises)

def paises_por_continente(paises):
    print("Paises:", paises)  # Print the countries list
    return {continente: [pais['nombre'] for pais in paises if pais['continente'] == continente] for continente in set(pais['continente'] for pais in countries)}
