---
title: PyNoon Week 1 - Exercise
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

# PyNoon Week 1 - Exercise

## 1. Futurecoder Lessons

Complete the following lessons on [futurecoder.io](https://futurecoder.io):

1. The Shell
2. String Basics
3. Variables

> You can check which lesson you are up to on Futurecoder from the
> `Table of Contents` link at the top of the Futurecoder webpage.


## 2. Back-of-the-envelope Calculation

A common use case for Python programming is performing
"back-of-the-envelope" calculations, where need to produce a rough
estimate of some numerical value based on a number of input values,
some of which may themselves be estimates. For example, we might like
to estimate the annual revenue for a company based on known product
prices and rough estimates of daily sales.

Python is great for performing back-of-the-envelope calculations
because:

* We can use it to perform many different mathematical operations
  * In the tutorial, you have seen basic operations like `+`, `-`,
    `*`, `/` and grouping operation with parentheses `()`.
* The lines of Python code that perform the calculation show how the
  calculation is performed step-by-step
* We can add notes and use meaningful variable names so that others
  (or our future selves) can easily understand the steps in the
  calculation.

Your assignment is to write a Python notebook that performs a
back-of-the-envelope calculation for some problem that is of interest
to you. You will need to use what you have learned in the tutorial and
futurecoder lessons about maths and variables.

### 2a. Pick something to calculate

* Pick some value that you would like to calculate, you may like to
  pick a use case from your own work domain, or something that
  interests you.
* You do not need to have exact values for all of the inputs needed to
  perform your calculation - the inexact inputs are what makes this a
  "back-of-the-envelope" calculation.
* Here are a few ideas of possible calculations to inspire you:
  * Calculate the revenue or profit for a business based on some
    approximate product prices and counts of customers.
  * Calculate the floor area of your home or office based on the
    dimensions of each room.
  * Calculate the number of Weetbix the whole of New Zealand eats in a
    year.

### 2b. Create a notebook for your calculation

* Create a new notebook in JupyterLite for your calculation.
* Give the notebook a meaningful name that describes your calculation.
  * The name should contain only lowercase letters, numbers, and
    underscores.

### 2c. Identify the inputs

* Make a list of the different values that will serve as inputs to
  your calculation.
* In a new notebook cell, define a variable for each input, assigning
  your best estimate for its value.
* Make sure you given your variables meaningful names made of
  lowercase letters, numbers, and underscores. Include any relevant
  units in the variable name.
* For example, here are what the variable assignments may look like
  to calculate the revenue of a cinema:

```code
adult_ticket_price = 15.5
child_ticket_price = 10.5

average_movie_hours = 1.75
opening_hours_per_day = 8

cinemas = 5
average_adult_tickets_per_movie = 80
average_child_tickets_per_movie = 40
```

* Run your notebook cell (with `shift+enter`) to make sure that it
  runs without errors.

### 2d. Add calculation steps

* Add more lines to the end of your notebook cell to perform each step
  of your calculation
* Each step should perform a mathematical operation with on one or
  more variables and assign the result to a new variable
* The number of calculation steps needed will depend on the
  calculation you have chosen
* For example, here are what the calculation steps may look like to
  calculate the revenue of a cinema:

```code
revenue_per_movie = (adult_ticket_price * average_adult_tickets_per_movie) + (child_ticket_price * average_child_tickets_per_movie)
average_movies_per_day = opening_hours_per_day / average_movie_hours
average_revenue_per_day = average_movies_per_day * revenue_per_movie
annual_revenue_forecast = average_revenue_per_day * 365
```

* Run your notebook cell (with `shift+enter`) to make sure that it
  runs without errors.

### 2e. Print the calculation result

* Add more lines to the end of your notebook cell to print the result
  of your calculation.
* You may like to print the values of intermediate calculation
  variables in addition to the final calculation result.
* You should print text values (wrapped in single quotes `'`) to
  describe what each value is (including any applicable units).
* You can print multiple text, number, or variable values from one
  print function call as follows:

```code
name = 'Guido'
print('My name is:', name)
```

* For example, here are the lines that could be used to print the
  results of the revenue calculation example:

```code
print(f'Revenue per movie:', revenue_per_movie)
print('Average movies per day:', average_movies_per_day)
print('Average daily revenue:', average_revenue_per_day)
print('Annual revenue forecast:', annual_revenue_forecast)
```

* Run your notebook cell (with `shift+enter`) to make sure that it
  runs without errors.

### 2f. Experiment!

* Try changing the values you assigned to your input variables and
  re-running the calculation.
* How do changes in the input variables affect the final result?
* What happens if you change input variables to have unexpected
  values, like zero or negative numbers?

### 2g. Document!

* Add one or more `Markdown` cells to your notebook to explain its
  purpose and how it works.
* You should include comments on what you observed from your
  experiments in the previous step.
* For example, I might add the following Markdown to the top of my
  notebook to calculate cinema revenue:

```
# Cinema Sales Forecast

Forecasts the annual revenue from ticket sales at my cinema complex.
```
