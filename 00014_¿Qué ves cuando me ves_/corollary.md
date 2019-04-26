¿Por qué tuvimos que poner las expresiones en ese orden específico?

* Si preguntábamos primero por la posición de la serie en el ranking, y la serie no estaba en la lista, nuestro código iba a explotar. :boom:
* En cambio, como lo hicimos, si la serie no está en el ranking (`not serie in ranking`) no hace falta preguntar su posición, porque ya sabemos que toda esa expresión es verdadera.

Recordemos que para que el operador `or` nos devuelva `True` alcanza con que una de las condiciones sea verdadera. Si la primera es verdadera, ¿para qué va a preguntar por la segunda? :sweat_smile: