# Matrix

**Nota:** El archivo que contenga las funciones debe llamarse matrix.py.

---

1. **Función `build_matrix()`:** Esta función no tiene ningún parámetro de entrada. Debe retornar una matriz de dimensiones 5x5 compuesta por números enteros aleatorios. La matriz deberá estar representada utilizando listas.

   Ejemplo:
   Si `build_matrix()` generara una matriz de 2x3, el retorno debería ser algo como: 
   ```python
   [[3,-4,2],[7,8,9]]
   ```
   Aquí, la matriz del ejemplo tiene 2 filas y 3 columnas (por eso su dimensión es 2x3). Las filas están representadas por cada elemento de la lista principal: [3,-4,2] y [7,8,9]. Cada fila es, a su vez, una lista que contendrá tantos elementos como columnas tenga la matriz.


2. **Función `find_sequence_by_row(matrix)`:** Esta función tiene la tarea de detectar y retornar todas las secuencias de cuatro números consecutivos presentes (sólo de izquierda a derecha) en las filas de la `matrix` generada por `build_matrix()`. Las posiciones de inicio y fin de cada secuencia detectada deben ser retornadas en una lista con el formato que se muestra a continuación.

   Ejemplo:
   Dada la matriz 
   ```python
   [[3,3,7,3,9],[3,3,7,4,9],[2,3,4,5,6],[5,5,3,6,5],[6,5,3,5,5]]
   ```
   La función `find_sequence_by_row(matrix)` debería retornar:
   ```python
   [[[2, 0], [2, 3]], [[2, 1], [2, 4]]]
   ```
   En este caso, existen dos secuencias, ambas en la misma fila. 
   
   Nota: Como usamos una lista para representar la matriz, tanto las filas como las columnas comienzan su numeración desde el índice 0. Es decir, la posición del primer elemento en la esquina superior izquierda de la matriz es [0, 0].


3. **Función `find_sequence_by_column(matrix)`:** Similar a `find_sequence_by_row(matrix)`, pero esta función debe detectar secuencias (sólo de arriba abajo) en las columnas de la `matrix` generada por `build_matrix()`.

   Ejemplo:
   Dada la matriz 
   ```python
   [[1,1,1,1,1],[2,2,2,2,2],[3,5,3,9,8],[4,4,7,8,9],[0,0,0,0,0]]
   ```
   La función `find_sequence_by_column(matrix)` debería retornar:
   ```python
   [[[0, 0], [3, 0]]]
   ```

---