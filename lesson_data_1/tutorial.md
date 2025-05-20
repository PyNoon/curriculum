---
title: PyNoon Data Lesson 1 - Tutorial
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

* A brief intro to Colab/Jupyter notebooks
* Working with built-in and third party libraries
* Loading and exploring tabular data with Pandas

It is based on:

* [swcarpentry.github.io/python-novice-gapminder/04-built-in.html](https://swcarpentry.github.io/python-novice-gapminder/04-built-in.html)
* [swcarpentry.github.io/python-novice-gapminder/06-libraries.html](https://swcarpentry.github.io/python-novice-gapminder/06-libraries.html)
* [swcarpentry.github.io/python-novice-gapminder/07-reading-tabular.html](https://swcarpentry.github.io/python-novice-gapminder/07-reading-tabular.html)
* [swcarpentry.github.io/python-novice-gapminder/08-data-frames.html](https://swcarpentry.github.io/python-novice-gapminder/08-data-frames.html)

> DEMO-ONLY TUTORIAL BEGINS HERE

## Intro to Colab

> Skip this section if continuing on from the PyNoon Starter course.

* **Jupyter notebooks** are a very popular platform for Python coding,
  particularly for data analysis and visualisation.
* You can run Jupyter notebooks on your own computer with
  **jupyterlab**, but today we are running Jupyter notebooks in
  **Google Colab** so that you don’t need to install Python or Jupyter
  on your own computer.
  * Note: Because your notebooks will run on Google’s servers, you
    shouldn’t upload any company data or code you are not authorised
    to use outside of company-approved systems.
* Your notebooks in Google Colab will be saved to your Google Drive
  account, you can find previous notebooks from the
  `File -> Open notebook` menu.
* Cells can be run in any order we choose, so we need to be careful of
  the order we run cells.
  * When working in notebooks, it is a good idea to regularly select
    `Runtime > Restart` session and run all from the menu to ensure
    our code executes as we expect when run in order.

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
run as follows in a notebook:

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

1. Make a new notebook for this lesson
2. What's the first thing to do? RENAME IT!
3. Name it `pynoon_data_1.ipynb`

Let's look at the data we're going to analyse:

Use the link on
[pynoon.github.io/lessons](https://pynoon.github.io/lessons/) to open
`inside_airbnb_listings_nz_2023_09.csv`

* Look at the data dictionary linked to from that page to learn what
  each column means.


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
listings_df = pd.read_csv('https://pynoon.github.io/data/inside_airbnb_listings_nz_2023_09.csv')
```

* `df` is a *conventional* variable suffix for a DataFrame.
* Pandas has many different `read_*` functions for reading from
  different types of files (e.g. `read_excel()`, `read_parquet()`).

We can check whether any variable refers to a DataFrame:

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

* **This doesn't change the original DataFrame**, it produced a new
  DataFrame that is sorted.
* Notice that the ratings sorted "last" are `NaN` (aka `null` or
  `None` or "missing"). **By default `sort_values()` puts all `NaN`
  values at the end, regardless of sort order.**
* Indeed, these listings have a `number_of_reviews` equal to 0. We’ll
  need to consider how to handle these rating-less listings later.


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

### Summary Statistics

We can get summary statistics for all numeric columns:

```code
listings_df.describe()
```

`.describe()` gives us:

* The count of non-NaN values
* The mean and standard deviation (i.e. how far values spread from the mean)
* Min/max values
* The 25%, 50%, and 75% quantiles

And we can get specific summary statistics for column's individually:

```code
listings_df['price_nzd'].max()
```

The maximum price looks suspiciously large for a price per night, this
will warrant further investigation!

For categorical values, we can get an initial picture by counting the
frequency of each distinct value:

```code
listings_df['room_type'].value_counts()
```

### Plotting Demo

* While useful, summary statistics only tell us part of the story.
* With the power of Python, there’s nothing stopping us from plotting
  our data to give us a clearer picture!
* As a quick demo of the power of DataFrames, we can install and use
  the Plotly library to create plots from DataFrame columns:

```code
%pip install plotly nbformat
```

```code
import plotly.express as px
```

```code
px.scatter(listings_df, x='longitude', y='latitude')
```

```code
px.histogram(listings_df, x='review_scores_rating')
```
