Para acceder a uno de estos elementos se debe:
  
  * Numerar cada elemento de la lista desde cero. El primer elemento es el elemento 0, el segundo 1, y así sucesivamente. Este número que indica la posición del elemento dentro de la lista, se conoce como **índice.**

  * Indicar éste índice dentro de dos corchetes `lista[índice]` <br>

Veamos un ejemplo:

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

Al momento de acceder a un elemento de la lista también podemos utilizarlo como en el ejemplo que se muestra a continuación, donde se realiza una operación indicando los números que debe sumar mediante la utilización del índice. 

``` python
#       0  1  2  3   4    5          0  1  2  3   4    5
print([-4, 1, 5, 10, 33, -10][3] + [-4, 1, 5, 10, 33, -10][0])
> 6
``` 

De esta forma estamos sumando el número de la posición 3 (10) con el de la posición 0 (-4) y nos da como resultado 6.

También es posible asignar un nombre a una lista y desde ahí referirse a algún elemento.

``` python
lista_enteros = [-4, 1, 5, 10, 33, -10]

print(lista_enteros[0])
> -4
``` 

El acceso a los elementos por el índice no solo permite recuperar el elemento, sino que también es posible apuntar al elemento para hacer modificaciones sobre él.

``` python
lista_enteros = [-4, 1, 5, 10, 33, -10]

lista_enteros[0] = 100

print(lista_enteros)
> [100, 1, 5, 10, 33, -10]
``` 

****


Además, también es posible acceder a un conjunto de estos elementos. A este recurso se le conoce como **slicing**. Para hacer un slicing debemos indicar dentro de dos corchetes y separado por dos puntos, en primer lugar el elemento de inicio, el de final (no se incluye) y el paso, `[lista][inicio:fin:paso]`. Esto último, indica de cuánto en cuanto se avanza adentro de la lista. Veamos algunos ejemplos

``` python
lista_enteros = [-4, 1, 5, 10, 33, -10]

#       lista[inicio:fin:salto]
print(lista_enteros[0:5:1])
> [-4, 1, 5, 10, 33]
``` 

<br>
> :memo: **Dada esta lista varios = [1, a, 2, b, 3, c, 4, d, 5, e] <br>
Imprimir una lista que contenga:**<br>
1. Todos los números de la lista<br>
2. Todas todas las letras de la lista. <br>
3. Las letras vocales que aparecen en la lista. <br>
4. Todos los números primos de la lista. <br>
5. La misma lista pero en el orden inverso [e, 5, d...
<br>
