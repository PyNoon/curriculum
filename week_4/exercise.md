---
title: PyNoon Week 4 - Exercise
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

# PyNoon Week 4 - Exercise

## 1. Answering questions from data

Use the `listings_df` dataset from the tutorial to answer the
following questions.

* You should create a notebook that answers these questions one by one
  and uses Markdown/Text cells to explain how you arrived at the
  answer - as if you were reporting these results to a colleague.
* You may want to refer to the [Week 3
  Tutorial](https://colab.research.google.com/github/pynoon/curriculum/blob/main/week_3/week_3_tutorial.ipynb)
  and [Week 3
  Exercise](https://colab.research.google.com/github/pynoon/curriculum/blob/main/week_3/week_3_exercise.ipynb)
  for some Pandas functions/methods to help answer these questions.
* You may find it helpful to plot the data using Plotly Express to
  answer some questions.

## 1a. Which host has the most listings?

Hint: You may find it helpful to use Pandas' `.value_counts()` or an
appropriate plot as part of your answer.

## 1b. In which region is the most expensive listing?

Hint: You may find it helpful to use Pandas' `.max()` as part of your
answer.

## 1c. What is the lowest cost booking I could make?

Hint: Remember that each listing has a minimum number of nights you
must book for, and that the given `price_nzd` is the price per night.
You may find it helpful to use Pandas' `.min()` as part of your
answer.

## 1d. Which parent region has more affordable listings on average, Auckland or Christchurch City?

Hint: You may find it helpful to use Pandas' `.mean()` as part of your
answer.

You may think of different wants to interpret what "affordable" means,
does you answer change depending on your interpretation?

## 1e. Would you say that more expensive listings tend to get better or worse reviews than cheaper listings?

Hint: You may find a plot useful to examine the relationship between
`price_nzd` or `price_per_person` and `review_scores_rating`.

## 2. Futurecoder

Complete the following lesson on
[futurecoder.io](https://futurecoder.io):

1. Lists

> You can check which lesson you are up to on Futurecoder from the
> `Table of Contents` link at the top of the Futurecoder webpage.
