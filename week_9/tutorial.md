---
title: PyNoon Week 9 - Tutorial
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

This week's tutorial will cover use of AI models, loading data from
text files, and constructing DataFrames.

## Setup

1. Make a new notebook for this week
2. What's the first thing to do? RENAME IT!
3. Name it `week9.ipynb`

## Using AI models from Python

* [huggingface.co](https://huggingface.co/) has LOTS of AI *models*
  available for different tasks that we can download and use.
  * Many are free to use, even for commercial purposes.
* Let's use an AI model to assign a label to a string of text!
* Specifically, we'll use a zero-shot classification model that picks
  which of a provided list of labels best fits a text snippet we
  provide.
  * Zero-shot means we don't need to provide examples of text snippets
    for our labels

> Normally we'd have to install `transformers` and its dependency
> `torch` using `pip`, but Colab already has these installed.

* Downloading and preparing the classifier is very straightforward.
* The model will be downloaded to the Colab instance running on
  Google's servers - not your computer.

```code
from transformers import pipeline

classifier = pipeline('zero-shot-classification', model='facebook/bart-large-mnli')
```

* Applying the classifier to a snippet of text is similarly easy:

```code
classifier(
    'one day I will see the world',
    candidate_labels=['travel', 'cooking', 'technology'],
)
```

* The output is given as a dictionary, containing a list of labels
  ordered from most likely to least likely, as well as a list of
  *scores* for those labels, indicating the model's confidence in
  assigning each label to the text.
* We can see that the model thinks that `travel` is the best fit,
  which seems reasonable.
  * Though AI models won't always give reasonable responses!
* Let's create a function that we can use to call the classifier with
  a single argument - the text to classify:

```code
def classify_text(text_to_classify):
    result = classifier(
        text_to_classify,
        candidate_labels=['travel', 'cooking', 'dancing'],
    )
    return result['labels'][0]

classify_text('one day I will see the world')
```

## Processing a text file to produce a DataFrame

* Now let's classify a text file of blog post titles to produce a
  DataFrame of rows containing each title and label
* Download `titles.txt` from:
  [pynoon.github.io/curriculum/week_9/titles.txt](https://pynoon.github.io/curriculum/week_9/titles.txt)
* Click the folder icon on the left side of the Colab interface, then
  use the upload button to upload `titles.txt`
* **ALTERNATIVELY:**
  * Click the folder icon on the left side of the Colab interface, then
    right-click and select `New file`
  * Right-click and select `Rename file` to name it `titles.txt`
  * Double-click the file to open it, and enter the following content:
    ```
    My weekend in Queenstown
    When to plant tomatoes
    Recommendations for 2024's best TVs
    The fastest ever cookie recipe
    ```
  * `Ctrl-s` to save the file.

* Now, we can use `open()` to load the file
* `open()` should be used with a `with` statement so that the file is
  automatically closed when we're finished with it:

```code
with open('titles.txt') as titles_file:
    titles = titles_file.readlines()
```

`.readlines()` has provided us with a list of strings representing
each line in the file:

```code
titles
```

We can use a list comprehension to transform each value in a list:

```code
[classify_text(title) for title in titles]
```

We can use a list comprehension to construct a list of dictionaries,
where each dictionary contains the title and its label:

```code
title_details = [
    {
        'title': title,
        'label': classify_text(title),
    }
    for title in titles
]
title_details
```

* `pd.DataFrame` can be used to construct a DataFrame from a list of
  dictionaries like `title_details`.
* Each dictionary should represent the values for each column in a
  given row.

```code
import pandas as pd

title_df = pd.DataFrame(title_details)
title_df
```

* Processing a text file line-by-line to construct a DataFrame like
  this is a common pattern that is useful in many situations.
