¿Por qué importa el orden en que pongamos las expresiones?

Recordemos un poco lo que vimos en la lección de lógica booleana. Para que el operador `or` nos de `True` solo basta con que una de las condiciones sea verdadera. Por lo tanto: si preguntamos primero por la posición de la serie en el ranking, y la serie no está en la lista, nuestro código explota. :boom:

Si en cambio preguntamos si la serie es parte del ranking primero, solo vamos a preguntar por su posición cuando sabemos que está en la lista (porque `not serie in ranking` dio `False`). :open_mouth: