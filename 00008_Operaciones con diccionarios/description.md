#### Operaciones sobre diccionarios.

Los diccionarios también tienen asociados un conjunto de funciones que podrían resultar útiles para manipular los datos contenidos.

#### Método update.

Es como el append de listas pero para diccionarios. Permite incluir datos dentro de un diccionario.

``` python
# definimos un diccionario
ubicacion = {'direccion' : 'monroe 860', 'lugar' : 'digital_house' }

# agregamos un nuevo elemento al diccionario
ubicacion.update({'ciudad': 'CABA'})

print(ubicacion)
``` 
_Salida:_
**> {'ciudad': 'CABA', 'direccion': 'monroe 860', 'lugar': 'digital_house'}**


¿Qué pasaría si la llave indicada en el método update ya esxite en el diccionario?<br>
El método update actulizaría ese elemento, sobreescribiendo el valor asociado. Incluso puedo hacerlo con varios elementos a la vez.


``` python
# actualizamos un elemento del diccionario
ubicacion.update({'ciudad': 'La Plata', 'pais': 'Argentina'})

print(ubicacion)
``` 
_Salida:_
**> {'ciudad': 'La Plata', 'direccion': 'monroe 860', 'lugar': 'digital_house'}**



**Les propongo actualizar la lista**
