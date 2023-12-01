---
title: PyNoon Week 1 - Tutorial
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

# Intro to JupyterLite

The following tutorial is an introduction to writing and running
Python code in the JupyterLite environment, loosely based on
[swcarpentry.github.io/python-novice-gapminder/01-run-quit.html](https://swcarpentry.github.io/python-novice-gapminder/01-run-quit.html),
(but more streamlined - not covering topics like shortcut keys).

> The remainder of this course will use [Google
> Colab](https://colab.google/) for running Python notebooks, but this
> tutorial uses JupyterLite to demonstrate use of the Python console,
> Python scripts, and Python notebooks.

**To get started open the PyNoon JupyterLite environment at:
[pynoon.github.io/jupyterlite](https://pynoon.github.io/jupyterlite)**

* You may have heard of Jupyter notebooks
* JupyterLite is very similar to a piece of software called JupyterLab
  that is used to run Jupyter's Python notebooks - a popular format
  for writing Python code that we will be using in this course.
* The benefit of JupyterLite is that it runs entirely inside your web
  browser, meaning you don't need to install Python, JupyterLab, or
  any other software on your computer.

In this tutorial, we will look at three ways of running Python code
inside JupyterLite:

* The Python console
* Python scripts
* Python notebooks

## The Python Console

* The Python console is great for running short snippets of Python
  code
* Use it to experiment and play with Python to learn more about how it
  works
* It's also useful as a general purpose calculator

**Open a Python Console**: From the JupyterLite Home/Launcher page,
under `Console`, select `Python`

In the prompt at the bottom of the Console screen, enter the following
code, then hold the `shift` key and press the `enter` key to run it:

```code
print('Hello world')
```

Congratulations! You've just run your first Python program!

> Note: Casing is important in Python, so make sure you write `print`
> in lower-case.

We can also use Python to perform maths; try running the following:

```code
1 + 1
```

```code
5 - 3
```

> Note: The spaces around mathematical operators are optional, but
> they are important to make the code more readable!

**It is important to remember that any work you do in the console is
lost when you close the console.**


## Python scripts

Python scripts are ideal for creating re-usable programs.

**To create a new script in JupyterLite:**

* Click the `+` button next to the current tab to open a new Tab/Launcher
* Under `Other` select `Python file`
* Right click on the tab of your new file, and rename it to `hello.py`
  * **It is very important to give your files useful names so that you
    know what they contain when you or others come back later.**
  * The `.py` extension says that this is a plain-text file (like one
    you could edit with notepad) containing Python code.

Write the following code to your script:

```code
print('Hello world')
```

**Remember to save the file: Hold the `Ctrl` key and press the `s` key**

* If you don't save your changes, the old version of your code will be
  used when you run the script.
* You can always tell the file isn't saved yet by the black dot over
  the "close tab" button

Go back to your Console tab (or open a new one), and run:

```code
%run hello.py
```

You should see `Hello world` printed again in the console.

> Note: You can view the script and Console at the same time by
> clicking and dragging the Console tab to the right-hand side of the
> screen.


Now try adding a new line to your script with the following code:

```code
1 + 1
```

Save the script and run it again at the console

> Tip: You can press the "up arrow" key in the Console to bring up
> lines you've previously run (saving you from typing them again).

When you run your script, you won't see the result of `1 + 1`.

This is because **Python scripts only output what we explicitly tell
Python to print!**


To print the result of `1 + 1`, change the line in your script to be:

```code
print(1 + 1)
```

Save the script and run it again at the console, and you should see
the following output:

```
Hello world
2
```


## Python Notebooks

Python notebooks are:

* Interactive like the Console
* Re-usable like scripts
* Support rich formatting of notes and outputs

**To create a new notebook in JupyterLite:**

* Click the `+` button next to the current tab to open a new Tab/Launcher
* Under `Notebook` select `Python`
* Right click on the tab of your new file, and rename it to `week1.ipynb`

In the "cell" prompt at the at the top of your notebook, enter the
following code, and run it with `shift + enter` (like at the Console):

```code
print('Hello world')
```

The result is printed and a new "cell" appears below.

Run this code in the new cell:

```code
1.5 + 10
```

Each time you press `shift+enter`, a new cell is created

**You can edit and re-run cells;** update your previous cell to have
the following content, then re-run it:

```code
(1.5 * 10) / (5 - 2)
```

> Note that we can use `*` for multiplication, `/` for division`, and
> group operations with parentheses `()`.

**You can add non-code cells for formatted notes:**

* Click into the empty cell at the end of the notebook
* Change the dropdown at the top of the page from `Code` to `Markdown`
* Add the following content:

```
My First Notebook
```

* Press `shift+enter`, and see the text displayed.

**You can add formatting in Markdown cells:**

* Double-click `My First Notebook` to edit the cell
* Add a `#` at the beginning of the line:

```
# My First Notebook
```

* Press shift-enter and see it formatted as a heading

**Markdown code is similar to shortcuts supported by software like
Slack and Teams**

For example, add a bullet list with:

```
* item 1
* item 2
* item 3
```

* To see what else is possible with Markdown, see:
  [www.markdownguide.org/](https://www.markdownguide.org/)

**You can re-order notebook cells**

* Hover your mouse to the left of your Markdown cell until you see a
  four-way arrow
* Click and drag your cell to the top of the notebook to act as a
  title

**Notebooks also support rich output from Python code**

* Run a cell with the following code (you don't need to understand the
  code yet):

```code
%pip install plotly nbformat pandas
import plotly.express as px
px.bar(x=['a', 'b', 'c'], y=[1, 2, 3])
```

**You should see an interactive plot**

* Scroll to zoom
* Click and drag to zoom to a selection
* Double click to reset zoom
* Find the camera button in the plot header to download the plot as an
  image

Try changing `y=[1, 2, 3]` in your cell to use different numbers, then
re-execute the cell.

* Notebooks are really good for presenting the results of your code -
  they very popular in data science and just for data exploration
* We'll primarily use notebooks in this course so that you can save
  the commands you run and add notes

> Tip: You should right-click and download your notebooks and Python
> files from the left-hand sidebar to avoid data loss when your
> browser's data is cleared
