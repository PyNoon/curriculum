---
title: PyNoon Week 5 - Exercise
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

# PyNoon Week 5 - Exercise

## 1. Grouping and summarising exercises

Use the `listings_df` dataset from the tutorial to answer the
following questions.

You should create a notebook that answers these questions one by one
and uses Markdown/Text cells to explain how you arrived at the
answer - as if you were reporting these results to a colleague.

### 1a. Which parent region has the highest average listing price?

Hint: Use a `groupby()` with an appropriate average statistic like
`mean()` or `median()`.

Bonus: The answer changes depending on whether you use `mean()` or
`median()`, what does that indicate?

### 1b. Create a bar chart to show how many listings of each room type there are in each parent region.

Hint: Use a `groupby()` with the `count()` statistic.

### 1c. Do "home" listings cost more? Are they better reviewed? Do they accommodate more people?

Hint: Use `.str.lower()` and `.str.contains()` to find listings with
the keyword "home", then use appropriate `groupby()`s and/or plotting.

### 1d. Of hosts with at least 10 reviewed listings, who has the highest average rating?

Hint: Use a `groupby()` on `review_scores_rating` with `.agg(['count',
'mean'])` to get both the count and mean of the ratings (see:
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.agg.html).
Then filter hosts based on the count of listings.

### 1e. Which parent region has the most listings that have no rating? Which has the highest proportion of listings with no rating?

Hint: Use `.isna()` to filter to listings with a missing rating. Then
use `groupby()` or `value_counts()` to count the number of listings
for each parent region.

### 1f. Do listings with higher prices typically have higher ratings?

Hint: Use `cut()`
(https://pandas.pydata.org/docs/reference/api/pandas.cut.html) to
create a categorical column containing small number of price bands.
Then use use appropriate `groupby()`s and/or plotting.


## 2. Futurecoder

Complete the following lessons on
[futurecoder.io](https://futurecoder.io):

1. A bit more about strings
2. Nested Loops

> You can check which lesson you are up to on Futurecoder from the
> `Table of Contents` link at the top of the Futurecoder webpage.


## 3. Identify a Personal Python Project to work on

* Do you have a dataset you want to analyse?
  * A spreadsheet from work?
  * Home income/expense data?
  * Something from:
    * https://www.kaggle.com/datasets
    * https://catalogue.data.govt.nz/dataset
* Is there a text or image file processing task you want to automate?
  * Automating a backup of specific files
  * Renaming files and organising them into folders
  * Generating a report from spreadsheets, word documents, or images
* For more inspiration, have a look at:
  * https://automatetheboringstuff.com/#toc
