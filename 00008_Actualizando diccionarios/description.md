Los diccionarios tienen asociados un conjunto de funciones que resultan útiles para manipular los datos contenidos. Te presentamos a continuación el método `update()`, que permite incluir nuevos elementos o actualizar los valores de los preexistentes:

``` python
# definimos un diccionario
ubicacion = {'direccion' : 'Monroe 860', 'lugar' : 'Digital House'}

# agregamos un nuevo elemento al diccionario
ubicacion.update({'barrio': 'Belgrano'})

print(ubicacion)

ム
> {'barrio': 'Belgrano', 'direccion': 'Monroe 860', 'lugar': 'Digital House'}
``` 

¿Qué pasaría si la clave indicada en el método `update()` ya existe en el diccionario?  
El método actualizaría ese elemento, sobreescribiendo el valor asociado. Incluso, puede hacerse con varios elementos a la vez. 

``` python
ubicacion.update({'barrio': 'Nuñez', 'pais': 'Argentina'})
print(ubicacion)

ム
> {'barrio': 'Nuñez', 'direccion': 'Monroe 860', 'lugar': 'Digital House'}
``` 

> :memo: **Te propongo actualizar el siguiente diccionario con los datos de la sede de Digital House en Brasil: Av. Dr. Cardoso de Melo, 90, Vila Olímpia. Sería buena idea agregar el país, ya que esa información no está contenida en el diccionario.**
