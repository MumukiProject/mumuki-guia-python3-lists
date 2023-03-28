_:baby: Where is itemmy?_

Another thing we want to do with lists is to find out the position at the first occurrence of a given item. To do this we use the `list.index` function as follows:

```python
ムlist.index(["I", "call", "the", "big", "one", "Bitey"], "call")
1
ムlist.index(["I", "call", "the", "big", "one", "Bitey"], "Bitey")
5
ムbusiness_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
ムlist.index(business_days, "Monday")
0
```

As you can see, the curious thing about this function is that it seems to always return one less than expected. For example, the word `"call"` appears second, not first; and `"Monday"` is the first business day, not zero. :bug: Is it a bug from Python creators? :confused:

Nope! :sweat_smile: In Python, as in many other languages, list _indexes_ start at 0: the first element is at position 0, the second at position 1, the third at position 2, and so on.

> And what happens if you pass as an argument an element to `list.index` that our list doesn't have? Find it out!
>
> Try the following:
>
> ```python
> ムlist.index(business_days, "Funday")
> ```
