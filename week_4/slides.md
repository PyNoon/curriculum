---
title: PyNoon Week 4
---

### Warm-Up Exercise (11:30 - 12:00)

<div style="text-align: left; font-size: 0.65em;">

#### Get setup with Colab

1. Open Colab Notebooks (link in the menu of
   [pynoon.github.io](https://pynoon.github.io))
2. Click the "New Notebook" button (it may take a few seconds)
3. Make sure you can run a simple `print('Hello world')` in a notebook
   cell (the first cell in a notebook will take a few seconds)

---

#### Plot some data

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
2. Make one or more interesting plots from the data
   * See [plotly.com/python/plotly-express/#gallery](https://plotly.com/python/plotly-express/#gallery) for inspiration

</div>

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


### Tutorial Objectives (12:15 - 1:00)

* Comparison operators
* Filtering rows in DataFrames
* Computing new columns in DataFrames

### Independent Work (1:00 - 1:30)

1. **Exercise Notebook:**
   * Answering questions from data
   * See the Exercise Notebook for Week 4 at
     [pynoon.github.io/schedule](https://pynoon.github.io/schedule)
2. **Work through [futurecoder.io](https://futurecoder.io) sections**:
   1. Lists (it's a longer one to work on over the break)
