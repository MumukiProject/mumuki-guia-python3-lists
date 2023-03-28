Just as there is a function to find out at which index an element is located, sometimes we need to know the opposite: which element is located at a certain position. :open_mouth:

To find it out we can use `[]`, the **indexing operator**. Just write it next to a list expression,  with the desired index within the brackets:

```python
ムmonths_of_year[0] # remember that the first element is at position 0
"January"
ム["When", "the", "last", "tree", "has", "fallen"][3]
"tree"
```

Beware of the **index**! It must be less than the list length, or bad things can happen. :astonished:

> Check it out in the console: what happens if you ask for element 0 at an empty list? Or if you ask for element 48 at `months_of_year`?
>
> When you've done, type `done()`.