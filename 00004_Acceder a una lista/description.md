#### Accediendo a los elementos dentro de una lista

Cada elemento dentro de una lista tiene una posición y es posible referirse a uno o algunos de estos elementos.

Para acceder a uno de estos elementos se debe:
  
  * Numerar cada elemento de la lista desde cero. El primer elemento es el elemento 0, el segundo 1, y así sucesivamente. Este número que indica la posición del elemento dentro de la lista, se conoce como índice.

  * Indicar éste índice dentro de dos corchetes `lista[índice]`

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

Al momento de acceder a un elemento de la lista podemos utilizarlo como en el ejemplo, donde se realiza una operación indicando los números que debe sumar mediante la utilización del índice. 

``` python
#       0  1  2  3   4    5          0  1  2  3   4    5
print([-4, 1, 5, 10, 33, -10][3] + [-4, 1, 5, 10, 33, -10][0])
``` 
_Salida:_
**> 6**

De esta forma estamos sumando el número de la posición 3 (10) con el de la posición 0 (-4) y nos da como resultdo 6.

Es posible asignar un nombre a una lista y desde ahi referirse a algún elemento.

``` python
lista_enteros = [-4, 1, 5, 10, 33, -10]

print(lista_enteros[0])
``` 
_Salida:_
**> -4**

Pero el acceso a los elementos por el índice no solo permite recuperar el elemento, sino que también es posible apuntar al elemento para hacer modificaciones sobre él.

``` python
lista_enteros = [-4, 1, 5, 10, 33, -10]

lista_enteros[0] = 100

print(lista_enteros)
``` 
_Salida:_
**> [100, 1, 5, 10, 33, -10]**


Como habíamos comentado, también es posible acceder a un conjunto de estos elementos. A este recurso se le conoce como **slicing**, para hacer un slicing debemos indicar dentro de dos corchetes y separado por dos puntos. El elemento de inicio, el de final (no se incluye) y el paso, `[lista][inicio:fin:paso]`. Esto último, indica de cuánto en cuanto se avanza adentro de la lista. Veamos algunos ejemplos

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

En este ejemplo se observa que el paso es de dos en dos, por eso no incluye los elementos 1, 10 y -10. 

<br>
**Dada esta lista varios = [1, a, 2, b, 3, c, 4, d, 5, e], imprimir una lista que contenga:**
1. Todos los números
2. Todas todas las letras de la lista.
3. Las letras vocales.
4. Todos los números primos.
5. BONUS --> la misma lista pero en el orden inverso [e, 5, d...
