---
title: PyNoon Data Lesson 4 - Exercise
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

# PyNoon Data: Lesson 4 - Exercise

## 1. Function and DRY Exercises

### 1a. Extend `get_above_average_listings_df` support both mean and median average

Extend the function `get_above_average_listings_df` from this lesson's
tutorial with an additional argument that will allow the caller of the
function to choose whether a `mean` or `median` average is used.

### 1b. Checking for valid sudoku solutions

A [sudoku](https://en.wikipedia.org/wiki/Sudoku) puzzle is constructed
on a 9x9 grid of digits, which is divided into nine 3x3 *boxes* (3
across by 3 down). A solution to a sudoku puzzle is only valid if
every column, row, and box contains the full set of digits 1-9,
without duplicates.

For example, the puzzle below is a valid solution:

```code
valid_puzzle = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9],
]
```

This puzzle, on the other hand, is not a valid solution because the
first row, the first column, and the top-left box all contain
duplicates of the `1` digit:

```code
invalid_puzzle = [
    [1, 1, 1, 6, 7, 8, 9, 1, 2],
    [1, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9],
]
```

Given the following definition for the `check_sudoku_valid` function
below, your task is to define the following three functions that it
uses:

* `get_puzzle_row`
* `get_puzzle_column`
* `check_digits_valid`

A "stub" definition is provided for each function, showing the
arguments it should accept and providing a docstring describing its
intended behaviour. You need to replace each `TODO` with code for the
body of the function.

```code
def check_sudoku_valid(puzzle):
    """Returns True if the given puzzle is a valid sudoku solution,
    where all rows, columns, and boxes contain all digits 1-9 without
    repetition.

    Args:
        puzzle: A list containing lists of rows containing digits.

    Returns:
        A Boolean value indicating whether or not the sudoku puzzle is
        a valid solution.

    """
    for row_index in range(9):
        if check_digits_valid(get_puzzle_row(puzzle, row_index)):
            return False
    for column_index in range(9):
        if check_digits_valid(get_puzzle_column(puzzle, column_index)):
            return False
    for box_index in range(9):
        if check_digits_valid(get_puzzle_box(puzzle, box_index)):
            return False
    return True

def get_puzzle_row(puzzle, index):
    """Returns a single row at the given index from the given sudoku puzzle."""
    TODO

def get_puzzle_column(puzzle, index):
    """Returns a single column at the given index from the given sudoku puzzle."""
    TODO

def get_puzzle_box(puzzle, index):
    """Returns a list of digits in a single box at the given index from the
    given sudoku puzzle. Boxes are indexed from left-to-right and top-to-bottom."""
    TODO

def check_digits_valid(digits):
    """Returns True if the given list of digits contains the set of digits 1-9
    without duplicates."""
    TODO

```

<!--
```
def get_puzzle_row(puzzle, index):
    """Returns a single row at the given index from the given sudoku puzzle."""
    return puzzle[index]

def get_puzzle_column(puzzle, index):
    """Returns a single column at the given index from the given sudoku puzzle."""
    return [row[index] for row in puzzle]

def get_puzzle_box(puzzle, index):
    """Returns a list of digits in a single box at the given index from the
    given sudoku puzzle. Boxes are indexed from left-to-right and top-to-bottom."""
    row_start_index = (index % 3) * 3
    col_start_index = (index // 3) * 3
    return [
        puzzle[row_start_index + row_index][col_start_index + col_index]
        for col_index in range(3)
        for row_index in range(3)
    ]

def check_digits_valid(digits):
    """Returns True if the given list of digits contains the set of digits 1-9
    without duplicates."""
    return sorted(digits) == list(range(1, 10))
```
-->

> Defining a function like `check_sudoku_valid` before implementing
> the functions it depends on is an example of [**top-down
> design**](https://en.wikipedia.org/wiki/Bottom%E2%80%93up_and_top%E2%80%93down_design),
> which is a helpful strategy for designing programs by breaking the
> task down into sub-tasks before figuring out how to implement each
> sub-task. Notice how the the resulting code in `check_sudoku_valid`
> reads similarly to the plain-text description of its behaviour in
> its docstring.

**Optional bonus task:** The definition of `check_sudoku_valid` itself
seems to contain some blocks of similar code. Can you reduce the
duplication of code in this function?

### 1c. Writing tests

* Write assert statements to test that `get_above_average_listings_df`
  and the sudoku functions produce the results you would expect for
  different arguments.
* Try to think of tests that might cause the function
  to produce an unexpected result. For example:
  * *edge cases* - values at or near the point that would trigger a
    behaviour change. Typically values such as `0`, `1`, or `-1`.
  * Very large or very small values.
  * Values that are the wrong type.

### 1d. Reducing duplication in previous code

* Go back through your code from previous exercises and look for
  opportunities to simplify your code with functions, loops, and list
  comprehensions.
* Carefully consider whether or not using these techniques would make
  the code more readable and maintainable.

## 2. Futurecoder

Complete the following lesson on
[futurecoder.io](https://futurecoder.io):

1. Dictionaries (note: this lesson is at the end of the Futurecoder
   course, so you will need to skip ahead using the Table of Contents)

> You can check which lesson you are up to on Futurecoder from the
> `Table of Contents` link at the top of the Futurecoder webpage.
