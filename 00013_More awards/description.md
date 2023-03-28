As we just learned, accessing an element at a position equal to or greater than the size of the list will produce an `IndexError: list index out of range` error. So be careful, do not go too far! :warning:

> With this in mind, here's our final challenge: define the `medal_for` function again - do you remember it from previous lessons? -, but this time using a maximum of one `if`. Maybe now lists can help us :wink:.
>
> We remind you what the function does: it has to return the medal that corresponds to the first places in a competition.
>
>```python
>ムmedal_for(1)
>"gold"
>ムmedal_for(2)
>"silver"
>ムmedal_for(3)
>"bronze"
>ムmedal_for(4)
>"nothing"
>ムmedal_for(5)
>"nothing"
```