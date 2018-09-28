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

```
En esta demostración declaramos 3 listas, una con enteros, otra con strings, y una lista vacía.


#### Accediendo a los elementos dentro de una lista

Cada elemento dentro de una lista tiene una posición y es posible referirse a uno o alguno de estos elementos.

Para acceder a uno de estos elementos se debe numerar cada elemento de la lista desde cero, o sea el primer elemento es el elemento 0, el segundo 1, y asi sucesivamente, este número que indica la posición del elemento dentro de la lista se conoce como índice.

Para utilizar el índice, se debe indicar el número correspondiente a la posición del elemento y ubicarlo dentro de dos corchetes `[lista][n°elemento]`

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

lista_eneteros[0]
``` 
_Salida:_
**> -4**