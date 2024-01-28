# Week 9

* Futurecoder:
  * Tic Tac Toe Project

# Week 10

* How to continue learning


# Other Topics

* Importing Python functions from a Python file
* Documentation
* Version control
* Deployment
* Structuring a project
* Debugging
* dataclasses
* sqlite
* wordcloud
* regexes
* OOP


<!--
### DataFrame Indexing and Slicing

* The first "column" in the DataFrame is the *index*, which defaults to incrementing
  integers
* Like how each column has a name, the *index* is the "name" of each
  row
* We can assign a column to be the index of a DataFrame:

```code
listings_df = listings_df.set_index('id')
```

```code
listings_df
```

Why do we need to assign the result of `set_index()`?

* Calling `.set_index()` does not change the original DataFrame value
* Calling `.set_index()` returns a **new DataFrame value** with the
  index changed, which we then assign to the original variable.
* Most Pandas methods return a new value rather than changing the
  original value.


**We can perform indexing and slicing on DataFrames using `.iloc`:**

To get the first row:

```code
listings_df.iloc[0]
```

To get the second column in the first row:

```code
listings_df.iloc[0, 1]
```

To get the second column of the first five rows:

```code
listings_df.iloc[0:5, 1]
```

To get the second column of all rows:

```code
listings_df.iloc[:, 1]
```

**We can also index and slice rows and columns by their names:**

To get a single row by it's name in the index:

```code
listings_df.loc['l9995141']
```

To get several rows by their names:

```code
listings_df.loc[['l9995141', 'l12026015', 'l44688136']]
```

> While you can use `:` slicing to specify a start and end names for a
> range, it is more common to specify a list of names.

To get the `name` column of all rows:

```code
listings_df.loc[:, 'name']
```
-->

<!-- WEEK 9 - AI -->

<!--
## 1d. Selection of Individual Values

Use sorting and indexing on `listing_df` to find:

1. The value in the third column of the fifth row.
2. The `name` of the listing with an `id` of `'l6113'`
3. The `review_scores_rating` of the most reviewed listing.
4. The `latitude` and `longitude` of the least expensive listing.
-->

<!--

### Lunch Talk: AI-Assisted Python Programming

* ChatGPT, GitHub Copilot, etc. are quite good at generating Python code
* Will programming become obsolete?
* Do's/Dont's of programming with AI

### Will programming become obsolete?

<div style="font-size: 0.7em; display: flex; align-items: center;">

* Probably not
* If anything, programming is more important to "glue" AI to
  data/systems
* AI-generated code often needs fixing - **you still need to know how to
  fix it**
* The essence of programming is about *precisely* instructing a
  computer - you still need to carefully **consider** and
  **communicate** those instructions

<div>
<img src="well.png" style="width: 1400px; margin: 0;">
<a href="https://xkcd.com/568/">xkcd.com/568</a>
</div>

</div>

### Do's/Dont's of programming with AI

* **DON'T** feed confidential data into public AI tools
* **DON'T** use generated code you don't understand
* **DON'T** use it to replace reading documentation
* **DO** ask it to explain code (as *one* perspective)
* **DO** use it generate snippets for specific tasks
* **DO** be specific in your instructions/requirements
* **DO** ask it to try fix code when the result is wrong

-->

<!--

## Using AI models from Python

* Now we'd like to make our form do something.
* Let's get it to use an AI model to assign a label to our text!
* [huggingface.co](https://huggingface.co/) has LOTS of AI models
  available for different tasks that we can download and use.
* In this case, we'll use a zero-shot classification model that picks
  which of a provided list of labels best fits a text snippet we
  provide.

> Normally we'd have to install `transformers` and its dependency
> `torch` using `pip`, but Colab already has these installed.

```code
from transformers import pipeline

classifier = pipeline('zero-shot-classification', model='facebook/bart-large-mnli')

text_to_classify = 'one day I will see the world'
classifier(
    text_to_classify,
    candidate_labels=['travel', 'cooking', 'dancing'],
)
```

* We can see that the model thinks that `travel` is the best fit,
  which seems reasonable.
  * Though AI models won't always give reasonable responses!
* The output is given as a dictionary, which you'll learn more about
  in this week's Futurecoder lesson.
* Let's create a function that we can use to call the classifier with
  a single argument - the text to classify:

```code
from transformers import pipeline

classifier = pipeline('zero-shot-classification', model='facebook/bart-large-mnli')

def classify_text(text_to_classify):
    return classifier(
        text_to_classify,
        candidate_labels=['travel', 'cooking', 'dancing'],
    )

classify_text('one day I will see the world')
```

-->
