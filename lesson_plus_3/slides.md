---
title: PyNoon Plus Lesson 3
---

### Warm-Up Exercise

* Continue working on your Personal Python Project
* Pair up and review each other's project work
  * Without explaining your code, can they understand what each line
    achieves?
  * What changes would make it easier to read?
  * Do you have any suggestions to DRY out your partner's code?

### Thanks

* To the host for the great venue!
* To our sponsors

### Administrivia

* Fire escapes
* Toilets
* Cleaning up after ourselves
* WiFi


### Lunch Talk: Deploying Python Code

* Sharing a Jupyter notebook
* Users already have Python installed
* "Native" applications (e.g. desktop or mobile app)
* Python web applications
  * Beyond the scope of this course

### Sharing a notebook

<div style="font-size: 0.8em;">

* **Option 1:** Just send them the .ipynb file
  * They'll need to open it with Colab or Jupyter
* **Option 2:** Export an `html` or `pdf` file
  * Won't run Python code, just show the code and its results
  * `html` files can be opened in a web browser and retain plot interactivity
  * Use [nbconvert](https://saturncloud.io/blog/convert-google-colab-notebook-to-pdf-html/), e.g. to [export as `html`](example_notebook.html):
    ```
    !jupyter nbconvert --HTMLExporter.require_js_url "" --to html \
        "drive/MyDrive/Colab Notebooks/pynoon_plus_1.ipynb
    ```
* **Option 3:** Create an interactive web application
  * E.g. [Panel](https://panel.holoviz.org/), [Voilà](https://voila.readthedocs.io/), [Plotly Dash](https://dash.plotly.com/), [Streamlit](https://streamlit.io/)
  * You'll need a web server to host it

</div>

### Sharing a notebook

* **Option 4:** Create a runnable `html` file
  * A recent development; some Python libraries and functions won't work
  * E.g. [Panel convert](https://panel.holoviz.org/how_to/wasm/convert.html), [Voici](https://github.com/voila-dashboards/voici), [stlite](https://github.com/whitphx/stlite)
  * [pyscript](https://pyscript.net/) also lets you write Python directly in a html file (without a notebook)
  * We'll look at [Panel convert](https://panel.holoviz.org/how_to/wasm/convert.html) in today's tutorial

### Users already have Python installed

* **Option 1:** Make a runnable zip file: [zipapp](https://docs.python.org/3/library/zipapp.html)
* **Option 2:** Create a Python package
  * [Poetry](https://python-poetry.org/) or [Rye](https://rye-up.com/)
    makes packaging easy
  * Share the package as a pip-installable file
  * Publish on [pypi](https://pypi.org/) for anyone to install with `pip`
* Useful for:
  * Libraries of functions for other programmers
  * Command-line apps - e.g. Built with [argparse](https://docs.python.org/3/library/argparse.html)
  * Desktop/GUI apps - e.g. Built with [Tkinter](https://docs.python.org/3/library/tkinter.html)

### Packaging a "native" application

* Often a bit tricky...
* Lots of tools and libraries out there:
  * [PyInstaller](https://pyinstaller.org/en/stable/)
  * [cx_Freeze](https://marcelotduarte.github.io/cx_Freeze/)
  * [and more...](https://packaging.python.org/en/latest/overview/#bringing-your-own-python-executable)
* Cross-platform development (desktop + mobile):
  * [Kivy](https://kivy.org/doc/stable/)
  * [Beeware](https://beeware.org/)


### Tutorial Objectives

* Building user interfaces in Jupyter notebooks
* Deploying a notebook as an html file (web page)

### Independent Work/Homework

1. **Exercise Notebook:**
   * User interface practice
   * See the Exercise Notebook for PyNoon Plus Lesson 3 at
     [pynoon.github.io/schedule](https://pynoon.github.io/schedule)
2. Work on your own Python project
