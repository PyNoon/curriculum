---
title: PyNoon Data Lesson 3 - Tutorial
jupyter:
  nbformat: 4
  nbformat_minor: 4
  kernelspec:
     display_name: Python (Pyodide)
     language: python
     name: python3
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

This tutorial will cover grouping and summarising data with
Pandas and Plotly, and handling missing data with Pandas.

It is based on:

* [swcarpentry.github.io/python-novice-gapminder/08-data-frames.html](https://swcarpentry.github.io/python-novice-gapminder/08-data-frames.html)
* [swcarpentry.github.io/python-novice-gapminder/09-plotting.html](https://swcarpentry.github.io/python-novice-gapminder/09-plotting.html)

## Setup

1. Make a new notebook for this lesson
2. What's the first thing to do? RENAME IT!
3. Name it `pynoon_data_3.ipynb`

## Load Data into Pandas

As we did last lesson, let's load the Pandas and Plotly libraries, and
load our AirBnB listings data into Pandas:

```code
import pandas as pd
import plotly.express as px
```

```code
listings_df = pd.read_csv('https://pynoon.github.io/data/inside_airbnb_listings_nz_2023_09.csv')
listings_df
```

## Grouping Data in Plotly

When analysing data, we often want to compare different groups or
subsets.

Plotly makes a lot of group comparisons easy if we have a *tidy*
DataFrame - with a **row for each data point** and a **column for each
attribute** - including *categorical* attributes we want to group by.

For example, we can specify a categorical column to colour data points
by:

```code
px.scatter_geo(listings_df, lon='longitude', lat='latitude', color='room_type')
```

> Note: You can select/deselect colours in the legend.

We can also specify a numerical column to determine the colour:

```code
px.scatter_geo(listings_df, lon='longitude', lat='latitude', color='price_nzd')
```

We can go further and create a separate subplot for the data points
belonging to each group by specifying a categorical column as a
`facet_row` or `facet_col`.

In the plot below, note that we:

* Sort the data by the `accommodates` column, so that the facet plots
  are sorted by value.
* Increase the height of the output to better view the large number of
  plots.
* Set `histnorm='percent'` so that groups with few data points still
  have a "full size" plot.

```code
px.histogram(
    listings_df.sort_values(by='accommodates'),
    x='price_nzd',
    facet_row='accommodates',
    height=2000,
    histnorm='percent',
)
```

Sometimes we'd like to treat a numeric column like a categorical
column in our visualisation.

We can do this by using `pd.qcut()` to create a categorical column by
dividing a numeric column into *bins*.

* Using `pd.qcut()` makes each bin **have the same number of data
  points**, while `pd.cut()` makes each bin **cover an equal-length
  interval of the numeric column**.
* We need to convert each "bin" value to a string in order to display
  it with Plotly.

For example, we can plot the distribution of review counts for
different tiers of pricing:

```code
listings_df['price_bin'] = pd.qcut(listings_df['price_nzd'], q=10).astype(str)

px.box(
    # Ensure lower price bins are shown first.
    listings_df.sort_values(by='price_nzd'),
    x='price_bin',
    y='number_of_reviews',
)
```

## Grouping Data in Pandas

We can also use Pandas' `groupby()` to split up a DataFrame according
to a categorical attribute.

If you're familiar with SQL, you'll see similarities to the `GROUP BY`
clause.

* We can loop over the "groups", getting the attribute value and a
  DataFrame of rows having that attribute value
* `.shape` returns the number of rows and number of columns as a pair
  (tuple)

```code
for room_type, room_type_group_df in listings_df.groupby('room_type'):
    print('Room type', room_type)
    print(room_type_group_df.shape[0])
```

`groupby()` can also be used to produce a DataFrame of aggregate
statistics for each group. In the following, see how we:

* Specify the columns from which to create a group for each
  combinations of values (`['accommodates', 'room_type']`)
* Use indexing to select a list of columns to calculate the statistic
  for (`['price_nzd', 'review_scores_rating']`)
* Choose a statistic to calculate: `mean()`
  * You can also compute `sum()`, `std()`, and more.

```code
listings_df.groupby(['accommodates', 'room_type'])[['price_nzd', 'review_scores_rating']].mean()
```

Note that `groupby()` turns the group columns into an *index*. We can
turn it back into a regular column with `reset_index()`:

```code
stats_df = listings_df.groupby(['accommodates', 'room_type'])[['price_nzd', 'review_scores_rating']].mean().reset_index()
stats_df
```

`.groupby()` is a very powerful tool for reshaping data into the right
*tidy* format that will support the plot you want.

Such DataFrames produced with `groupby()` can be very useful for
producing plots of statistics, like bar charts:

```code
px.bar(
    stats_df.sort_values(by='accommodates'),
    x='accommodates',
    y='price_nzd',
    color='room_type',
    barmode='group',
    title='Mean Price',
)
```

We can also export our new DataFrame to a CSV file:

```code
listing_groups_df.to_csv('listing_groups.csv')
```

## Handling Missing Data in Pandas

We can use `isna()` to get a mask of rows where a value is missing:

```code
listings_df[listings_df['review_scores_rating'].isna()]
```

We can invert the mask with `~` and filter out rows with missing
values:

```code
listings_df[~listings_df['review_scores_rating'].isna()]
```

Alternatively, we can use `fillna()` to replace missing values with a
fixed value. For example, we make want to consider un-reviewed
listings with a mid-point rating:

```code
listings_df['review_scores_rating_filled'] = listings_df['review_scores_rating'].fillna(2.5)
listings_df
```

Finally, `dropna()` on a DataFrame can be used to simply remove any
rows where any column contains a missing value:

```code
listings_df.dropna()
```
