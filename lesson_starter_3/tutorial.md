---
title: PyNoon Starter Lesson 3 - Tutorial
jupyter:
  nbformat: 4
  nbformat_minor: 4
  kernelspec:
     display_name: Python (Pyodide)
     language: python
     name: python3
  language_info:
     codemirror_mode:
       name: python
       version: 3
     file_extension: ".py"
     mimetype: "text/x-python"
     name: "python"
     nbconvert_exporter: "python"
     pygments_lexer: "ipython3"
     version: "3.8"
---

This tutorial will cover:

* A review of functions
* Lists
* Dictionaries

This tutorial is based on:

* [swcarpentry.github.io/python-novice-gapminder/11-lists.html](https://swcarpentry.github.io/python-novice-gapminder/11-lists.html)

> DEMO-ONLY TUTORIAL BEGINS HERE

## Functions

We're going to be using a lot of functions from Python data libraries,
so lets summarise their key facts:

**Functions are like small Python scripts that we can *call* to
perform some operation or return some value.**

**Functions are *called* using parentheses, with *arguments* inside the parentheses.**

```code
print('hello')
```

Using a function's name without parentheses refers to the function
itself *as* a value:

```code
print
```

**Functions attached to values are called *methods***

```code
'hello'.upper()
```

**Some functions take multiple arguments**

```code
round(3.14159, 2)
```

**Functions may have default values for some arguments**

`round()` defaults to rounding a number to zero decimal places:

```code
round(3.14159)
```

**Every function returns a value**

Even functions that don't seem to return a value (like `print`)
actually return a special value called `None` (similar to `null` in
SQL or other languages):

```code
returned_value = print('hello')
```

```code
returned_value
```

```code
type(returned_value)
```

**Functions accept named arguments (and some require it):**

```code
round(3.14159, ndigits=2)
```

**Use the built-in function help to get help for a function**

```code
help(round)
```

```code
help('hello'.upper)
```

**Use `dir()` and `dir(__builtins__)` to list available functions (and
non-function variables)**

```code
dir()
```

```code
dir(__builtins__)
```

> Don't worry about the underscored names

**Use `dir(some_value)` to list methods (and non-function variables
called attributes) of a value**

```code
dir('hello')
```

* See
  [docs.python.org/3/library/functions.html](https://docs.python.org/3/library/functions.html)
  for more about functions that are built-in and always available in
  Python.
* A key power of Python is that you can define your own functions as
  Python code to execute when the function is called.


> FOLLOW-ALONG TUTORIAL BEGINS HERE

* Last lesson we looked at different types of values, primarily numbers
  and strings
* This lesson we'll look at *collection* types that can store multiple
  values (even other collections)
* Specifically, we'll look at *lists* and *dictionaries*, which when
  used together are sufficient for managing data in many programming
  domains.

## Lists

* We can use a list to store an **ordered sequence** of multiple
  values
* Lists are created using *square bracket* syntax:

```code
scores = [95, 89, 64, 91]
print(scores)
```

Like strings, we can get the length of a list:

```code
len(scores)
```

Also similar to strings, we can use positional indexing and slicing to
get specific elements out of a list:

```code
print(scores[0])
print(scores[-1])
print(scores[1:2])
```

Unlike strings, we can replace the value at a specific index:

```code
scores[2] = 99
print(scores)
```

We can append an element to the end of a list with the `.append()`
method:

```code
scores.append(75)
print(scores)
```

One of the most useful things we can do with lists is to *loop* over a
list and execute some code for each elment:

```code
for score in scores:
    print('Score:', score)
    print('Score percent:', score / 100)
```

Pay careful attention to the colon at the end of the first line, and
the indented line(s) after

## Dictionaries

* *Dictionaries* are another common type of collection in Python
* Dictionaries contain a number of *keys* that are each associated
  with some other *value*.
* We create a dictionary using *curly brace* syntax:

```code
user = {'first_name': 'Bob', 'last_name': 'Smith'}
print(user)
```

> Dictionary keys are most commonly strings, but many other data types
> can also be used.

Similar to strings and lists, we can use `len()` to count the number
of key/value pairs in a dictionary:

```code
len(user)
```

Instead of indexing values within a dictionary by their positional
index, we index them by their associated key:

```code
user['first_name']
```

Similar to lists, we can update the value for a given key:

```code
user['first_name'] = 'Alice'
print(user)
```

We can also insert new key/value pairs by simply "updating" a key that
doesn't already exist in the dictionary:

```code
user['middle_name'] = 'Mallory'
print(user)
```

We can also remove an item from the dictionary with the `del` statement:

```code
del user['middle_name']
print(user)
```

Looping over a dictionary will loop over its keys:

```code
for key in user:
    print(key)
```

It is more common to use `.items()` to loop over each key/value pair:

```code
for key, value in user.items():
    print(key, value)
```

> Extra: We can also loop over the keys and values with `.keys()` and
> `.values()` respectively. These methods return list-like *iterables*
> that can be looped over, and can also be turned into proper lists by
> wrapping them with the `list()` function.

## Reducing code duplication with loops and list comprehensions

* Looping over lists can help us reduce code duplication.
* For example, take the following code that transforms several fields
  of a dictionary to lowercase:

```code
user['first_name'] = user['first_name'].lower()
user['last_name'] = user['last_name'].lower()
```

* We can loop over a list of keys, meaning we only have to define the
  transformation once.
* If we ever need to change the transformation, we only need to change
  it in once place.

```code
text_keys = ['first_name', 'last_name']

for text_key in text_keys:
    user[text_key] = user[text_key].lower()
```

* It is quite common to want to transform one list of values into
  another list of values.
* One way you might do that is as follows:

```code
names = ['Alice', 'Bob', 'Mallory']

name_lengths = []
for name in names:
    name_lengths.append(len(name))
name_lengths
```

Python's *list comprehensions* provide a more **succinct** and
**idiomatic** way to do this:

```code
names = ['Alice', 'Bob', 'Mallory']

name_lengths = [len(name) for name in names]
name_lengths
```

List comprehensions are particularly useful when we don't even want to
keep the list itself in a variable, but just to use it as an
intermediate value in some computation:

```code
names = ['Alice', 'Bob', 'Mallory']

max_name_length = max([len(name) for name in names])
max_name_length
```

List comprehensions can also be used to *filter out* items from a
list:

```code
longest_names = [
    name for name in names
    if len(name) == max_name_length
]
longest_names
```
