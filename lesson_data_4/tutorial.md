---
title: PyNoon Data Lesson 4 - Tutorial
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

This tutorial will cover defining and using your own functions, and
reducing duplication in your code.

It is based on:

* [swcarpentry.github.io/python-novice-gapminder/16-writing-functions.html](https://swcarpentry.github.io/python-novice-gapminder/16-writing-functions.html)

## Setup

1. Make a new notebook for this lesson
2. What's the first thing to do? RENAME IT!
3. Name it `pynoon_starter_3.ipynb`

## Defining Functions

* One of the key ways to reduce duplication of code in our projects is
  to define our own re-usable functions.
* In Python, we can use the `def` keyword to define our own functions.
* Any number of lines of code after the `def` line that are *indented*
  make up the *body* of the function that is executed when the
  function is called.

```code
def print_greeting():
    print('Hello World!')
    print('How are you?')
```

Defining the function does not execute the code inside it, but we can
call the function just like any other function:

```code
print_greeting()
```

* We can write functions that accept arguments.
* The argument can be used just like any other variable in the
  function's body.

```code
def print_greeting(name):
    print(f'Hello {name}!')
    print('How are you?')
```

```code
print_greeting('Cooper')
```

* We can write functions that return values using the `return`
  statement.
* The function will immediately exit as soon as it hits any `return`
  statement.
* If a function does not `return` a value, it implicitly returns the
  value `None`.

```code
def shorten_description(description, max_length):
    if len(description) > max_length:
        short_description = description[:max_length] + '...'
        return short_description
    return description
```

```code
short_description = shorten_description('This is a very long description', 10)
short_description
```

* A benefit of functions is that we can test that they return the
  values we expect for a variety of argument combinations.
* For example, let's test that `shorten_description` returns the
  `description` unchanged if it is equal to the `max_length`:

```code
shorten_description('12345', 5) == '12345'
```

* An `assert` statement will raise an error if the Boolean expression
  given to it returns `False`:

```code
assert shorten_description('12345', 5) == '12345'
```

Now let's test that the `description` is limited to the given
`max_length`:

```code
assert shorten_description('123456789', 5) == '12...'
```

Hmmm, why did that fail?

```code
shorten_description('123456789', 5)
```

Aha! we need take into account the length of the ellipsis:

```code
def shorten_description(description, max_length):
    if len(description) > max_length:
        ellipsis = '...'
        return description[:(max_length - len(ellipsis))] + ellipsis
    return description
```

## Short aside: F-Strings

* F-strings allow us to insert the value of a Python variable or
  expression into a string:

```code
name = 'Ben'
print(f'Hello {name}')
print(f'Hello {name.upper()}')
```

## Applying functions to DataFrames

* We can apply functions to each value in a Pandas DataFrame.
* Let's load our AirBnB listings data into Pandas:

```code
import pandas as pd
```

```code
listings_df = pd.read_csv('https://pynoon.github.io/data/inside_airbnb_listings_nz_2023_09.csv')
listings_df
```

While Pandas provides many more functions for transforming DataFrames
and Series, it is still often convenient to express a transformation
as plain-old-Python code applied to a single value or row.

We can do this by writing our transformation as a regular Python
function and then *applying* it to a Series or DataFrame.

To transform a listing ID into a URL, we can do the following:

```
id = 'l11909616'
f'https://www.airbnb.co.nz/rooms/{id[1:]}'
```

Let's define a function to transform a listing ID into a URL:

```code
def id_to_url(id):
    return f'https://www.airbnb.co.nz/rooms/{id[1:]}'
```

```code
id_to_url('l11909616')
```

Calling `.apply(id_to_url)` on a single column Series passes each item
in the Series to the function and returns a new Series where each
value is the corresponding value returned by the function. We can then
assign the resulting Series into a new `url` column:

```code
listings_df['url'] = listings_df['id'].apply(id_to_url)
listings_df
```

We can also use `.apply()` with `axis='columns` on an entire DataFrame
to pass an entire row at a time to the function.

The output will still be a single Series of the returned values.

```code
def listing_to_description(row):
    room_type = row['room_type']
    host_name = row['host_name']
    return f'{room_type} by {host_name}'

listings_df['description'] = listings_df.apply(listing_to_description, axis='columns')
listings_df
```

The `row` passed into the function will be a Series representing a
single row in the DataFrame.

We can access the row's value for each column in the same way we
access columns in a DataFrame.


One important point to know about `.apply()` is that **Pandas built-in
operations will often be much faster** than running plain-old-Python on
each row.

However, this often won't make much of a difference until you're
dealing with hundreds of thousands or millions of rows. And remember,
when exploring the data it's **most important for you to be able to
quickly translate your ideas into working code!**


## Organising code with functions

* Consider the following two blocks of code that look for "above
  average" listings.
* You can copy the code from:
  [pynoon.github.io/curriculum/lesson_data_4/duplication_example.py](https://pynoon.github.io/curriculum/lesson_data_4/duplication_example.py)

```code
akl_listings_df = listings_df[listings_df['region_parent_name'] == 'Auckland']
akl_average_price = akl_listings_df['price_nzd'].median()
akl_above_average_price_df = akl_listings_df[akl_listings_df['price_nzd'] > akl_average_price]
display(akl_above_average_price_df)

wlg_listings_df = listings_df[listings_df['region_parent_name'] == 'Wellington City']
wlg_average_rating = wlg_listings_df['review_scores_rating'].median()
wlg_above_average_rating_df = wlg_listings_df[wlg_listings_df['review_scores_rating'] > wlg_average_rating]
display(wlg_above_average_rating_df)
```

* We can define a re-usable function to reduce code duplication here.
* First, let's identify the differences between the blocks of code:
  * One looks at Auckland, the other Wellington
  * One considers price, the other rating
* These points of difference determine the arguments to our function.
* We also add a **docstring** to document what our function does.

```code
def get_above_average_listings_df(listings_df, comparison_column):
    """Returns the subset of the given listings_df that is above average
    according to the given comparison_column."""
    average_value = listings_df[comparison_column].median()
    return listings_df[listings_df[comparison_column] > average_value]
```

```code
akl_above_average_price_df = get_above_average_listings_df(
    listings_df=listings_df[listings_df['region_parent_name'] == 'Wellington City'],
    comparison_column='price_nzd',
)
wlg_above_average_rating_df = get_above_average_listings_df(
    listings_df=listings_df[listings_df['region_parent_name'] == 'Wellington City'],
    comparison_column='review_scores_rating',
)
```

* Naming our arguments when calling the function makes it easier to
  read the function calls.
* While we could accept a `parent_region_name` argument, we instead
  accept a `listings_df`
  * Because it is listed as an argument, the `listings_df` *local*
    variable inside the function is separate to the `listings_df`
    *global* variable we have been using outside the function.
  * It is also good practice to avoid depending on global variables in
    functions - it makes them more versatile for re-use.
  * Accepting a `listings_df` is more versatile, because we are not
    restricted to just filtering by region - we can pass in any
    filtered (or even unfiltered) DataFrame of listings.

* Whenever *refactoring* code to make it more readable, maintainable,
  or re-usable - it is important to make sure that we have *NOT*
  changed its behaviour.
* Writing tests is a great way to check that code produces the same
  results.
  * That will be part of this lesson's exercise
