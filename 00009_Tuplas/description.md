## Estructura de datos: Tuplas

La tupla es una estructura de datos parecida a las listas, la diferencia es que esta estructura es inmutable, es decir que no permite las transformaciones que las listas soportan, como el **append** o el **sort**. 

En las tuplas no es posible realizar una cambio en los elementos que contiene, sin que internamente sea destruída y vuelta a construir, por lo que generalmente se suelen agrupar datos estáticos sobre esta estructura.

Además no es posible realizar una operacion de asignación como veremos al final de este enunciado.

Para definir una tupla es necesario declarar los elementos contenidos entre paréntesis y poner comas entre cada elemento dentro de la tupla

``` python
# definimos una tupla
fruta = ('manzana', 'anana', 'pera', 'banana', 'mandarina' )

# accedemos a un elemento mediante el indice
print(fruta[2])
``` 
_Salida:_
**> pera**

Tanto el indexing como el slicing se pueden realizar sobre una tupla, pero la diferencia con respecto a la lista, es que para la tupla no es posible acceder a los elementos de la tupla para asignarlos.

``` python
# definimos una tupla
fruta = ('manzana', 'anana', 'pera', 'banana', 'mandarina' )

# accedemos a un elemento mediante el indice para asignarle otro
fruta[2] = 'limon'
``` 
_Salida:_
**> TypeError: 'tuple' object does not support item assignment**