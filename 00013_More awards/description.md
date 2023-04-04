As we just learned, accessing an element at a position equal to or greater than the size of the list will produce an `IndexError: list index out of range` error. So be careful, do not go too far! :warning:

> 🏆 Here's our final challenge: define the `medal_for` function again - do you remember it from previous lessons? -, but this time use one `if` at most. Maybe now lists can help us.
>
> :thought_balloon: We remind you what `medal_for` does: it returns the medal that corresponds to the first places in a competition.
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