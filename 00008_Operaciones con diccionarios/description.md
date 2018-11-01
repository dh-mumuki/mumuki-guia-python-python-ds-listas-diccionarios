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
