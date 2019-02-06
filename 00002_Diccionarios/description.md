Los diccionarios, al igual que las listas, permiten agrupar elementos dentro de una estructura. Pero a diferencia de estas, los elementos dentro de un diccionario no poseen un orden. Los diccionarios se definen con llaves ({}). Dentro de un diccionario, los elementos se expresan como **pares clave:valor**.

A continuación te mostramos cómo definir algunos diccionarios:

``` python
ruedas = {'auto': 4, 'bicicleta': 2, 'triciclo': 3}
ubicacion = {'direccion' : 'monroe 860', 'lugar' : 'digital_house'}
vacio = {}
```
Las **claves** pueden ser de tipo _string_ o numéricas y no deben estar repetidas, ya que se definió que para cada valor dentro de un diccionario debe existir una clave única.

A diferencia de las listas, los elementos dentro de un diccionario no poseen un orden. Esto significa que para acceder a los valores de un diccionario no se usa un índice de posición, sino que se accede por sus claves.

``` python
ubicacion = {'direccion' : 'monroe 860', 'lugar' : 'digital_house'}
print(ubicacion['direccion'])

ム
> monroe 860
```

>  :memo: **Escribí un diccionario que tenga como claves nombre, apellido y mail. Luego, completalo con tus datos** 