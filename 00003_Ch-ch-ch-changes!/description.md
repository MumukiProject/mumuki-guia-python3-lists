Lists are really useful for treating multiple items as a whole. But there is more! We can also add elements to them at any time, using the `list.append` procedure, which takes two parameters: the list and the element. For example:

```python
ムdiscs = ["Serú Girán", "Artaud", "Almendra", "Quebrado"]
ムlen(discs)
4
ムlist.append(discs, "Vida")
ムlen(discs)
5
```

As we see, `list.append` adds an element to the list, which increases its size. But where in the list is it added? At first? In the end? In the middle? :thinking:

> Find out for yourself: inspect in the console what elements `books` contains, add `"Insomnia"` to it and inspect `books` again.
>
> There is also a procedure `list.remove`, which takes as a parameter a list and an element of it. Check in the console what it does. :eyes:
>
>When you're done, type `done()`.