Ya hemos visto dos tipos de colecciones de datos, las listas y los diccionarios. Ahora, presentaremos las **tuplas**.

La tupla es una estructura de datos parecida a las listas. Para definir una tupla es necesario declararla entre paréntesis. Al igual que en las listas, los elementos dentro de una tupla se separan con comas, y podemos acceder a ellos a partir de su índice o haciendo slicing.

Veamos un ejemplo:

``` python
# definimos una tupla
frutas = ('manzana', 'anana', 'pera', 'banana', 'mandarina')

# accedemos a un elemento mediante su índice
print(frutas[2])

ム
> pera 

# accedemos a varios elementos mediante slicing
print(frutas[0:3])

ム
> ('manzana', 'anana', 'pera') 
```

Hasta aquí, nada nuevo. Pero, entonces, ¿qué distingue a las tuplas de las listas? La principal diferencia es que las tuplas son inmutables, es decir, no permiten las transformaciones que las listas sí soportan.

En las tuplas no es posible realizar un cambio en sus elementos sin que internamente sean destruídas y vueltas a construir. Por lo cual, generalmente se suelen agrupar datos estáticos en estas estructuras, que sabemos que no vamos a necesitar modificar. Por otra parte, tampoco es posible realizar una operacion de asignación, como vemos a continuación.

¿Qué pasa si queremos reescribir el valor de un elemento de una tupla?

``` python
# definimos una tupla
frutas = ('manzana', 'anana', 'pera', 'banana', 'mandarina')

# accedemos a un elemento mediante su índice para asignarle otro valor
frutas[2] = 'limón'

ム
> TypeError: 'tuple' object does not support item assignment
``` 
<br>

> :memo: **Creá una tupla con cinco verduras, donde la lechuga esté en la segunda posición. Luego, imprimí esa verdura.**