# Actividad Python - Estadísticas y Vacunas
Programa realizado como parte de las actividades semanales de la cátedra 2021 de la materia Estructura de Datos, de la carrera Ingeniería en Computación de la Universidad Nacional de Tres de Febrero.

El mismo utiliza un dataset de Datos Abiertos proveídos por el Ministerio de Salud (Argentina).
Disponible aquí: <br>
http://datos.salud.gob.ar/dataset/vacunas-contra-covid19-dosis-aplicadas-en-la-republica-argentina

Cabe señalar que es un archivo muy pesado (alrededor 2GB comprimido, 17GB descomprimido). Por lo que, incluso con buenas especificaciones técnicas, la ejecución del programa será larga y no debería ser interrumpida. Saludos.

## Consigna
### Consigna original de 2021
Se dispone de un archivo de valores separados por comas que contiene información sobre las dosis aplicadas de las vacunas contra el COVID-19 en todas las jurisdicciones del país

Dado que el archivo es muy extenso como para abrirlo y analizarlo en Excel, se prefirió realizar un programa en Python que pueda responder con complejidad O(n), y evitando recorrer el archivo más de una vez, las siguientes estadísticas de interés:

1. Cantidad de vacunas aplicadas por provincia:
Provincia, Dosis 1, Dosis 2, Aplicadas total

2. Cantidad de aplicaciones por condición de la persona:
Condición, Aplicaciones

3. Cantidad de vacunas aplicadas por Género:
Género, Dosis 1, Dosis 2, Total

4. Totales:
Cantidad total de vacunados con 1 dosis, Cantidad total de vacunados con 2 dosis, Cantidad total de vacunados


Toda esta información deberá presentarse en forma de tablas, en cuatro archivos diferentes que utilicen campos de longitud fija.

### Actualización 11/2022
Debido a que la cantidad de dosis posibles aumentó, se realizaron modificaciones al programa
que permitan almacenar los datos de la siguiente manera en cada categoría:

* Dosis 1, Dosis 2, Adicional, Refuerzo, Única, Totales
