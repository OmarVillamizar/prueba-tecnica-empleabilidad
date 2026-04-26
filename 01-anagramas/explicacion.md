# Explicación algoritmo de agrupamiento de anagramas

## Solución
Usé sorted() para que palabras diferentes (como "roma" y "amor") consigan una llave en común que permita agruparlas.
Luego en base a su llave, se van acumulando en el diccionario, en el caso de no existir, se agrega como posiblidad nueva.
Finalmente con el .values() extraemos solo los datos de los valores que solicitan en el output.

## Complejidad

### Tiempo
O(n)
### Espacio
O(n)
## Test unitarios
Tuve que explorar el uso de PYTEST, ya que nunca habia realizado test unitarios para mi código, realmente me ayude de la IA para crear 10 casos de prueba y ponerlo a prueba, como resultado he aprendido la estructura y el uso de pytest, y he obtenido 10/10 casos de prueba aprobados.