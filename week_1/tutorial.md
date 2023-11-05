# Week 1

## Intro to Jupyter

Loosely based on
[https://swcarpentry.github.io/python-novice-gapminder/01-run-quit.html](https://swcarpentry.github.io/python-novice-gapminder/01-run-quit.html),
but using a more streamlined set of things to review (e.g. we don't
want to teach shortcut keys).

* Open our jupyterlite:
  [https://pynoon.github.io/jupyterlite](https://pynoon.github.io/jupyterlite)
  * You may have heard of Jupyter notebooks
  * Jupyterlite is a version of Jupyter that runs entirely in the browser
* **Python console**
  * Great for experimenting, doing quick calculations
  * `print('Hello world')`
  * `1 + 1`
  * Work in the console is lost when you close the console
* **Python scripts**
  * Ideal for creating re-usable programs
  * New tab -> new Python file -> rename to `hello.py`
  * Add `print('Hello world')`
  * Go back to your console and run: `%run hello.py`
  * Add `1 + 1`
    * Result isn't shown until we wrap it with `print()`
* **Notebooks**
  * Interactive like the console, re-usable like python scripts, and
    you can add formatted notes
  * Rename your notebook: `week1.ipynb`
  * `print('Hello world')`
  * Markdown: `# My First Notebook`
  * Notebooks support rich output, like plots:
    ```
    %pip install plotly nbformat pandas
    import plotly.express as px
    px.bar(x=['a', 'b', 'c'], y=[1, 2, 3])
    ```
  * Interact with the plot
  * Change the plot data and re-execute
  * Drag cells around
  * We'll primarily use notebooks, so that you can save the commands
    you run and add notes
* **Tip:** Download notebooks and python files to avoid data loss when
  clearing browser data

## Variables and Assignment

* Live code through: [https://swcarpentry.github.io/python-novice-gapminder/02-variables.html](https://swcarpentry.github.io/python-novice-gapminder/02-variables.html)
