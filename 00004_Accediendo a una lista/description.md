#### Accediendo a los elementos dentro de una lista

Cada elemento dentro de una lista tiene una posición y es posible referirse a uno o algunos de estos elementos.

Para acceder a uno de estos elementos se debe:
  
  * numerar cada elemento de la lista desde cero, o sea el primer elemento es el elemento 0, el segundo 1, y asi sucesivamente, este número que indica la posición del elemento dentro de la lista, se conoce como índice.

  * indicar éste índice dentro de dos corchetes `lista[índice]`

``` python
#       0  1  2  3   4    5
print([-4, 1, 5, 10, 33, -10][3])
``` 
_Salida:_
**> 10**

``` python
#       0       1         2
print(['hola', 'python', 'etc'][1])
``` 
_Salida:_
**> python**

Al momento de acceder a un elemento de la lista, podemos utilizarlo como el tipo de datos que es.

``` python
#       0  1  2  3   4    5          0  1  2  3   4    5
print([-4, 1, 5, 10, 33, -10][3] + [-4, 1, 5, 10, 33, -10][0])
``` 
_Salida:_
**> 6**

Como podemos observar en esta última demostración, es posible sumar ambos números refiriendonos a ellos desde una lista.

Es posible asignar a una nombre a una lista, y desde ahi, referirse a algún elemento.

``` python
lista_enteros = [-4, 1, 5, 10, 33, -10]

print(lista_enteros[0])
``` 
_Salida:_
**> -4**

Pero el acceso a los elementos por el índice no solo permiten recuperar al elemento, sino que tambien es posible apuntar al elemento para hacer modificaciones sobre él.

``` python
lista_enteros = [-4, 1, 5, 10, 33, -10]

lista_enteros[0] = 100

print(lista_enteros)
``` 
_Salida:_
**> [100, 1, 5, 10, 33, -10]**


Como habíamos comentado también es posible acceder a un conjunto de éstos elementos, a este recurso se le conoce como slicing, para hacer un slicing debemos indicar dentro de dos corchetes y separado por dos puntos,  el elemento de inicio, el de final (no se incluye) y el salto, `[lista][inicio:fin:salto]`, veamos algunos ejemplos

``` python
lista_enteros = [-4, 1, 5, 10, 33, -10]

#       lista[inicio:fin:salto]
print(lista_enteros[0:5:1])
``` 
_Salida:_
**> [-4, 1, 5, 10, 33]**

A diferencia del llamado al índice, el slicing devuelve una sublista de elementos.

En éste último slice no se observa el elemento -10 que ocupa la posición 5, esto es porque el último elemento señalado no se incluye.

A continuación otro ejemplo de slicing.

``` python
lista_enteros = [-4, 1, 5, 10, 33, -10]

print(lista_enteros[0:5:2])
``` 
_Salida:_
**> [-4, 5, 33]**