---
title: PyNoon Starter Lesson 3 - Exercise
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

# PyNoon Starter: Lesson 3 - Exercise

## 1. Software Carpentry Exercises

(mostly from
[Lists](https://swcarpentry.github.io/python-novice-gapminder/11-lists.html))

## 1a. Spot the Difference

Predict what each of the print statements in the program below will
print.

```code
easy_string = "abc"
print(max(easy_string))
rich = "gold"
poor = "tin"
print(max(rich, poor))
print(max(len(rich), len(poor)))
```

## 1b. Indexing out of range

What happens when you index into a list with an index that is outside
of its range/length of elements? Try it and find out:

```code
letters = ['a', 'b', 'c']
letters[3]
```

Now also try:

* Retrieving a key from a dictionary that is not present in the
  dictionary.
* Making a slice from a list with bounds that are outside the range of
  the list.

### 1c. Dictionary Comprehensions

In the tutorial, we looked at list comprehensions, but we can also
construct dictionaries with dictionary comprehensions:

```code
user = {
    'first_name': 'Ben',
    'last_name': 'Smith',
    'city': 'Auckland',
    'country': 'New Zealand',
}

lowercase_user = {key: value.lower() for key, value in user.items()}
```

Rewrite the following code to use a dictionary comprehension to
construct `passing_percent_subject_scores`:

```code
subject_scores = {
    'Maths': 90,
    'Literature': 40,
    'Art': 70,
    'Science': 30,
}

passing_percent_subject_scores = {}
for subject, score in subject_scores.items():
    if score >= 50:
        passing_percent_subject_scores[subject] = score / 100
```

### 1d. Fill in the Blanks

Fill in the blanks so that the program below produces the output shown.

```code
values = ____
values.____(1)
values.____(3)
values.____(5)
print('first time:', values)
values = values[____]
print('second time:', values)
```

```
first time: [1, 3, 5]
second time: [3, 5]
```

### 1e. From Strings to Lists and Back

Given this:

```code
print('string to list:', list('tin'))
print('list to string:', ''.join(['g', 'o', 'l', 'd']))
```

```
string to list: ['t', 'i', 'n']
list to string: gold
```

1. What does `list('some string')` do?
2. What does `'-'.join(['x', 'y', 'z'])` generate?

### 1f. Sort and Sorted

What do these two programs print? In simple terms, explain the
difference between sorted(letters) and letters.sort().

```code
# Program A
letters = list('gold')
result = sorted(letters)
print('letters is', letters, 'and result is', result)
```

```code
# Program B
letters = list('gold')
result = letters.sort()
print('letters is', letters, 'and result is', result)
```

### 1g. Copying (or not)

What do these two programs print? In simple terms, explain the
difference between new = old and new = old[:].

```code
# Program A
old = list('gold')
new = old      # simple assignment
new[0] = 'D'
print('new is', new, 'and old is', old)
```

```code
# Program B
old = list('gold')
new = old[:]   # assigning a slice
new[0] = 'D'
print('new is', new, 'and old is', old)
```


## 3. Futurecoder

Complete the following lesson on [futurecoder.io](https://futurecoder.io):

1. If statements

> You can check which lesson you are up to on Futurecoder from the
> `Table of Contents` link at the top of the Futurecoder webpage.
