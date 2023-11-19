---
title: PyNoon Week 2 - Tutorial
---

## Variables

* `age = 42`
  * `=` symbol assigns the name on the left to refer to the value on the right
  * Variable is created when first assigned to
  * Variables are case-sensitive
* `age + 10`
* `first_name = 'Alice'`
* `print(first_name)`
* Be careful of cell order:
  * Move `print(first_name)` above `first_name = 'Alice'`
  * The print cell still works for now...
  * `Restart and run all`
* Be aware that the variable does not refer to a dynamic calculation, it refers
  to a value:
  ```
  a = 2
  b = 5 * a
  a = 3
  print(a)
  print(b)
  ```


## Types

### Checking the type

* Every value has a type
* We can use the `type()` function to find out what it is
* `type(42)` (integer)
* `type(age)`
  * Note: the value has a type, not the variable
* `type(42.0)` (float)
* `type(42 + 42.0)`
  * Maths with both integers and floats results in a float:
* `type(first_name)` (string)

### Operations vary by type

* The type of a value determines what operations we can perform with it
* `'hello' + 'world'`
* `'hello' - 'h'` (results in a `TypeError`)
* `len('hello')`
* `len(10)` (results in a `TypeError`)

### Operations with mixed types

* Some operations do not work with mixed types
* `1 + '1'`
* `'1' + '1'`
* We can convert values from one type to another
* `str(1) + '1'`
* Some operations do work with mixed types
* `'=' * 10`


## Indexing and Slicing

### Indexing

* We can use indexing to get particular characters from a string
* `first_name[0]`
* `first_name[1]`
* `first_name[-1]`

### Slicing

* We can use indexing to get part of a string
* `first_name[0:2]`
* The slice **includes** the first index, and **excludes** the last index
* The length of the slice is the difference of the two indexes
* Taking a slice does not change the contents of the original string,
  but returns a copy of part of the string:
  * Check `first_name`
* `first_name[1:2]`
* `first_name[:2]`
* `first_name[2:]`
* You can even index with variables:
* start_index = 3
* `first_name[start_index:]`

### DataFrames

* More generally, indexing and slicing work on any type that is an ordered list of elements.
* `import pandas as pd`
* `df = pd.read_csv('examples/data/iris.csv')`
* `df`
* `type(df)`
* `len(df)`
* `df.iloc[0]`
* `df.iloc[0:3]`
