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
Cada elemento dentro de la lista debe ir separado por comas, esa es la forma en que se delimita una posición en una lista.

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

En éste último slice no se observa el elemento -10 que ocupa la posición 5, esto es porque el último elemento señalado no se incluye.

A continuación otro ejemplo de slicing.

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

El modo de uso es **lista.append(elemento_nuevo)**, entonces el **"append"** toma el **"elemento_nuevo"** y lo incluye en la última posición de **"lista"**

``` python
lista_enteros = [1, 2, 3]

lista_enteros.append(5)

lista_enteros
``` 
_Salida:_
**> [1, 2, 3, 5]**

Otra demostración

``` python
# definimos una lista vacía 
lista_1 = []

lista_1.append('hola')

lista_1.append(33)

lista_1
``` 
_Salida:_
**> ['hola', 33]**

En este útimo caso, inicializamos una lista vacía e invocamos el método append para poblar esa lista, a veces es necesario obtener una lista vacía, cuando veamos los iteradores vamos a conocer la importancia de este recurso.

#### Método sort.

El método sort permite ordenar los elementos de la lista según un criterio, para eso, los elementos deben tener un comparador interno que permita llevar adelante el ordenamiento, en el caso de los números, este comparador se encuentra definido, pero podría no estarlo para otro tipo de datos.

``` python
lista_enteros = [3, 2, 2.5,  5]

lista_enteros.sort()

lista_enteros
``` 
_Salida:_
**> [2, 2.5, 3, 5]**

#### Método remove 

Este método permite buscar un elemento dado, si el elemento existe, entonces lo quita de la lista.

``` python
lista_enteros = [3, 2, 2.5,  5]

lista_enteros.remove(2)

lista_enteros
``` 
_Salida:_
**> [3, 2, 2.5,  5]**


## Estructura de datos: Diccionario

Los diccionarios al igual que las listas, permiten mantener elementos dentro de una estructura, pero a diferencia de las listas, los elementos dentro de un diccionario no poseen un orden de precedencia intencionado, esto significa, que uno no suele acceder a los elementos con un índice de posición, en los diccionarios se accede por una **llave**.

Una **llave** debe ser un tipo string o numérico, y no debe estar repetido, ya que se definió que para cada elemento dentro del diccionario debe existir una **llave** única.

A continuación vemos algunas formas de definir diccionarios.

``` python

masa = {'auto': 3000, 'bicleta': 22, 'perro': 5 }

ubicacion = {'direccion' : 'monroe 860', 'lugar' : 'digital_house' }

vacio = {}

```

Para referirnos a un elemento del diccionario debemos utilizar la **llave** para el que ese elemento fue asignado.



#### Operaciones sobre diccionarios.

Los diccionarios también tienen asociados un conjunto de funciones que podrían resultar útiles para manipular los datos contenidos.

#### Método update.

Es como el append de listas pero para diccionarios, permite incluir datos dentro de un diccionario.

``` python
# definimos un diccionario
ubicacion = {'direccion' : 'monroe 860', 'lugar' : 'digital_house' }

# agregamos un nuevo elemento al diccionario
ubicacion.update({'ciudad': 'CABA'})

print(ubicacion)
``` 
_Salida:_
**> {'ciudad': 'CABA', 'direccion': 'monroe 860', 'lugar': 'digital_house'}**




## Estructura de datos: Tuplas

