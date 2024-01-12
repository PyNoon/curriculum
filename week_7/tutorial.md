---
title: PyNoon Week 7 - Tutorial
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

This week's tutorial will cover building user interfaces in Jupyter
notebooks, and using an off-the-shelf AI model.

## Setup

1. Make a new notebook for this week
2. What's the first thing to do? RENAME IT!
3. Name it `week7.ipynb`

## UI Widget Basics

To get started, let's import:

* The `ipywidgets` module that provides widgets for building user
  interfaces.
* A `display` function for displaying the widgets.

```code
from IPython.display import display
import ipywidgets as widgets
```

Now let's make a text field:

```code
text_field = widgets.Text()
```

We can use `display` to display it:

```code
display(text_field)
```

And we can get the current contents of the field:

```code
text_field.value
```

* Try entering some text, then re-run `text_field.value`.
* See that the value has changed.

## Buttons

Now let's make a button:

```code
submit_button = widgets.Button(description='Submit')
display(submit_button)
```

* We can use `on_click()` to assign a function that should be called
  whenever the button is clicked.
* Note that the function we provide must accept a single argument that
  will contain details of the button click "event".
  * We generally won't need to use the `event`, but the function must
    still accept it.

```code
submit_button = widgets.Button(description='Submit')

def on_submit(event):
    print('hello')

submit_button.on_click(on_submit)

display(submit_button)
```

* Each time you click the button, `hello` is printed again.
* But what if we want to replace the printed text each time the button
  is clicked?
* We can print to our own `Output()` widget:
* When the submit handler runs, we:
  1. Clear any current contents of the `output`.
  2. Use `with output:` to capture any printed or displayed content
     and add it to the contents of `output`.
* We must make sure we display the `output` widget itself.

```code
submit_button = widgets.Button(description='Submit')
output = widgets.Output()

def on_submit(event):
    output.clear_output()
    with output:
        print('hello')

submit_button.on_click(on_submit)

display(
    submit_button,
    output,
)
```

## Building a self-contained form

* Now let's write a function to keep all of our interface code
  together
  * Because all of the variables are defined inside the function, they
    will not overwrite other variables outside the function.
* Use a consistent layout:
  * Start by defining widgets.
  * Then define and assign event handlers.
  * Then return a *layout* widget that wraps up all of the widgets to
    be displayed.
    * Instead of displaying the interface, `ui_form()` will return a
      widget that we can display as we please.
    * This is particularly useful for creating nested interface
      functions.

```code
def user_interface():
    text_field = widgets.Text()
    submit_button = widgets.Button(description='Submit')
    output = widgets.Output()

    def on_submit(event):
        output.clear_output()
        with output:
            print(text_field.value)

    submit_button.on_click(on_submit)

    return widgets.VBox([
        text_field,
        submit_button,
        output,
    ])

display(user_interface())
```

## Using

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

## Separating Logic from Interface

* Now let's make our interface classify the entered text whenever the
  submit button is clicked.
* Instead of changing our interface to call the classifier, let's make
  the user interface accept *any* function that can transform the
  entered text into some output.
* This will:
  * Logically separate our interface code from our "business logic".
  * Make our form re-usable for different actions.
  * Make it easier to test both our interface and classifier.

> For those interested, this is an example of the [**dependency
> inversion**](https://en.wikipedia.org/wiki/Dependency_inversion_principle)
> design principle.

```code
def user_interface(produce_output):
    text_field = widgets.Text()
    submit_button = widgets.Button(description='Submit')
    output = widgets.Output()

    def on_submit(event):
        output.clear_output()
        with output:
            display(produce_output(text_field.value))

    submit_button.on_click(on_submit)

    return widgets.VBox([
        text_field,
        submit_button,
        output,
    ])

display(user_interface(produce_output=classify_text))
```

## Going further with user interfaces

* Look at the [available ipywidgets](https://ipywidgets.readthedocs.io/en/stable/examples/Widget%20List.html)
* There are tools that can turn notebooks into web applications:
  * [Voila](https://voila.readthedocs.io/)
  * [Panel](https://panel.holoviz.org/index.html)
* Other user interface libraries exist for:
  * Web apps
    * [Streamlit](https://streamlit.io/)
    * [Plotly Dash](https://dash.plotly.com/)
  * Desktop apps (less popular these days)
    * [Tkinter](https://docs.python.org/3/library/tkinter.html)
    * [PyQt](https://wiki.python.org/moin/PyQt)
