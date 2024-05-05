---
title: PyNoon Starter Lesson 1 - Tutorial
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

# Intro to Python Coding

The following tutorial is an introduction to writing and running
Python code in the [futurecoder.io](https://futurecoder.io/) and
[Google Colab/Jupyter](https://colab.google) environments, loosely
based on
[swcarpentry.github.io/python-novice-gapminder/01-run-quit.html](https://swcarpentry.github.io/python-novice-gapminder/01-run-quit.html),
(but more streamlined - not covering topics like shortcut keys).

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

**Open a Python Console in Futurecoder**:

* Visit [futurecoder.io](https://futurecoder.io/)
* Click the link that says "Just code"
* You will see the Console on the right-side of the screen, indicated
  by the `>>>` (three angle brackets) called the *prompt*.
* Click anywhere in the Console to be able to type into it.

Enter the following code, then press the `enter` key to run it:

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
lost when you close the console (or refresh the futurecoder
webpage).**

> Tip: You can press the "up arrow" key in the Console to bring up
> lines you've previously run (saving you from typing them again).


## Python scripts

Python scripts are ideal for creating re-usable programs.

* You can write a Python script in the left-hand side of the screen of
  the futurecoder interface.
* Click on the left-hand side of the screen to be able to type your
  script into it.
* Write the following code in your script:

```code
print('Hello world')
```

* Press the `Run` button to run your script
* You should see `Hello world` printed again in the console.
* Now try adding a new line to your script with the following code:

```code
1 + 1
```

* Now run it again.
* When you run your script, you won't see the result of `1 + 1`.
* This is because **Python scripts only output what we explicitly tell
  Python to print!**
* To print the result of `1 + 1`, change the line in your script to
  be:

```code
print(1 + 1)
```

* Run the script again and you should see the following output:

```
Hello world
2
```

* If you refresh or close and re-open futurecoder, the last script you
  wrote will be saved.
* To save your scripts for future use, copy and save them save them
  somewhere else.

> Running python scripts locally: You can use a *plain text editor*
> (e.g. Notepad, Notepad++, Visual Studio Code) to create a Python
> script file that ends in a `.py` extension. If you have Python
> installed on your computer, you can run your script from the
> Terminal/Command Prompt with `python my_script.py` (assuming you
> have used `cd` commands to move your terminal session into the same
> folder as `my_script.py`). It is is important to remember to save
> changes to your script files before you re-run them!


## Python Notebooks

* You may have heard of Jupyter notebooks, as they are a very popular
  platform for Python coding, particularly for data analysis and
  visualisation.
* We will create Jupyter notebooks in Google Colab, which is a service
  that will allow us to run Jupyter notebooks without installing
  Python or Jupyter on your own computer.
* Note: Because your notebooks will run on Google's servers, you
  shouldn't upload any company data or code you are not authorised to
  use outside of company-approved systems.
* Jupyter notebooks can also be run on your own desktop or server with
  a piece of software called JupyterLab - a popular format for writing
  Python code that we will be using in this course.
* Python notebooks are:
  * Interactive like the Console
  * Re-usable like scripts
  * Support rich formatting of notes and outputs

**To create a new notebook in Google Colab:**

* Open [colab.google](https://colab.google) in your web browser
* Click the `New Notebook` link
* Click on the title at the top of the page, and rename it
  `pynoon_starter_1.ipynb` - helpful names are important!

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

* Click the `+ Text` button at the top of the notebook
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

* Click on a cell you want to move up or down in the notebook
* Click on the up/down arrows that appear in the top-right of the
  cell.

**Notebooks also support rich output from Python code**

* Run a cell with the following code (you don't need to understand the
  code yet):

```code
%pip install plotly nbformat pandas
import plotly.express as px
px.bar(x=['a', 'b', 'c'], y=[1, 2, 3])
```

**You should see an interactive plot**

* Click and drag to zoom to a selection
* Double click to reset zoom
* Find the camera button in the plot header to download the plot as an
  image

Try changing `y=[1, 2, 3]` in your cell to use different numbers, then
re-execute the cell.

* Notebooks are really good for presenting the results of your code -
  they are very popular in data science and just for data exploration
* We'll primarily use notebooks in this course so that you can save
  the commands you run and add notes

> Note: Your notebooks will all be saved to your Google Drive account,
> you can find previous notebooks from the `File -> Open notebook`
> menu.
