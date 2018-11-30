#### Operaciones sobre diccionarios.

Los diccionarios también tienen asociados un conjunto de funciones que podrían resultar útiles para manipular los datos contenidos.

#### Método update.

Es como el append de listas pero para diccionarios. Permite incluir datos dentro de un diccionario.

``` python
# definimos un diccionario
ubicacion = {'direccion' : 'Monroe 860', 'lugar' : 'Digital House' }

# agregamos un nuevo elemento al diccionario
ubicacion.update({'barrio': 'Belgrano'})

print(ubicacion)
``` 
_Salida:_
**> {'barrio': 'Belgrano', 'direccion': 'Monroe 860', 'lugar': 'Digital House'}**


¿Qué pasaría si la llave indicada en el método update ya existe en el diccionario?  
El método update actualizaría ese elemento, sobreescribiendo el valor asociado. Incluso puedo hacerlo con varios elementos a la vez. 


``` python
ubicacion.update({'barrio': 'Nuñez', 'pais': 'Argentina'})

print(ubicacion)
``` 
_Salida:_
**> {'barrio': 'Nuñez', 'direccion': 'Monroe 860', 'lugar': 'Digital House'}**



**Les propongo actualizar el siguiente diccionario con los datos de la sede de Digital House, en Brasil: Av. Dr. Cardoso de Melo, 90, Vila Olímpia, Brasil**

