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

The value returned is either `True` or `False`, a **Boolean** value:

```code
type(1 < 2)
```

To check if two values are equal, use two equal signs (as a single
equal sign is used by Python for assignment):

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
if bag_kg <= 7:
    print('Bag allowed as carry-on')
    print('Please proceed to board the plane')
else:
    print('Please check your bag')
```

> `<=` is "less than or equal to"

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

We can see how big the DataFrame is using `.shape`:

```code
listings_df.shape
```

We can also see what columns we have available to work with:

```code
listings_df.columns
```


## Column Types and Data Preparation

Every column has a type of value stored in it:

```code
listings_df.info()
```

* Even though the CSV provided no data type information, numeric types
  have been automatically inferred by Pandas
* Non-numeric types like strings are listed as `object` (we only have
  strings here)
* **Types aren’t always what we want** - the `last_review` column
  should be a datetime

We can convert date columns from strings to dates:

```code
pd.to_datetime(listings_df['last_review'])
```

We must assign the transformed column to replace the original column:

```code
listings_df['last_review'] = pd.to_datetime(listings_df['last_review'])
```

```code
listings_df.info()
```

## Computing new columns

Applying standard Python maths operators on a Series performs the
operation on each value in the Series and returns a new Series:

```code
listings_df['price_nzd'] * 0.5
```

Performing maths with two Series applies the operation *element-wise*
to each pair of values from the two Series:

```code
listings_df['price_nzd'] / listings_df['accommodates']
```

Just as we can updated columns, we can add a new column to an existing
DataFrame by assigning to a new column name that doesn't exist in the
DataFrame yet:

```code
listings_df['price_per_person'] = listings_df['price_nzd'] / listings_df['accommodates']
```

```code
listings_df
```


## Use comparisons to select data based on value.

Using a comparison operator on a Series performs the comparison to
each value in the Series, and returns a new Series full of Boolean
values:

```code
listings_df['region_parent_name'] == 'Auckland'
```

> Remember: the type of the value determines what an operation will do
> with it.

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


## Pandas and Plotly Documentation

The tools for transforming and filtering data we’ve used here are the
kind of code you’ll spend much of your time writing when analysing
data with Pandas.

Find out what other functions (methods) and variables (attributes) are
attached to DataFrames and Series from their reference documentation:

* https://pandas.pydata.org/pandas-docs/stable/reference/frame.html
* https://pandas.pydata.org/pandas-docs/stable/reference/series.html

Similarly, look at the user guide and reference documentation for
Plotly express to see what other plot types are available and what
arguments they will accept to configure them:

* https://plotly.com/python/plotly-express/
* https://plotly.com/python-api-reference/


## More Data Preparation

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
