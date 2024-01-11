---
title: PyNoon Week 6
---

### Warm-Up Exercise

<div style="font-size: 0.9em;">

* Pair up and share your Personal Python Project idea
* What is the goal of your project - how will you know it has succeeded?
* What parts of your project do you think will be the most difficult to implement?
* Can you identify any skill you'll need to learn to complete your project?
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


### Lunch talk:<br>DRY: Don't Repeat Yourself

* Foundational principle for maintainable code
  * See [The Pragmatic Programmer](https://pragprog.com/titles/tpp20/the-pragmatic-programmer-20th-anniversary-edition/), Section 2.7
* When you need to make a change later, there should be **only one
  place to change**
* Strive to remove all forms of duplication
  * Getting your code to *work* is not the finish line!
  * **Refactor** your code to DRY it out

### What should you DRY out?

<div style="font-size: 0.8em;">

* Data
  * Each piece of data should have a **single source of truth**
  * Generate other representations from that source
* Documentation
  * Comments that state **how** the code works get out of date
  * Comments should explain **what** the code does and **why**
* Code
  * Use loops and custom functions to avoid code duplication
  * A great function is **re-usable** in many different contexts
  * We'll look more at these tools in the tutorial

</div>

### Don't *over-DRY* your code!

<div style="font-size: 0.85em;">

* E.g. you produce near-identical reports for two teams
* You DRY them so that they share all repeated code
* Later, one team asks for a change to their report, but now it is
  hard to change one without changing the other
* The two reports weren't actually **duplicating** one thing, they were
  just two things that **happened to be the same**

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
