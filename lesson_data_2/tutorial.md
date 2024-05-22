---
title: PyNoon Data Lesson 2 - Tutorial
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

This tutorial will cover Boolean comparisons and more Pandas
for analysing and manipulating tabular data.

It is based on:

* [swcarpentry.github.io/python-novice-gapminder/07-reading-tabular.html](https://swcarpentry.github.io/python-novice-gapminder/07-reading-tabular.html)
* [swcarpentry.github.io/python-novice-gapminder/08-data-frames.html](https://swcarpentry.github.io/python-novice-gapminder/08-data-frames.html)


> DEMO-ONLY TUTORIAL BEGINS HERE

## Boolean Comparisons

*Comparison operators* can be used to compare two values:

```code
1 < 2
```

In the code above, we are effectively asking "is 1 less than 2?".

Let's try the "greater than or equal to" operator next:

```code
1 >= 2
```

The value returned is either `True` or `False`, a **Boolean** value:

```code
type(1 < 2)
```

To check if two values are equal, use two equal signs (as a single
equal sign is used by Python for assignment):

```code
'pynoon' == 'pynoon'
```

```code
'pynoon' == 'PYNOON'
```

We can directly state a Boolean value by name - but remember to start with a capital letter!

```code
True
```

Boolean values can be inverted with `not`:

```code
not True
```

Multiple Boolean values can be combined with `and` and `or`, or
inverted with `not`:

```code
True and False
```

```code
True or False
```

As usual, parentheses can be used to group operations:

```code
True and (True or False)
```

Comparisons are commonly used to conditionally run different lines of
code using `if` statements (as seen in more detail in the Futurecoder
lessons):

```code
bag_kg = 3
if bag_kg < 7:
    print('Bag allowed as carry-on')
    print('Please proceed to board the plane')
else:
    print('Please check your bag')
```

> Note: The `else:` clause is optional

> FOLLOW-ALONG TUTORIAL BEGINS HERE

## Setup

1. Make a new notebook for this lesson
2. What's the first thing to do? RENAME IT!
3. Name it `pynoon_data_2.ipynb`

## Loading Data into Pandas

As we did last lesson, let's load our AirBnB listings data into Pandas:

```code
import pandas as pd
```

```code
listings_df = pd.read_csv('https://pynoon.github.io/data/inside_airbnb_listings_nz_2023_09.csv')
```

> We can load data from local files or, in this case, directly from a URL.

```code
listings_df
```

## Use comparisons to select data based on value.

Recall that we can refer to a single column from a DataFrame,
returning a value with a type of Pandas' `Series`:

```code
listings_df['region_parent_name']
```

```code
type(listings_df['region_parent_name'])
```

Using a comparison operator on a Series performs the comparison to
each value in the Series, and returns a new Series full of Boolean
values:

```code
listings_df['region_parent_name'] == 'Auckland'
```

> Remember: the type of the value determines what an operation will do with it.

We can use the Boolean Series, commonly called a **mask**, to return a
*new* DataFrame that is filtered to contain only the rows where the
mask is `True`:

```code
auckland_mask = listings_df['region_parent_name'] == 'Auckland'
listings_df[auckland_mask]
```

### Plotting filtered DataFrames

Let's use filtering to plot the ratings of highly reviewed listings.

First, import Plotly and plot the ratings:

```code
%pip install plotly nbformat
import plotly.express as px

px.histogram(listings_df, x='review_scores_rating')
```

Now, filter the DataFrame to only contain listings with more than 100
reviews:

```code
px.histogram(listings_df[listings_df['number_of_reviews'] > 100], x='review_scores_rating')
```

### Combining filters

Just as we could use `not`, `and`, and `or` to combine Boolean values,
we can also combine Boolean Series.

Let's remind ourselves of the value of `auckland_mask`:

```code
auckland_mask
```

Just like how we can use `not` to invert a Boolean value, we can use
`~` to invert a mask:

```code
~auckland_mask
```

We can also use `|` to perform an `or` operation between two masks,
and `&` to perform an `and` operation:

```code
good_mask = listings_df['review_scores_rating'] > 4.9
```

```code
good_mask
```

```code
auckland_mask | good_mask
```

```code
auckland_mask & good_mask
```

One final note: Conditions on NaN values always return False.


## Computing new columns

Performing maths on a Series applies the operation to each value in
the Series, returning a new Series:

```code
nzd_to_aud = 0.93
listings_df['price_nzd'] * nzd_to_aud
```

Performing maths with two Series applies the operation element-wise to
each pair of values from the two Series:

```code
listings_df['price_nzd'] / listings_df['accommodates']
```

We can add a new column to an existing DataFrame by assigning to a new
column name that doesn't exist in the DataFrame yet:

```code
listings_df['price_per_person'] = listings_df['price_nzd'] / listings_df['accommodates']
```

```code
listings_df
```

```code
listings_df['price_per_person'].describe()
```


## Pandas and Plotly Documentation

Find out what other functions (methods) and variables (attributes) are
attached to DataFrames and Series from their reference documentation:

* https://pandas.pydata.org/pandas-docs/stable/reference/frame.html
* https://pandas.pydata.org/pandas-docs/stable/reference/series.html

Similarly, look at the user guide and reference documentation for
Plotly express to see what other plot types are available and what
arguments they will accept to configure them:

* https://plotly.com/python/plotly-express/
* https://plotly.com/python-api-reference/


## Column Types and Data Preparation

Every column has a type of value stored in it:

```code
listings_df.info()
```

* Numeric types have been automatically inferred by Pandas
* Non-numeric types like strings are listed as `object` (we only have
  strings here)
* Some types aren't what we want

We can convert date columns from strings to dates:

```code
pd.to_datetime(listings_df['host_since'])
```

We must assign the transformed columns to replace the original columns:

```code
listings_df['host_since'] = pd.to_datetime(listings_df['host_since'])
listings_df['last_review'] = pd.to_datetime(listings_df['last_review'])
```

```code
listings_df.info()
```

```code
listings_df
```

We can also remove the dollar sign from each price:

```code
listings_df['price'].str.replace('$', '', regex=False)
```

We can "chain" additional method calls on the results of previous
method calls to replace commas and convert the column data type from
string to float:

```code
listings_df['price'].str.replace('$', '', regex=False).str.replace(',', '', regex=False).astype(float)
```

```code
listings_df['price'] = listings_df['price'].str.replace('$', '', regex=False).str.replace(',', '', regex=False).astype(float)
```

```code
listings_df.info()
```

```code
listings_df
```
