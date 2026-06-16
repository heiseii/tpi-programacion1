import csv
# Reescribe el archivo paises.csv completo a partir de la lista en memoria.
# Se llama cada vez que se agrega o modifica un país.
def guardar_paises(paises):
    with open('paises.csv', 'w', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(['nombre', 'poblacion', 'superficie', 'continente'])
        for p in paises:
            escritor.writerow([p['nombre'], p['poblacion'], p['superficie'], p['continente']])
