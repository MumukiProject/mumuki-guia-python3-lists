Como vimos, al pedir un elemento en una posición igual o mayor al tamaño de la lista, se va a producir un error `IndexError: list index out of range`. Así que ¡ojo, no te pases de índice! :warning:

> Teniendo esto en cuenta, va un desafío: definí nuevamente la función `medalla_segun_puesto`, pero esta vez usando como máximo un único `if`. Quizás las listas te pueden ser útiles acá :wink:.
>
> Te recordamos qué hace la función: tiene que retornar la medalla que le corresponde a los primeros puestos de una competencia.
>
>```python
>ム medalla_segun_puesto(1)
>"oro"
>ム medalla_segun_puesto(2)
>"plata"
>ム medalla_segun_puesto(3)
>"bronce"
>ム medalla_segun_puesto(4)
>"nada"
>ム medalla_segun_puesto(5)
>"nada" 
```
