---
title: PyNoon Data Lesson 1 - Exercise
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

# PyNoon Data: Lesson 1 - Exercise

## 1. Software Carpentry Exercises

## 1a. When is help available?

When a colleague of yours types help(math), Python reports an error:

```
NameError: name 'math' is not defined
```

What has your colleague forgotten to do?

<details>
    <summary>Answer:</summary>
    They have forgotten to Import the math module (`import math`)
</details>

## 1b. Importing With Aliases

1. Fill in the blanks so that the program below prints `90.0`.
2. Rewrite the program so that it uses `import` without `as`.
3. Which form do you find easier to read?

```code
import math as m
angle = ____.degrees(____.pi / 2)
print(____)
```

## 1c. Writing Data

As well as the `read_csv` function for reading data from a file,
Pandas provides a `to_csv` function to write DataFrames to files.
Applying what you’ve learned about reading from files, write
`listing_df` from the tutorial to a file called `processed.csv`. You
can use `help(listing_df.to_csv)` or Pandas documentation to get
information on how to use `to_csv`.

## 2. Exploratory Data Analysis Notebook

In this assignment, your task is to extend your notebook from this
lesson's tutorial into a shareable notebook that performs Exploratory
Data Analysis to identify interesting details of the AirBnB listings
dataset.

* In future lessons, we'll cover even more features of Python and
  Pandas to help you extend your exploratory data analysis.
* If you have another CSV you'd like to perform Exploratory Data
  Analysis instead of the AirBnB listings, feel free!

### 2a. Calculate Descriptive Statistics

Add additional cells to your notebook to understand more about the
AirBnB listings.

**Calculate additional descriptive statistics of DataFrame columns.**

For example, the mean of the `latitude` column can be computed with:

```code
listings_df['latitude'].mean()
```

Have a look at the other methods that are available to compute
descriptive statistics of DataFrame columns (remember, the data type
of a single column is a `Series`):
[pandas.pydata.org/pandas-docs/stable/reference/series.html#computations-descriptive-stats](https://pandas.pydata.org/pandas-docs/stable/reference/series.html#computations-descriptive-stats)

### 2c. Find Frequent and Rare Values

Learn more about the `.value_counts()` method of Series from the
Pandas' documentation or by using `help()`:

```code
help(listings_df.value_counts)
```

Use this method to find the most frequent and least frequent values
for columns of your choosing. What columns would it be interesting to
find out the frequent and rare values for?

### 2d. Missing Values

Learn more about the `.isna()` and `.dropna()` methods of Series from
the Pandas' documentation or by using `help()`.

Use these methods to find which columns have "missing" (aka `na`)
values, and how many values are missing in those columns. Hint: as
part of calculating the number of missing values in a column Series,
you may find it helpful to apply the `len()` function on one or more
Series.

### 2d. Plotting

Have a look at the different kinds of plotting functions available
from [Plotly Express](https://plotly.com/python/plotly-express/), and
create some interesting plots of column values.

### 2e. Document your Notebook

1. Ensure your notebook has a meaningful name that makes it clear that
   it performs exploratory analysis of the listings dataset.
2. Add Markdown cells with
   [headings](https://www.markdownguide.org/basic-syntax/#headings)
   to:
   1. Provide a title at the beginning of the notebook
   2. Mark the beginning of the code that loads the dataset
   <!-- 3. Mark the beginning of the code that pre-processes the dataset -->
   <!--    (i.e. setting the index and changing column data types) -->
   3. Mark the beginning of the code that analyses the dataset
3. Extend or add more Markdown cells to document:
   <!-- 1. What each data pre-processing step is for -->
   1. What each analysis of the dataset tells you about the data -
      provide commentary you think would be useful to a colleague who
      will also be working with this data

## 3. Futurecoder

Complete the following lesson on [futurecoder.io](https://futurecoder.io):

1. Lists

> You can check which lesson you are up to on Futurecoder from the
> `Table of Contents` link at the top of the Futurecoder webpage.
