#### Método append.

Este método se utiliza para agregar un elemento al final de una lista.

El modo de uso es **lista.append(elemento_nuevo)**, entonces el **"append"** toma el **"elemento_nuevo"** y lo incluye en la última posición de **"lista"**

``` python
lista_enteros = [1, 2, 3]

lista_enteros.append(5)

print(lista_enteros)
``` 
_Salida:_
**> [1, 2, 3, 5]**

Otra demostración

``` python
# definimos una lista vacía 
lista_1 = []

lista_1.append('hola')

lista_1.append(33)

print(lista_1)
``` 
_Salida:_
**> ['hola', 33]**

En este útimo caso, inicializamos una lista vacía e invocamos el método append para poblar esa lista. A veces es necesario obtener una lista vacía, cuando veamos los iteradores vamos a conocer la importancia de este recurso.


¿Que resultado esta contenido en la variable **mi_lista** después de la ejecución?

``` python
mi_lista = [0, 1, 3]

mi_lista.append([3, 4])

```