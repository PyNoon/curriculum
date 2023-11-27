---
title: PyNoon Week 3 - Tutorial
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

This week's tutorial will cover:

* A review of functions
* Working with built-in and third party libraries
* Loading and exploring tabular data with Pandas

It is based on:

* [swcarpentry.github.io/python-novice-gapminder/04-built-in.html](https://swcarpentry.github.io/python-novice-gapminder/04-built-in.html)
* [swcarpentry.github.io/python-novice-gapminder/06-libraries.html](https://swcarpentry.github.io/python-novice-gapminder/06-libraries.html)
* [swcarpentry.github.io/python-novice-gapminder/07-reading-tabular.html](https://swcarpentry.github.io/python-novice-gapminder/07-reading-tabular.html)
* [swcarpentry.github.io/python-novice-gapminder/08-data-frames.html](https://swcarpentry.github.io/python-novice-gapminder/08-data-frames.html)

> DEMO-ONLY TUTORIAL BEGINS HERE

:::::: {.notebook-only}
## Functions

We've used functions in previous tutorials, but we're going to start
using a lot more of them, so lets summarise their key facts:

**Functions are like small Python scripts that we can *call* to
perform some operation or return some value.**

**Functions are *called* using parentheses, with *arguments* inside the parentheses.**
::::::

:::::: {.cell .code .notebook-only}
```code
print('hello')
```
::::::

:::::: {.notebook-only}
Using a function's name without parentheses refers to the function
itself *as* a value:
::::::

:::::: {.cell .code .notebook-only}
```code
print
```
::::::

:::::: {.notebook-only}
**Functions attached to values are called *methods***
::::::

:::::: {.cell .code .notebook-only}
```code
'hello'.upper()
```
::::::

:::::: {.notebook-only}
**Some functions take multiple arguments**
::::::

:::::: {.cell .code .notebook-only}
```code
round(3.14159, 2)
```
::::::

:::::: {.notebook-only}
**Functions may have default values for some arguments**

`round()` defaults to rounding a number to zero decimal places:
::::::

:::::: {.cell .code .notebook-only}
```code
round(3.14159)
```
::::::

:::::: {.notebook-only}
**Every function returns a value**

Even functions that don't seem to return a value (like `print`)
actually return a special value called `None` (similar to `null` in
SQL or other languages):
:::::::

:::::: {.cell .code .notebook-only}
```code
returned_value = print('hello')
```
::::::

:::::: {.cell .code .notebook-only}
```code
returned_value
```
::::::

:::::: {.cell .code .notebook-only}
```code
type(returned_value)
```
::::::

:::::: {.notebook-only}
**Functions accept named arguments (and some require it):**
::::::

:::::: {.cell .code .notebook-only}
```code
round(3.14159, ndigits=2)
```
::::::

:::::: {.notebook-only}
**Use the built-in function help to get help for a function**
::::::

:::::: {.cell .code .notebook-only}
```code
help(round)
```
::::::

:::::: {.cell .code .notebook-only}
```code
help('hello'.upper)
```
::::::

:::::: {.notebook-only}
**Use `dir()` and `dir(__builtins__)` to list available functions (and
non-function variables)**
::::::

:::::: {.cell .code .notebook-only}
```code
dir()
```
::::::

:::::: {.cell .code .notebook-only}
```code
dir(__builtins__)
```
::::::

:::::: {.notebook-only}
> Don't worry about the underscored names

**Use `dir(some_value)` to list methods (and non-function variables
called attributes) of a value**
::::::

:::::: {.cell .code .notebook-only}
```code
dir('hello')
```
::::::

:::::: {.notebook-only}
* See
  [docs.python.org/3/library/functions.html](https://docs.python.org/3/library/functions.html)
  for more about functions that are built-in and always available in
  Python.
* A key power of Python is that you can define your own functions as
  Python code to execute when the function is called.
::::::


## Modules and Libraries

To get more functions (and other things) to use in Python, you can
import **modules**, which are just files of Python code.

To use the contents of a module, we must import it once (usually at
the top of our notebook or script):

```code
import math
```

Then we can use functions and variables from the module:

```code
math.pi
```

```code
math.sqrt(4)
```

We can use the `help()` function to find out what is available in a
module:

```code
help(math)
```

:::::: {.notebook-only}
Sometimes we want to import only certain functions or variables from a
module...
::::::

:::::: {.cell .code .notebook-only}
```code
from math import pi, e
```
::::::

:::::: {.notebook-only}
Or import the module under an aliased name...
::::::

:::::: {.cell .code .notebook-only}
```code
import pandas as pd
```
::::::

* `math` is one of the many modules in Python's **standard library**,
  which is well known for its extensive functionality.
  * You can find out more about the modules available at:
  [docs.python.org/3/library](https://docs.python.org/3/library/index.html)
* Python is also well known for its many **3rd party libraries** that
  provide more modules, but before they can be imported they must be
  downloaded to your computer.
  * You can search for available Python libraries at:
    [pypi.org](https://pypi.org/)

3rd party Python libraries can be downloaded with `pip`, which can be
run as follows in JupyterLite:

```code
%pip install pandas
```

> **Anyone** can publish a 3rd party library, so it's prudent to ask
> the following questions before installing a library:
>
> * Has someone you trust recommended this library?
> * Is there concrete evidence of an active user base for this library?
> * Am I sure I am spelling the library's name correctly? (malicious users
>   have been known to publish "typo-squatting" libraries with similar names
>   to popular libraries)

The webpage for a library on `pypi.org` will often have links to:

* A **GitHub (or similar) page** where you can read the library's
code, report issues, and contribute improvements.
* A **quick start** to briefly demonstrate you how to use the library
* More extensive **documentation** or an **API reference** that
  documents all the functions and capabilities of the library.

For example, check out:
[pypi.org/project/pandas](https://pypi.org/project/pandas/)

> FOLLOW-ALONG TUTORIAL BEGINS HERE

## Setup

Let's start by getting some data to analyse:

1. MAKE A BACKUP OF YOUR EXISTING NOTEBOOKS
   * I have observed a bug with JupyterLite deleting files when
     working with CSV files
2. Use the link on
   [pynoon.github.io/schedule](https://pynoon.github.io/schedule/) to
   open `inside_airbnb_listings_nz_2023_09.csv`
   * Look at the data dictionary linked to from that page to learn
     what each column means.
3. Double-click on the file in the file browser to view it in
   JupyterLite.
4. Make a new notebook for this week
5. What's the first thing to do? RENAME IT!
6. Name it `week3.ipynb`

## Pandas DataFrames

We can use the `pandas` library to work with tabular data in Python.

* Pandas is based on a lower-level maths library called `numpy`
* Pandas DataFrames are similar to R's DataFrames

```code
import pandas as pd
```

> Importing Pandas as the alias `pd` is conventional, and saves us
> typing out `pandas` everytime we want to use it.

To load the CSV into a DataFrame:

```code
listings_df = pd.read_csv('inside_airbnb_listings_nz_2023_09.csv')
```

* `df` is a *conventional* variable suffix for a DataFrame.
* Pandas has many different `read_*` functions for reading from
  different types of files (e.g. `read_excel()`, `read_parquet()`).

```code
type(listings_df)
```

Let's look at the DataFrame:

```code
listings_df
```

> Only a few rows from the top and bottom of the DataFrame are shown

We can sort the DataFrame by a column:

```code
listings_df.sort_values('review_scores_rating')
```

> Note: This doesn't change the original DataFrame, it produced a new
> DataFrame that is sorted

We can extract a single column from the DataFrame:

```code
listings_df['name']
```

The type of a single column or row from a Pandas `DataFrame` is a
`Series`:

```code
type(listings_df['name'])
```


Also handy to get a new DataFrame that only contains a subset of
columns:

```code
listings_df[['latitude', 'longitude']]
```

### Column Types and Data Preparation

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

### Summary Statistics

We can get summary statistics for all numeric columns:

```code
listings_df.describe()
```

And we can get specific summary statistics for column's individually:

```code
listings_df['last_review'].max()
```

```code
listings_df['review_scores_rating'].mean()
```

### Plotting Demo

As a quick demo of the power of DataFrames, we can install and use the
Plotly library to create plots from DataFrame columns:

```code
%pip install plotly nbformat
```

```code
import plotly.express as px
```

```code
px.scatter(listings_df, x='longitude, y='latitude')
```

```code
px.histogram(listings_df, x='price')
```

<!--
### DataFrame Indexing and Slicing

* The first "column" in the DataFrame is the *index*, which defaults to incrementing
  integers
* Like how each column has a name, the *index* is the "name" of each
  row
* We can assign a column to be the index of a DataFrame:

```code
listings_df = listings_df.set_index('id')
```

```code
listings_df
```

Why do we need to assign the result of `set_index()`?

* Calling `.set_index()` does not change the original DataFrame value
* Calling `.set_index()` returns a **new DataFrame value** with the
  index changed, which we then assign to the original variable.
* Most Pandas methods return a new value rather than changing the
  original value.


**We can perform indexing and slicing on DataFrames using `.iloc`:**

To get the first row:

```code
listings_df.iloc[0]
```

To get the second column in the first row:

```code
listings_df.iloc[0, 1]
```

To get the second column of the first five rows:

```code
listings_df.iloc[0:5, 1]
```

To get the second column of all rows:

```code
listings_df.iloc[:, 1]
```

**We can also index and slice rows and columns by their names:**

To get a single row by it's name in the index:

```code
listings_df.loc['l9995141']
```

To get several rows by their names:

```code
listings_df.loc[['l9995141', 'l12026015', 'l44688136']]
```

> While you can use `:` slicing to specify a start and end names for a
> range, it is more common to specify a list of names.

To get the `name` column of all rows:

```code
listings_df.loc[:, 'name']
```
-->
