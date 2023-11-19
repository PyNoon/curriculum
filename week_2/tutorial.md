---
title: PyNoon Week 2 - Tutorial
---

* Make a new notebook
* What's the first thing to do? RENAME IT!
* Name it `week2.ipynb`

## Variables

* Quick recap on variables for those who haven't reached that part of
  the homework
* `height_cm = 180`
* `=` symbol assigns the name on the left to refer to the value on the right
* Now we use the variable anywhere we would have used the value
* `height_cm`
* `height_cm + 10`
* Python convention is to use snake_case
* Important: Variables are case-sensitive
* Variables are useful for:
  * Giving meaningful names to values
    * This is bad:
      ```
      height / 2.54
      ```
    * This is better:
      ```
      cm_per_inch = 2.54
      height_cm / cm_per_inch
      ```
    * Also note how helpful it is to include the units in the name
  * Storing the result of an operation for later use:
    ```
    cm_per_inch = 2.54
    height_inch = height_cm / cm_per_inch
    ```

<!-- * Be careful of cell order: -->
<!--   * Move `print(first_name)` above `first_name = 'Alice'` -->
<!--   * The print cell still works for now... -->
<!--   * `Restart and run all` -->
<!-- * Be aware that the variable does not refer to a dynamic calculation, it refers -->
<!--   to a value: -->
<!--   ``` -->
<!--   a = 2 -->
<!--   b = 5 * a -->
<!--   a = 3 -->
<!--   print(a) -->
<!--   print(b) -->
<!--   ``` -->


## Types

### Checking the type

* Now that we've looked at assigning values to variables, let's talk
  more about the values themselves
* In Python, every value has a type
* The type of a value determines what operations we can perform with it
* We can use the `type()` function to find out what it is
* `type(42)` (integer)
* An integer is a number without a decimal part
* `type(42.0)` (float)
* Float is the name Python and other programming languages use for
  numbers with decimal parts
* `type('hello')` (string)
* A string is a string of characters

### Operations vary by type

* The type of a value determines what operations we can perform with it
* `'hello' + 'world'`
* `'hello' - 'h'` (results in a `TypeError`)
* `len('hello')`
* `len(10)` (results in a `TypeError`)
* Different types also support different variables and functions
  attached to the value itself:
* `'hello'.upper()`
* `upper()` is a function like `print`, `type`, and `len`, but it
  doesn't take any arguments
* You can see what attributes and methods are available for a value:
* `dir('hello')`
  * Don't worry about the underscored names

### Operations with mixed types

Skip this section if short on time

* Some operations do not work with mixed types
* `1 + '1'`
* Functions are available to convert values from one type to another
* `str(1) + '1'`
* Some operations do work with mixed types
* `'<>' * 10`
* `type(42 + 42.0)`
  * What do you think the result will be?
  * Maths with both integers and floats results in a float
  * `42 + 42.0`


## Indexing and Slicing

### Indexing

* We can use indexing to get particular characters from a string
* `email = 'pynoon@example.com'`
* `email`
* `email[0]`
* `email[1]`
* `email[-1]`

### Slicing

* We can use indexing to get part of a string
* `email[0:2]`
* The slice **includes** the first index, and **excludes** the last index
* The length of the slice is the difference of the two indexes
* Taking a slice does not change the contents of the original string,
  but returns a copy of part of the string:
* `email`
* A more concrete example
* `at_index = email.find('@')`
* `at_index`
* `email[at_index]`
* `email[0:at_index]`
* `email[at_index:len(email)]`


### DataFrames

* More generally, indexing and slicing work on any type that is an ordered list of elements.
* `import pandas as pd`
* `df = pd.read_csv('examples/data/iris.csv')`
* `df`
* `type(df)`
* `df.iloc[0]`
* `df.iloc[0:3]`
* `len(df)`
* `df * 5`
