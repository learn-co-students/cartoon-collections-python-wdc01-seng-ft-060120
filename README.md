

## Objectives

You're going to get familiar with iterating through arrays.

## Instructions

There are four functions to complete in this lab:

1. Dwarf Roll Call
2. Summon Captain Planet
3. Long Planeteer Calls
4. Find the Cheese

#### Function 1 - Dwarf Roll Call

![dwarves](https://s3-us-west-2.amazonaws.com/web-dev-readme-photos/cartoon-collections/dwarves.jpg)

This function should accept a list of dwarf names, for instance:

```python
["Doc", "Dopey", "Bashful", "Grumpy"]
```

It should then print out each name using `print`. The print-out should look like this:

> 1. Doc
> 2. Dopey
> 3. Bashful
> 4. Grumpy

Look into [for loops](https://wiki.python.org/moin/ForLoop) and [enumerate()](https://docs.python.org/3/library/functions.html#enumerate)

Once the test for this function is passing, move on to the next function.

#### Function 2 - Summon Captain Planet

![captain-planet](https://s3-us-west-2.amazonaws.com/web-dev-readme-photos/cartoon-collections/captain-planet.jpeg)

This function should accept an array of planeteer calls, like this:

```python
planeteer_calls = ["earth", "wind", "fire", "water", "heart"]
```

It should then capitalize each element and add an exclamation point at the end. The return value of this function should be an array. Example:

```python
summon_captain_planet(planeteer_calls)
#=> ["Earth!", "Wind!", "Fire!", "Water!", "Heart!"]
```

The `map` function or list comprehensions might be appropriate for this task, take a look at them [here](http://www.dotnetperls.com/map) and [here](http://www.dotnetperls.com/list-python).

Once the test for this function is passing, move on to the next function, long planeteer calls.

#### Function 3 - Long Planeteer Calls

The `long_planeteer_calls` function should accept an array of calls. The function should tell us if any of the calls are longer than four characters. For example:

```python
short_words = ["puff", "go", "two"]
long_planeteer_calls(short_words)
#=> False

assorted_words = ["two", "go", "industrious", "bop"]
long_planeteer_calls(assorted_words)
#=> True
```

Notice the return value of this function is either `False` or `True`, depending on the array it was given as an argument.

Checkout the [Python docs on lists](https://docs.python.org/3/tutorial/datastructures.html) for a hint.

Once the test for this function is passing, move on to the last function.

#### Function 4 - Find the Cheese

![dancing-mice](https://s3-us-west-2.amazonaws.com/web-dev-readme-photos/cartoon-collections/cheese.jpg)

The "find_the_cheese" function should accept a list of strings. It should then look through these strings and return the first string the is a type of cheese. The types of cheese that appear are **cheddar**, **gouda**, and **camembert**.

For example:

```python

snacks = ["crackers", "gouda", "thyme"]
find_the_cheese(snacks)
#=> "gouda"

soup = ["tomato soup", "cheddar", "oyster crackers", "gouda"]
find_the_cheese(soup)
#=> "cheddar"
```

If, sadly, a list of ingredients does not include cheese, return `None`:

```python
ingredients = ["garlic", "rosemary", "bread"]
find_the_cheese(ingredients)
#=> None
```

You can assume that all strings will be lower-case. Take a look a the [include]() function for a hint. Your `find_the_cheese` function  should return a string value - not print it. Keep that in mind!

## Resources

* [Programming Ruby 1.9](http://books.flatironschool.com/books/11?page=459) - [Enumerable](http://books.flatironschool.com/books/11?page=459), page 459
