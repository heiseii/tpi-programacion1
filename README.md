# Sistema de Gestión de Países

Aplicación de consola desarrollada en Python 3 para gestionar información sobre países.
Permite agregar, actualizar, buscar, filtrar, ordenar y obtener estadísticas de un conjunto
de datos almacenado en un archivo CSV.

Trabajo Práctico Integrador - Programación 1
Tecnicatura Universitaria en Programación - UTN

---

## Integrantes

- Lucca Joan Weinzettel (M26 C1-02)
- Juan Cruz Caminos (M26 C1-09)

---

## Requisitos

- Python 3.x instalado
- No requiere librerías externas, solo módulos de la biblioteca estándar de Python (`csv`)

---

## Instalación y ejecución

### Windows

1. Descargar o clonar el repositorio
2. Abrir una terminal (CMD o PowerShell) en la carpeta del proyecto
3. Ejecutar el programa con el siguiente comando:
python main.py

### Linux

1. Clonar el repositorio o descomprimir el archivo del proyecto
2. Abrir una terminal en la carpeta del proyecto
3. Ejecutar el programa con el siguiente comando:
python3 main.py

---

## Estructura del proyecto
tpi-programacion1/

├── main.py                 # Archivo principal, contiene el bucle del programa

├── menu.py                 # Función que muestra y gestiona el menú de opciones

├── mostrar_estadisticas.py # Funciones de cálculo y visualización de estadísticas

├── paises.csv              # Dataset base con países precargados

└── README.md               # Este archivo

---

## Funcionalidades

| Opción | Descripción |
|--------|-------------|
| 1. Agregar país | Solicita nombre, población, superficie y continente. Valida que no haya campos vacíos ni duplicados. |
| 2. Actualizar país | Permite modificar la población o la superficie de un país existente. |
| 3. Buscar país | Búsqueda por nombre con coincidencia parcial o exacta. |
| 4. Filtrar países | Filtra por continente, rango de población o rango de superficie. |
| 5. Ordenar países | Ordena por nombre, población o superficie de forma ascendente o descendente. |
| 6. Estadísticas | Muestra el país más y menos poblado, promedios de población y superficie, y cantidad de países por continente. |
| 7. Salir | Cierra el programa. |

---

## Ejemplos de uso

**Agregar un país:**
Ingrese el nombre del pais: México

Ingrese la poblacion del pais: 126014024

Ingrese la superficie del pais (km²): 1964375

Ingrese el continente del pais: América

País 'México' agregado correctamente.

**Buscar un país:**
Ingrese el nombre del pais a buscar: ar

Se encontraron 2 resultado(s):

Nombre: Argentina | Población: 45,376,763 | Superficie: 2,780,400 km² | Continente: América

Nombre: Alemania  | Población: 83,149,300 | Superficie: 357,022 km²   | Continente: Europa

**Estadísticas:**

País más poblado: China

País menos poblado: Italia

Promedio población: 480,907,972

Promedio superficie: 3,077,674
Países por continente:

América: 3 país/es -> Argentina, Brasil, Estados Unidos

Asia: 3 país/es -> Japón, India, China

Europa: 3 país/es -> Alemania, Francia, Italia

---

## Dataset base

El archivo `paises.csv` incluye 9 países precargados:
Argentina, Brasil, Estados Unidos, Alemania, Francia, Italia, Japón, India y China.

El formato del archivo es el siguiente:
nombre,poblacion,superficie,continente

Argentina,45376763,2780400,América

---

## Video demostrativo

[Insertar link aquí]

## Documentación

Abrir el PDF 'Documentacion' dentro del repo
