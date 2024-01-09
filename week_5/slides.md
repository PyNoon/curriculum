---
title: PyNoon Week 5
---

### Warm-Up Exercise

<style>
.plot-exercise pre {
    width: 100%;
    margin: 5px 0;
}
</style>
<div class="plot-exercise">

1. Load libraries and data in a notebook:
   ```python
   import pandas as pd
   import plotly.express as px

   listings_df = pd.read_csv('https://pynoon.github.io/data/inside_airbnb_listings_nz_2023_09.csv')
   listings_df
   ```
2. Using what you learned in week 4's tutorial:
   * Make a histogram plot of listing prices *in Auckland*
   * Make a scatter plot of listing of price against review rating for
     listings that *only accomodate one person*
   * Challenge: Add an `island` column to `listings_df` that indicates
     which island the listing is located in (`'north'` or `'south'`)
     based on its latitude and longitude

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


### Tutorial Objectives

* Grouping and summarising data in Pandas and Plotly
* Handling missing data in Pandas


### Independent Work/Homework

1. **Exercise Notebook:**
   * Grouping and summarising exercises
   * See the Exercise Notebook for Week 4 at
     [pynoon.github.io/schedule](https://pynoon.github.io/schedule)
2. **Work through [futurecoder.io](https://futurecoder.io) sections**:
   1. A bit more about strings
   2. Nested Loops
3. Identify a project you can apply Python to
