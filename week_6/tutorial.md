---
title: PyNoon Week 6 - Tutorial
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

This week's tutorial will cover defining and using your own functions,
and reducing duplication in your code.

It is based on:

* [swcarpentry.github.io/python-novice-gapminder/16-writing-functions.html](https://swcarpentry.github.io/python-novice-gapminder/16-writing-functions.html)

## Setup

1. Make a new notebook for this week
2. What's the first thing to do? RENAME IT!
3. Name it `week6.ipynb`

## Short aside: F-Strings

* F-strings allow us to insert the value of a Python variable or
  expression into a string:

```code
name = 'Ben'
print(f'Hello {name}')
print(f'Hello {name.upper()}')
```

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

## Applying functions to DataFrames

* We can apply functions to each value in a Pandas DataFrame.
* As we have previously, let's load our AirBnB listings data into Pandas:

```code
import pandas as pd
```

```code
listings_df = pd.read_csv('https://pynoon.github.io/data/inside_airbnb_listings_nz_2023_09.csv')
listings_df
```

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
value is the corresponding value returned by the function:

```code
listings_df['url'] = listings_df['id'].apply(id_to_url)
listings_df
```

We can also use `.apply()` with `axis='index'` on an entire DataFrame
to pass an entire row at a time to the function:

```code
def listing_to_description(row):
    room_type = row['room_type']
    host_name = row['host_name']
    return f'{room_type} by {host_name}'

listings_df['description'] = listings_df.apply(listing_to_description, axis='columns')
listings_df
```

## Organising code with functions

* Consider the following two blocks of code that look for "above
  average" listings.
* You can copy the code from:
  [pynoon.github.io/curriculum/week_6/duplication_example.py](https://pynoon.github.io/curriculum/week_6/duplication_example.py)

```code
akl_listings_df = listings_df[listings_df['region_parent_name'] == 'Auckland']
akl_average_price = akl_listings_df['price_nzd'].median()
akl_above_average_price_df = akl_listings_df[akl_listings_df['price_nzd'] > akl_median_price]
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
  changed it's behaviour.
* Writing tests is a great way to check that code produces the same
  results.
  * That will be part of this week's exercise

## Reducing duplication with loops and list comprehensions

* Loops can also help us reduce code duplication.
* For example, take the following code that transforms several text
  columns to lowercase:

```code
listings_df['name'] = listings_df['name'].str.lower()
listings_df['host_name'] = listings_df['host_name'].str.lower()
listings_df['region_name'] = listings_df['region_name'].str.lower()
listings_df['region_parent_name'] = listings_df['region_parent_name'].str.lower()
```

* We can loop over a list of columns, meaning we only have to define
  the transformation once.
* If we ever need to change the transformation, we only need to change
  it in once place.

```code
text_columns = ['name', 'host_name', 'region_name', 'region_parent_name']

for text_column in text_columns:
    listings_df[text_column] = listings_df[text_column].str.lower()
```

* It is quite common to want to transform one list of values into
  another list of values.
  * Similar to how we used `.apply()` on a Pandas Series earlier
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
