Los diccionarios, al igual que las listas, permiten ordenar elementos dentro de una estructura. Pero a diferencia de estas, los elementos dentro de un diccionario no poseen un orden. Esto significa que para acceder a los elementos de un diccionario no se usa un índice de posición sino que se accede por una **llave**.

Una **llave** puede ser de tipo string o numérico y no debe estar repetida, ya que se definió que para cada elemento dentro del diccionario debe existir una **llave** única.

A continuación te mostramos algunas formas de definir diccionarios:

``` python
ruedas = {'auto': 4, 'bicicleta': 2, 'triciclo': 3 }
ubicacion = {'direccion' : 'monroe 860', 'lugar' : 'digital_house' }
vacio = {}
```
Para referirnos a un elemento del diccionario debemos utilizar la **llave** para el que ese elemento fue asignado.

``` python
ubicacion = {'direccion' : 'monroe 860', 'lugar' : 'digital_house' }
print(ubicacion['direccion'])

ム
> monroe 860
```

>  :memo: **Escribí un diccionario que tenga como llave nombre, apellido y mail. Luego completalo con tus datos** 