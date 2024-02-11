---
title: PyNoon Week 6
---

### Warm-Up Exercise

<div style="font-size: 0.9em;">

* Pair up and share your Personal Python Project idea
* What is the goal of your project - how will you know it has succeeded?
* What parts of your project do you think will be the most difficult to implement?
* Can you identify any skills you'll need to learn to complete your project?
* Is there any data you need to collect for your project?

</div>

### Thanks

* To the host for the great venue!
* Our supporting employers
* New Zealand Python User Group (NZPUG) for support

### Administrivia

* Fire escapes
* Toilets
* Cleaning up after ourselves
* WiFi


### Lunch Talk:<br>DRY: Don't Repeat Yourself

* Foundational principle for maintainable code
  * See [The Pragmatic Programmer](https://pragprog.com/titles/tpp20/the-pragmatic-programmer-20th-anniversary-edition/), Section 2.7
* E.g. Don't copy-paste code around your project
* When you need to make a change later, there should be **only one
  place to change**
* Getting your code to *work* is not the finish line!
  * **Refactor** working code to make it more **readable** and
    **maintainable**

### How do you DRY out code?

<div style="font-size: 0.95em;">

* Repeating code in **one place** for different "things"?
  * **Loop** over those things
* Repeating code in lots of **different places**?
  * Write a **custom function**
  * Great functions are **re-usable** in many contexts
* We'll look at these tools in the tutorial

</div>

### Don't *over-DRY* your code!

<div style="font-size: 0.85em;">

* E.g. you produce near-identical reports for two teams
* You DRY them so that they share all repeated code
* Later, one team asks for a change to their report, but now it
  is hard to change one without changing the other
* The two reports weren't actually **duplicating** one thing, they were
  just two things that **happened to be the same**

</div>

### What else should you DRY out?

<div style="font-size: 0.75em;">

* Data
  * Each piece of data should have a **single source of truth**
  * Generate other **representations** from that source
* Documentation
  * Comments that state exactly what code does (i.e. repeat what they
    code itself is saying) get out of date
  * Comments should explain what code **achieves** and **why**

</div>

### Helpful Comments

<div style="font-size: 0.8em;">

```python
price_bound = listings_df.groupby('region_name')['price_nzd'].min().max()
```

Which is a more helpful comment?

```python
# Group listings by region, take the minimum price of each group,
# then take the maximum across all groups
```

```python
# Get the highest listing price that is the cheapest in its region
```

```python
# Get the highest listing price that is the cheapest in its region
# to find the minimum nightly cost for a round-the-country trip.
```

</div>

### Tutorial Objectives

* Defining and using your own functions
* Reducing duplication in your code


### Independent Work/Homework

1. **Exercise Notebook:**
   * Function and de-duplication exercises
   * See the Exercise Notebook for Week 6 at
     [pynoon.github.io/schedule](https://pynoon.github.io/schedule)
2. **Work through [futurecoder.io](https://futurecoder.io) sections**:
   1. Functions
3. Work on your own Python project
