**La tupla** es una estructura de datos parecida a las listas. La diferencia es que esta estructura es inmutable, es decir, no permite las transformaciones que las listas soportan.  

En las tuplas no es posible realizar un cambio en los elementos que contiene sin que internamente sea destruída y vuelta a construir. Por lo cual, generalmente se suelen agrupar datos estáticos sobre esta estructura. Además no es posible realizar una operacion de asignación como veremos al final de este enunciado.

Para definir una tupla es necesario declarar los elementos contenidos entre paréntesis y poner comas entre cada elemento dentro de la tupla.
Veamos un ejemplo:

``` python
# definimos una tupla
fruta = ('manzana', 'anana', 'pera', 'banana', 'mandarina' )

# accedemos a un elemento mediante el índice
print(fruta[2])

ム
> pera 
``` 

Tanto el indexing como el slicing se pueden realizar sobre una tupla pero la diferencia con respecto a la lista es que, para la tupla, no es posible acceder a los elementos para asignarlos.
Veamos qué pasa hacemos esto:

``` python
# definimos una tupla
fruta = ('manzana', 'anana', 'pera', 'banana', 'mandarina' )

# accedemos a un elemento mediante el indice para asignarle otro
fruta[2] = 'limón'

ム
> TypeError: 'tuple' object does not support item assignment
``` 
<br>

> :memo:**Creá un tupla con cinco verduras, donde el tomate este en la segunda posición. Luego, imprimí esa verdura.**