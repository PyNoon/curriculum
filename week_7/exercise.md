---
title: PyNoon Week 7 - Exercise
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

# PyNoon Week 7 - Exercise

## 1. User Interface Practice

* Build your own user interface for some task
* For example:
  * To capture user input for your project
  * To provide a search box or category for filtering the AirBnB
    listings data
  * To call some other AI model, such as a text summarisation model:
    https://huggingface.co/facebook/bart-large-cnn
* Use the pattern from the tutorial of building the user interface as
  a function.
  * Separate out any "business logic" into separate functions that are
    passed as arguments to the form.
  * Add comments and a function docstring to make the purpose of your
    user interface clear.

### Pandas + Plotly +  Example

To help you get started, look at the following example that allows the
user to upload a CSV, and then uses Pandas and Plotly to create a plot
from its contents.

> Note: The file-upload widget won't work correctly within Colab or
> Jupyterlite, but it will work correctly from the exported html app.
> You may find it useful to prototype your app in Colab using a file
> loaded from the file browser, and then re-use functions from your
> prototype to create the final html app interface.

```code
from io import BytesIO
import pandas as pd
import panel as pn
import plotly.express as px

# To use plotly with Panel, we must load the plotly extension
pn.extension('plotly')

# Create a file-upload field that accepts a csv file
file_field = pn.widgets.FileInput(accept='.csv')

def on_upload(file_value):
    # If no file has been uploaded yet, do nothing
    if not file_value:
      return

    # Load the file's contents into a Pandas DataFrame
    df = pd.read_csv(BytesIO(file_value))
    # Return a Plotly histogram of the first column in the DataFrame
    # We must explicitly specify a width for the plot.
    first_column = df.columns[0]
    return px.histogram(df, x=first_column, width=500)

# Call on_upload when a file is uploaded
output = pn.bind(on_upload, file_field)

layout = pn.Column(
    file_field,
    output,
)
layout.servable()
```

## 2. Futurecoder

Complete the following lesson on
[futurecoder.io](https://futurecoder.io):

1. Dictionaries (note: this lesson is at the end of the Futurecoder
   course, so you will need to skip ahead using the Table of Contents)

> You can check which lesson you are up to on Futurecoder from the
> `Table of Contents` link at the top of the Futurecoder webpage.
