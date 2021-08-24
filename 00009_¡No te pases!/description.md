Así como existe una función para averiguar en qué posición está un elemento, también puede ocurrir que queramos saber lo contrario: qué elemento está en una cierta posición. :open_mouth:

Para averiguarlo podemos usar el **operador de indexación**, escribiendo después de la colección y entre corchetes `[]` la posición que queremos para averiguar:

```python
ム meses_del_anio[0] # recordá que el primer elemento está en la posición 0
"enero"
ム ["ese", "perro", "tiene", "la", "cola", "peluda"][1]
"perro"
```

¡Ojo! El número que le pases, formalmente llamado **índice**, debe ser menor a la longitud de la lista, o cosas malas pueden suceder. :astonished:

> Probalo en la consola: ¿qué sucede si le pedís el elemento 0 a una lista vacía? ¿O si le pedís el elemento 48 a los `meses_del_anio`?
>
> Cuando hayas hecho las pruebas escribí `listo()`. 
