Why did we have to put the expressions in this particular order?

* If we first asked for the series position in the ranking, and the series was not in the list, our code would explode :boom:
* On the other hand, as we did, if the series is not in the ranking (`not series in ranking`) it is not necessary to ask its position, because we already know that all that expression is true.

Remember that for the `or` operator to return `True`, it is enough for one of the conditions to be true. If the first is true, why would you ask about the second? :sweat_smile:
