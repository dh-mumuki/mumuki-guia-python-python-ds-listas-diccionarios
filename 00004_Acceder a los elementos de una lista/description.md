Hemos visto que las listas son colecciones de elementos. Las listas se encuentran ordenadas: dentro de una lista, a cada elemento le corresponde un índice (número) que lo identifica y define su posición dentro de la colección. Las listas poseen índices con base cero: al primer elemento de la lista siempre le corresponde el índice 0, al segundo, el 1, y así sucesivamente.

Conociendo el índice de un elemento de una lista, podemos acceder a él con la siguiente sintaxis:

`lista[índice]` <br>

Veamos algunos ejemplos:

``` python
#       0  1  2  3   4    5 
print([-4, 1, 5, 10, 33, -10][3])
>10
``` 

``` python
#       0       1         2
print(['hola', 'python', 'etc'][1])
>python
``` 

Las listas pueden contener elementos de distintos tipos (valores numéricos, _strings_, etc.). Una vez que accedemos a ellos, podemos realizar normalmente cualquiera de las operaciones admitidas por cada tipo de dato. En el ejemplo que tenemos a continuación, vemos que podemos acceder a números de listas distintas a partir de sus respectivos índices y calcular su suma:

``` python
#       0  1  2  3   4    5          0  1  2  3   4    5
print([-4, 1, 5, 10, 33, -10][3] + [-4, 1, 5, 10, 33, -10][0])
> 6
``` 

De esta forma, estamos sumando el número con índice 3 de la primera lista (10) con aquel que posee índice 0 de la segunda lista (-4), y nos da como resultado 6.

También es posible definir una variable que almacene una lista y desde ahí referirse a algún elemento.

``` python
lista_enteros = [-4, 1, 5, 10, 33, -10]

print(lista_enteros[0])
> -4
``` 

El acceso a un elemento por su índice no sólo permite obtener su valor, sino que también es posible apuntar al elemento para hacer modificaciones sobre él. En el ejemplo a continuación, vemos cómo podemos reescribir el valor del primer elemento de una lista (¡recordemos que siempre tiene índice 0!):

``` python
lista_enteros = [-4, 1, 5, 10, 33, -10] # Definimos la lista

lista_enteros[0] = 100 # Accedemos al primer elemento y cambiamos su valor

print(lista_enteros) # Verificamos que la lista original se modificó
> [100, 1, 5, 10, 33, -10]
``` 

****

Además, también es posible acceder a un conjunto de los elementos de una lista. A este recurso se lo conoce como **slicing**. La sintaxis para hacer un slicing tiene esta forma: `[lista][inicio:fin:paso]`

Luego de llamar a la lista que queremos recorrer, debemos indicar a continuación, dentro de dos corchetes y separados por dos puntos,  los índices del primer elemento del slice que queremos hacer, el índice del elemento hasta el queremos llegar (no se incluye) y cuántos "pasos" daremos entre elementos (de uno en uno, de dos en dos, etc.). Algunos puntos a tener en cuenta:

1. Cuando no especificamos el punto de partida, por defecto comenzaremos el slicing por el primer elemento de la lista.
2. Cuando no especificamos el punto final, recorreremos la lista desde punto incial que hayamos definido hasta el final.
3. Si no aclaramos cuántos "pasos" damos entre los elementos, por defecto avanzaremos de a uno en uno.
4. Podemos utilizar "saltos" negativos (por ejemplo, `[lista][0:10:-1]`) para hacer un slicing de atrás hacia adelante.

Veamos algunos ejemplos:

``` python
lista_enteros = [-4, 1, 5, 10, 33, -10]

#       lista[inicio:fin:salto]
print(lista_enteros[0:5:1])
> [-4, 1, 5, 10, 33]

print(lista_enteros[2:])
> [5, 10, 33, -10]

print(lista_enteros[:2:-1])
> [-10, 33, 10]
``` 
<br>
> :memo: **Dada esta lista: <br>
      varios = [1, a, 2, b, 3, c, 4, d, 5, e] <br>
Definí listas que contengan:**<br>
1. Todos los números de la lista<br>
2. Todas todas las letras de la lista. <br>
3. Las letras vocales que aparecen en la lista. <br>
4. Todos los números primos de la lista. <br>
5. La misma lista pero en el orden inverso [e, 5, d...
<br>
