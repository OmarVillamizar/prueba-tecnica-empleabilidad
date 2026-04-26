# Explicación de algoreitmo de customer queue

## Solución
Creé un diccionario donde cada llave es un nivel de prioridad (1, 2, 3) y cada valor es una lista (cola).
Al hacer enqueue, el cliente se guarda directo en su nivel de prioridad correspondiente.
Para el dequeue, el algoritmo barre las prioridades en orden (de 1 a 3); en cuanto encuentra a alguien, lo saca para ser atendido con .pop(0) para respetar que el primero en llegar sea el primero en salir dentro de su mismo nivel de prioridad.

## Complejidad

### Tiempo
O(n)
### Espacio
O(n)
## Test unitarios
Nuevamente lo enfrente a 10 test creados en PYTEST por la IA para poner a prueba mi algoritmo, como resultado 9/10 test acertados, obteniendo error en el caso de prueba 9, el cual validaba la inserción de una prioridad errada (nivel 4), pero mi algoritmo esta hecho para trabajar con los 3 niveles de prioridad descritos, por lo tanto se comporto como deberia y no acepto este caso de prueba, lo veo como un comportamiento normal dentro de los lineamientos del ejercicio.