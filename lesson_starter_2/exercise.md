---
title: PyNoon Starter Lesson 2 - Exercise
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

# PyNoon Starter: Lesson 2 - Exercise

## 1. Software Carpentry Exercises

(from [Variables and
Assignment](https://swcarpentry.github.io/python-novice-gapminder/02-variables.html)
and [Data Types and Type
Conversion](https://swcarpentry.github.io/python-novice-gapminder/03-types-conversion.html))

### 1a. Predicting Values

What is the final value of `position` in the program below? (Try to
predict the value without running the program, then check your
prediction.)

```code
initial = 'left'
position = initial
initial = 'right'
```

### 1b. Challenge

If you assign `a = 123`, what happens if you try to get the second
digit of a via a[1]?

### 1c. Automatic Type Conversion

What type of value is `3.25 + 4`?

### 1d. Strings to Numbers

Where reasonable, float() will convert a string to a floating point
number, and int() will convert a floating point number to an integer.
Run the following to see:

```code
print('string to float:', float('3.4'))
print('float to int:', int(3.4))
```

If the conversion doesn’t make sense, however, an error message will
occur. Try running:

```code
print('string to float:', float('Hello world!'))
```

Given this information, what do you expect the following program to do?

What does it actually do?

Why do you think it does that?

```code
print("fractional string to int:", int('3.4'))
```

### 1e. Arithmetic with Different Types

Which of the following will return the floating point number `2.0`?
Note: there may be more than one right answer.

```code
first = 1.0
second = "1"
third = "1.1"
```

1. `first + float(second)`
2. `float(second) + float(third)`
3. `first + int(third)`
4. `first + int(float(third))`
5. `int(first) + int(float(third))`
6. `2.0 * second`


### 1f. Slicing Practice

What does the following program print? Try to predict the answer
before running the code.

```code
atom_name = 'carbon'
print('atom_name[1:3] is:', atom_name[1:3])
```

### 1g. Slicing Concepts

Given the following string:

```code
species_name = 'Acacia buxifolia'
```

What would these expressions return? Try running them, as we didn't
cover all of these variations in the tutorial.

* `species_name[2:8]`
* `species_name[11:]` (without a value after the colon)
* `species_name[:4]` (without a value before the colon)
* `species_name[:]` (just a colon)
* `species_name[11:-3]`
* `species_name[-5:-3]`
* What happens when you choose a stop value which is out of range?
  (i.e., try `species_name[0:20]` or `species_name[:103]`)


## 2. Write a random password generator

Your next assignment is to write a random password generator. The
instructions below are to give you a framework for generating a
password, but feel free to get more creative!

### 2a. Set up a notebook

* Create a new notebook (or a Python script if you prefer)
* Give it a meaningful name
* Add a markdown cell (or comments in a script) to the top explaining
  that the purpose of this tool is to generate random passwords.

### 2b. Generate random numbers

* Your password should include a random number, which we can do with
  Python's `secrets` module.
* To load the `randbelow` function from the `secrets` module, run this
  code once in your notebook or script:

```code
from secrets import randbelow
```
* Then, you can call the function as follows to generate a random
  integer greater than or equal to `0` and below a specified limit number
  (in this case, `10`):
```code
randbelow(10)
```
* **Assign one or more random numbers to variables.**

### 2c. Add a random symbol

* Your password should include one or more random symbols.
* Declare a variable to store a sequence of possible symbols as follows:

```code
symbols = '!@#$%^&*()_+-='
```

* Use `randbelow()` to generate a random number, then use indexing
  with that number to pick a random symbol.
* Hint: Use the `len()` function on `symbols` as the limit number for
  your call to `randbelow()`
* **Assign one or more random symbols to variables.**

### 2d. Add a random sequence of letters

* Your password should include a random sequence of letters.
* Declare a variable to store a sequence of letters as follows:

```code
letters = 'abcdefghijklmnopqrstuvwxyz'
```

* Use `randbelow()` to generate two random numbers, then use slicing
  with those numbers to get a random slice from `letters`.
* Challenge: How can you ensure the first index is smaller than the
  second? Could you perform some maths with the numbers?
* **Assign one or more random string sequences to variables.**

### 2e. Combine the parts of your password

* Combine the random strings and numbers into a password, and store
  the result in a final variable called `password`
* To join strings and numbers together, you will first need to convert
  the numbers to strings with: `str(my_number_variable)`
* **Print the password to the screen for the user to save**


## 3. Futurecoder

Complete the following lesson on [futurecoder.io](https://futurecoder.io):

1. For Loops

> You can check which lesson you are up to on Futurecoder from the
> `Table of Contents` link at the top of the Futurecoder webpage.
