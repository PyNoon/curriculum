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

We can see how big the DataFrame is using `.shape`:

```code
listings_df.shape
```

We can also see what columns we have available to work with:

```code
listings_df.columns
```

## Grouping Data in Plotly

When analysing data, we often want to compare different groups.

One simple way is to colour data points by a categorical column when
plotting. For example, colouring listings by their room type:

```code
px.scatter_geo(listings_df, lon='longitude', lat='latitude', color='room_type')
```

We can also specify a categorical column as a `facet_row` or
`facet_col` to generate a separate graph for data points having each
"facet" value.

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

It can be useful to compute our own categorical columns, such as to
compare one category against all others:

```code
listings_df['is_queenstown'] = listings_df['region_parent_name'] == 'Queenstown-Lakes District'
px.histogram(
    listings_df,
    x='price_nzd',
    facet_row='is_queenstown',
    histnorm='percent',
)
```

## Grouping Data in Pandas

We can also use Pandas' `groupby()` to split up a DataFrame according
to a categorical attribute:

```code
for accommodates, accommodates_group_df in listings_df.groupby('accommodates'):
    print('Accommodates:', accommodates)
    display(accommodates_group_df)
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
listing_groups_df = listings_df.groupby(['accommodates', 'room_type'])[['price_nzd', 'review_scores_rating']].mean().reset_index()
listing_groups_df
```

Such DataFrames produced with `groupby()` can be very useful for
producing plots of statistics, like bar charts:

```code
px.bar(
    listing_groups_df,
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

We can also use `.count()` to count the number of rows in each group,
but notice that the count for the rating column is less than the price
column:

```code
listings_df.groupby('accommodates')[['price_nzd', 'review_scores_rating']].count().reset_index()
```

This is because there are `missing` (aka `null`, aka `NA`) values in
the rating column that are ignored by `count()`.

We can use `isna()` to get a mask of rows where a value is missing:

```code
listings_df['review_scores_rating'].isna()
```

```code
listings_df[listings_df['review_scores_rating'].isna()]
```

We can then invert the mask with `~` and filter out rows with missing
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
