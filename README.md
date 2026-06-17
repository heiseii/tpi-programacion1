# Sistema de Gestión de Países

Aplicación de consola desarrollada en Python 3 para gestionar información sobre países.
Permite agregar, actualizar, buscar, filtrar, ordenar y obtener estadísticas de un conjunto
de datos almacenado en un archivo CSV.

Trabajo Práctico Integrador - Programación 1
Tecnicatura Universitaria en Programación - UTN

---

## Integrantes y participación

**Lucca Joan Weinzettel (M26 C1-02)**
- Configuración del repositorio y estructura del proyecto
- Implementación de `agregar_pais()` con validaciones completas
- Implementación de `actualizar_pais()`
- Implementación de `buscar_pais()` con soporte de coincidencia parcial
- Implementación de todas las funciones de estadísticas (`mostrar_estadisticas()`, `pais_mas_poblado()`, `pais_menos_poblado()`, `promedio_poblacion()`, `promedio_superficie()`, `paises_por_continente()`)

- Modularización del proyecto en archivos separados por responsabilidad

**Juan Cruz Caminos (M26 C1-09)**
- Creación y mantenimiento del dataset base (`paises.csv`)
- Documentación técnica del proyecto (informe PDF)
- Implementación de `filtrar_paises()`
- Implementacion de `ordenar_paises()`
  
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

├── main.py                 # Punto de entrada, contiene el bucle principal del programa

├── menu.py                 # Muestra el menú y devuelve la opción elegida por el usuario

├── agregar_pais.py         # Validación y alta de nuevos países

├── actualizar_pais.py      # Modificación de población o superficie de un país existente

├── buscar_pais.py          # Búsqueda por nombre con coincidencia parcial o exacta

├── filtrar_paises.py       # Filtrado por continente, rango de población o superficie

├── ordenar_paises.py       # Ordenamiento por nombre, población o superficie

├── mostrar_estadisticas.py # Cálculo y visualización de estadísticas

├── guardar_paises.py       # Reescritura del CSV a partir de la lista en memoria

├── paises.csv              # Dataset base con países precargados

└── README.md               # Este archivo

---

## Funcionalidades

| Opción | Función | Descripción |
|--------|---------|-------------|
| 1. Agregar país | `agregar_pais()` | Solicita los cuatro campos requeridos. Valida que no haya campos vacíos, que los valores numéricos sean enteros positivos y que el país no exista previamente. |
| 2. Actualizar país | `actualizar_pais()` | Busca un país por nombre exacto y permite modificar su población o superficie. Reescribe el CSV completo al terminar. |
| 3. Buscar país | `buscar_pais()` | Recorre la lista y devuelve todos los países cuyo nombre contenga el término ingresado, de forma parcial o exacta. |
| 4. Filtrar países | `filtrar_paises()` | Filtra la lista por continente, rango de población o rango de superficie, mostrando solo los registros que cumplan la condición. |
| 5. Ordenar países | `ordenar_paises()` | Ordena la lista por nombre, población o superficie en dirección ascendente o descendente según elija el usuario. |
| 6. Estadísticas | `mostrar_estadisticas()` | Calcula y muestra el país con mayor y menor población, el promedio de población y superficie, y el agrupamiento de países por continente. |
| 7. Salir | — | Termina el bucle principal y cierra el programa. |

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

**Filtrar por continente:**

Seleccione una opción: 4

Filtrar por continente
Filtrar por población
Filtrar por superficie
Cancelar

Seleccione una opción: 1

Ingrese el continente: Asia

Nombre: Japón  | Población: 125,800,000 | Superficie: 377,975 km²   | Continente: Asia

Nombre: India  | Población: 1,380,004,385 | Superficie: 3,287,263 km² | Continente: Asia

Nombre: China  | Población: 1,439,323,776 | Superficie: 9,596,961 km² | Continente: Asia


**Estadísticas:**

Estadísticas:

País más poblado: China

País menos poblado: Italia

Promedio población: 480,907,972 habitantes.

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
