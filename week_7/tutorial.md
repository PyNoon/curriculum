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

To get started, let's import the `panel` module that provides widgets
for building user interfaces

* Usually installed with `%pip install panel`, but it's pre-installed
  in Colab.
* We also need to call `pn.extension()` to finish loading panel.

```code
import panel as pn

pn.extension()
```

Now let's make a text field:

```code
text_field = pn.widgets.TextInput()
```

We can display it:

```code
text_field
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
submit_button = pn.widgets.Button(name='Submit')
submit_button
```

* We can use `pn.bind()` to assign a "callback" function that should
  be called whenever the button is clicked.

```code
submit_button = pn.widgets.Button(name='Submit')

def on_submit(event):
    if not event:
        return

    return text_field.value

submit_output = pn.bind(on_submit, submit_button)

pn.Column(
    submit_button,
    submit_output,
)
```

* The value returned by `pn.bind()` will display outputs returned by
  the callback.
  * We display the button and output together by wrapping them in a
    `pn.Column`.
  * `pn.bind()` can also bind functions to any widget updates, like
    text box changes.
* Note that the function we provide must accept a single argument that
  will contain details of the button click "event".
  * The callback will be called once initially, but the argument
    passed to it will only contain a value when the button has been
    clicked.

Each time you click the button, the current value of the text input
is displayed.

## Bringing it all together a self-contained form

* Use a consistent structure:
  * Start by defining widgets.
  * Then define and bind event handlers.
  * Then define a layout that includes all of the widgets to be
    displayed.
* If your interface gets too big, consider splitting it up into
  functions

```code
text_field = pn.widgets.TextInput()
submit_button = pn.widgets.Button(name='Submit')

def on_submit(event):
    if not event:
        return

    return text_field.value

submit_output = pn.bind(on_submit, submit_button)

layout = pn.Column(
    text_field,
    submit_button,
    submit_output,
)
layout
```

## Deploying our app

* One way we can share a `panel` application with users is to convert
  it to a shareable `.html` file.
* `html` is the language web pages are written in, so any user will be
  able to open the file in their web browser.
* Recent developments in web and Python technologies allow us to
  create `html` files that can run Python code.

### Preparing the app notebook

* Make a new notebook, call it `week7_app.ipynb`
* Add from above:

```code
import panel as pn

pn.extension()

...interface...

layout.servable()
```

* Make sure your `layout` ends with `.servable()`
  * This tells panel what components make up the "app"
* Save the file

### Converting the app notebook to html

From your original notebook (important to avoid including the `!panel
convert` line in your app notebook):

* Click on the file browser in the left-hand sidebar, and select the
  button to `Mount Drive`
* Add a notebook cell to run:

```code
!panel convert "drive/MyDrive/Colab Notebooks/week7_app.ipynb" --to pyscript --out app_output
```

* Refresh the file browser
* From the file browser, download `app_output/week7_app.html`
* Open `week7_app.html` in your web browser to use your app!


## Going further with user interfaces

* Look at the [`panel` documentation](https://panel.holoviz.org/index.html)
  * See what input widgets are available (under `Component Gallery` ->
    `Widgets` in the documentation sidebar)
  * See what rich outputs are available (e.g. Plotly plots, under
    `Component Gallery` -> `Panes` in the documentation sidebar)
* Other user interface libraries exist for:
  * Notebook and web apps
    * [ipywidgets](https://ipywidgets.readthedocs.io/en/stable/)
    * [Streamlit](https://streamlit.io/)
    * [Plotly Dash](https://dash.plotly.com/)
  * Desktop apps (less popular these days)
    * [Tkinter](https://docs.python.org/3/library/tkinter.html)
    * [PyQt](https://wiki.python.org/moin/PyQt)


<!--

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

-->
