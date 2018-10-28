## Estructura de datos: Diccionario

Los diccionarios al igual que las listas, permiten mantener elementos dentro de una estructura, pero a diferencia de las listas, los elementos dentro de un diccionario no poseen un orden de precedencia intencionado, esto significa, que uno no suele acceder a los elementos con un índice de posición, en los diccionarios se accede por una **llave**.

Una **llave** debe ser un tipo string o numérico, y no debe estar repetido, ya que se definió que para cada elemento dentro del diccionario debe existir una **llave** única.

A continuación vemos algunas formas de definir diccionarios.

``` python

masa = {'auto': 3000, 'bicleta': 22, 'perro': 5 }

ubicacion = {'direccion' : 'monroe 860', 'lugar' : 'digital_house' }

vacio = {}
```

Para referirnos a un elemento del diccionario debemos utilizar la **llave** para el que ese elemento fue asignado.

``` python
ubicacion = {'direccion' : 'monroe 860', 'lugar' : 'digital_house' }

print(ubicacion['direccion'])
```
_Salida:_
**> monroe 860**


¿Que imprime el siguiente código?

``` python
mi_diccionario = { 'llave1': 1, 'llave2': 2, 'llave3':3 } 

print(mi_diccionario[2])

```
