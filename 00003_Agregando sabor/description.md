Las listas son muy útiles para contener múltiples elementos. ¡Pero hay más! También podemos agregarle elementos en cualquier momento, utilizando la función `list.append`, que recibe dos parámetros: la lista y el elemento. Por ejemplo:

```python
pertenencias = ["espada", "escudo", "antorcha"]
# len(pertenencias) devuelve 3

list.append(pertenencias, "amuleto")
# ahora len(pertenencias) devuelve 4
```

Como vemos, `list.append` agrega un elemento a la lista, lo cual hace que su tamaño aumente. ¿Pero en qué parte de la lista lo agrega? ¿Al principio? ¿Al final? ¿En el medio?

> Averigualo vos mismo: inspeccioná en la consola qué elementos contiene `pertenencias`, agregale una `"ballesta"` y volvé a inspeccionar `pertenencias`.
>
> Además existe una función `list.remove`, que recibe por parámetro una lista y un elemento de ella. Investigá en la consola qué hace. :eyes:
