---
title: PyNoon Week 1 - Tutorial
---

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
  * `5 - 3`
  * Work in the console is lost when you close the console
* **Python scripts**
  * Ideal for creating re-usable programs
  * New tab -> new Python file -> rename to `hello.py`
  * Add `print('Hello world')`
  * Save the file with `Ctrl + S`
    * We can tell the file isn't saved yet by the black dot over the
      close-tab button
  * Go back to your console and run: `%run hello.py`
  * Add `1 + 1`
    * Result isn't shown until we wrap it with `print()`
* **Notebooks**
  * Interactive like the console, re-usable like python scripts, and
    you can add formatted notes
  * Rename your notebook: `week1.ipynb`
  * `print('Hello world')`
  * `1.5 * 10`
  * Each time you press shift+enter, a new cell is created
  * Edit and re-run a cell: `(1.5 * 10) / (5 - 2)`
  * Markdown: `My First Notebook`
  * Add markdown formatting: `# My First Notebook`
  * Similar to Teams/Slack: Add a bullet list
  * Drag cells around
  * Notebooks support rich output, like plots:
    ```
    %pip install plotly nbformat pandas
    import plotly.express as px
    px.bar(x=['a', 'b', 'c'], y=[1, 2, 3])
    ```
  * Interact with the plot
  * Change the plot data and re-execute
  * Notebooks are really good for presenting the results of your
    code - very popular in data science and just for data exploration
  * We'll primarily use notebooks, so that you can save the commands
    you run and add notes
* **Tip:** Download notebooks and python files to avoid data loss when
  clearing browser data

## Variables and Assignment

* Live code through: [https://swcarpentry.github.io/python-novice-gapminder/02-variables.html](https://swcarpentry.github.io/python-novice-gapminder/02-variables.html)

## Exercise

Do a back of the envelope calculation like:

```
# Cinema Sales Forecast

Forecasts the annual revenue from ticket sales at my cinema complex.

---

adult_ticket_price = 15.5
child_ticket_price = 10.5

average_movie_hours = 1.75
opening_hours_per_day = 8

cinemas = 5
average_adult_tickets_per_movie = 80
average_child_tickets_per_movie = 40

revenue_per_movie = (adult_ticket_price * average_adult_tickets_per_movie) + (child_ticket_price * average_child_tickets_per_movie)
print(f'Revenue per movie:', revenue_per_movie)

average_movies_per_day = opening_hours_per_day / average_movie_hours
print('Average movies per day:', average_movies_per_day)

average_revenue_per_day = average_movies_per_day * revenue_per_movie
print('Average daily revenue:', average_revenue_per_day)

# Multiply daily revenue by number of days in the year
annual_revenue_forecast = average_revenue_per_day * 365
print('Annual revenue forecast:', annual_revenue_forecast)
```
