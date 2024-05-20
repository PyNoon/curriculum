---
title: PyNoon Starter Lesson 2 - Tutorial
jupyter:
  nbformat: 4
  nbformat_minor: 4
  kernelspec:
     display_name: Python (Pyodide)
     language: python
     name: python
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

This tutorial is based on:

* [swcarpentry.github.io/python-novice-gapminder/02-variables.html](https://swcarpentry.github.io/python-novice-gapminder/02-variables.html)
* [swcarpentry.github.io/python-novice-gapminder/03-types-conversion.html](https://swcarpentry.github.io/python-novice-gapminder/03-types-conversion.html).

> DEMO-ONLY TUTORIAL BEGINS HERE

## Types

**In Python, every value has a type**

**The type of a value determines what operations we can perform with it**

### Checking the type of a value

We can use the `type()` function to find out what it is:

```code
type(42)
```

An `int` or "integer" is a number without a decimal part.

```code
type(42.0)
```

`float` is the name Python and other programming languages use for
numbers with decimal parts (aka floating point numbers).

```code
type('hello')
```

A `str` or "string" is a string of characters - a piece of text.

### Operations vary by type

The type of a value determines what operations we can perform with it:

```code
'hello' + 'world'
```

Note that "adding" strings joins them together, while we've seen that
adding numbers performs arithmetic addition.

What if we try to subtract strings?

```code
'hello' - 'h'
```

Python complains with a `TypeError`, telling us that the `-` operation
is not supported for strings.

We can get the length of a string with the `len()` function:

```code
len('hello')
```

But the length of an integer is not defined:

```code
len(10)
```

Different types also support different variables and functions
attached to the value itself:

```code
'hello'.upper()
```

`upper()` is a function like `print`, `type`, and `len`, but it
doesn't take any arguments, and it is attached to string values
(referred to as a special kind of function called a *method*).


### Operations with mixed types

Some operations do not work with mixed types:

```code
1 + '1'
```

Functions are available to convert values from one type to another,
like `str()` to convert values to strings:

```code
str(1) + '1'
```

Some operations do work with mixed types

```code
'<>' * 10
```

What do you think the result of this will be?

```code
type(42 + 42.0)
```

Maths with both integers and floats results in a `float`. Note the
decimal part after the resulting number:

```code
42 + 42.0
```

> FOLLOW-ALONG TUTORIAL BEGINS HERE

## Setup

* Make a new notebook for this lesson
* What's the first thing to do? RENAME IT!
* Name it `pynoon_starter_2.ipynb`

## Variables

A quick recap on variables for those who haven't reached that part of
futurecoder yet. Run the following:

```code
height_cm = 180
```

The `=` symbol assigns the name on the left to refer to the value on
the right.

Now we can use the variable anywhere we would have used the value:

```code
height_cm
```

```code
height_cm + 10
```

> Note: The Python convention for naming variables is to use "snake
> case" (lowercase letters separated with words/parts separated by
> underscores).

> Note: Variables are case-sensitive.

**Variables are useful for giving meaningful names to values:**

This is bad:

```code
height_cm / 2.54
```

This is better:

```code
cm_per_inch = 2.54
height_cm / cm_per_inch
```

Also note how helpful it is to include the units in the name of the
variable.

**Variables are also useful for storing the result of an operation for later use:**

```code
cm_per_inch = 2.54
height_inch = height_cm / cm_per_inch
```

<!-- * Be careful of cell order: -->
<!--   * Move `print(first_name)` above `first_name = 'Alice'` -->
<!--   * The print cell still works for now... -->
<!--   * `Restart and run all` -->
<!-- * Be aware that the variable does not refer to a dynamic calculation, it refers -->
<!--   to a value: -->
<!--   ``` -->
<!--   a = 2 -->
<!--   b = 5 * a -->
<!--   a = 3 -->
<!--   print(a) -->
<!--   print(b) -->
<!--   ``` -->


## Indexing and Slicing

### Indexing

We can use indexing to get particular characters from a string:

```code
email = 'pynoon@example.com'
email
```

To get a new string containing only the first character of the `email`
string:

```code
email[0]
```

Note that Python starts counting indexes at `0`, so index `1` is the
second character:

```code
email[1]
```

You can also specify negative indexes to count from the end of the
string:

```code
email[-1]
```

### Slicing

We can use slicing to get a new string that is a subset of the target
string:

```code
email[0:2]
```

* The result of the slice **includes** the first index, and **excludes**
  the last index.
* The length of the slice is the difference of the two indexes.

Taking an index or slice does not change the contents of the original
string, but returns a copy of part of the string:

```code
email
```

Here's a more concrete example to split an email address around it's
`@` sign.

We can use the `find()` method supported by strings to get the index
of the first `@` sign:

```code
at_index = email.find('@')
```

```code
at_index
```

We can then use that index to slice the string:

```code
email[at_index]
```

```code
email[0:at_index]
```

```code
email[at_index:len(email)]
```

```code
email[(at_index + 1):len(email)]
```


### DataFrames

More generally, indexing and slicing work on any type that is an
ordered list of elements.

Let's try that out with the DataFrame type from the `pandas` library,
which stores tabular data. We look at DataFrames in more detail in the
PyNoon Data course.

To import the pandas library as the alias `pd`:

```code
import pandas as pd
```

To load a CSV file into a DataFrame:

```code
df = pd.read_csv('http://pynoon.github.io/data/inside_airbnb_listings_nz_2023_09.csv')
```

> Note: Your notebook must not be inside a subfolder for this command
> to work.

Look at the contents of the DataFrame:

```code
df
```

Check the type of the DataFrame:

```code
type(df)
```

Get the first row of the DataFrame by indexing:

```code
df.iloc[0]
```

Get the first three rows of the DataFrame by slicing:

```code
df.iloc[0:3]
```

Check the length of the DataFrame:

```code
len(df)
```

Remember, **the type of the value determines what operations behave**.
Maths operations applied to a DataFrame are applied to every cell
individually:

```code
df * 5
```
