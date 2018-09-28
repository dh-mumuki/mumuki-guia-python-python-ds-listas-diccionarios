## Estructura de datos: Listas

Una forma de agrupar datos en python es utilizando una lista, una lista es una estructura de datos que permite mantener en un solo lugar un conjunto de elementos.

Veamos como se puede declarar una lista:

``` python
# una lista con enteros
[-4, 1, 5, 10, 33, -10]

# una lista con strings
['hola', 'python', 'etc']

# una lista vacia
[]

# una lista con distintos tipos de datos

[-4, 1, 5, 'python', 10, 'etc', 3.44]

```
En esta demostración declaramos 4 listas, una con enteros, otra con strings, una lista vacía y una con tipos de datos mixtos.

En python las listas pueden contener distintos tipos de datos.


#### Accediendo a los elementos dentro de una lista

Cada elemento dentro de una lista tiene una posición y es posible referirse a uno o algunos de estos elementos.

Para acceder a uno de estos elementos se debe:
  
  * numerar cada elemento de la lista desde cero, o sea el primer elemento es el elemento 0, el segundo 1, y asi sucesivamente, este número que indica la posición del elemento dentro de la lista, se conoce como índice.

  * indicar éste índice dentro de dos corchetes `lista[índice]`

``` python
# 0  1  2  3   4    5
[-4, 1, 5, 10, 33, -10][3]
``` 
_Salida:_
**> 10**

``` python
# 0       1         2
['hola', 'python', 'etc'][1]
``` 
_Salida:_
**> python**

Al momento de acceder a un elemento de la lista, podemos utilizarlo como el tipo de datos que es.

``` python
# 0  1  2  3   4    5
[-4, 1, 5, 10, 33, -10][3] + [-4, 1, 5, 10, 33, -10][0]
``` 
_Salida:_
**> 6**

Como podemos observar en esta última demostración, es posible sumar ambos números refiriendonos a ellos desde una lista.

Es posible asignar a una nombre a una lista, y desde ahi, referirse a algún elemento.

``` python
lista_enteros = [-4, 1, 5, 10, 33, -10]

lista_enteros[0]
``` 
_Salida:_
**> -4**

Como habíamos comentado también es posible acceder a un conjunto de éstos elementos, a este recurso se le conoce como slicing, para hacer un slicing debemos indicar dentro de dos corchetes y separado por dos puntos,  el elemento de inicio, el de final (no se incluye) y el salto, `[lista][inicio:fin:salto]`, veamos algunos ejemplos

``` python
lista_enteros = [-4, 1, 5, 10, 33, -10]
#lista[inicio:fin:salto]
lista_enteros[0:5:1]
``` 
_Salida:_
**> [-4, 1, 5, 10, 33]**

A diferencia del llamado al índice, el slicing devuelve una sublista de elementos.

En éste slice no se observa el elemento -10 que ocupa la posición 5, esto es porque el último elemento señalado no se incluye.

``` python
lista_enteros = [-4, 1, 5, 10, 33, -10]

lista_enteros[0:5:2]
``` 
_Salida:_
**> [-4, 5, 33]**


#### Operaciones sobre listas.

Las listas en python tienen métodos asociados que permiten realizar alguna acción sobre ellas.

Estos métodos son instrucciones que permiten llevar a cabo operaciones como:

  * Agregar uno o más elementos.
  * Buscar elementos según alguna propiedad.
  * Quitar uno o más elemtos.
  * Ordenar los elementos según alguna propiedad.

Para utilizar alguno de estos métodos es necesario primero inicializar una lista.

#### Método append.

Este método se utiliza para agregar un elemento al final de una lista.

El modo de uso es **lista.append(elemento_nuevo)**, entonces el **append** toma el **elemento_nuevo** y lo incluye en la última posición de **lista**