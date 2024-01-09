# Week 6

* Futurecoder:
  * Functions

# Week 7

* Futurecoder:
  * Dictionaries

# Week 8

* Futurecoder:
  * Boolean Operators

# Week 9

* Futurecoder:
  * Tic Tac Toe Project

<!--
### DataFrame Indexing and Slicing

* The first "column" in the DataFrame is the *index*, which defaults to incrementing
  integers
* Like how each column has a name, the *index* is the "name" of each
  row
* We can assign a column to be the index of a DataFrame:

```code
listings_df = listings_df.set_index('id')
```

```code
listings_df
```

Why do we need to assign the result of `set_index()`?

* Calling `.set_index()` does not change the original DataFrame value
* Calling `.set_index()` returns a **new DataFrame value** with the
  index changed, which we then assign to the original variable.
* Most Pandas methods return a new value rather than changing the
  original value.


**We can perform indexing and slicing on DataFrames using `.iloc`:**

To get the first row:

```code
listings_df.iloc[0]
```

To get the second column in the first row:

```code
listings_df.iloc[0, 1]
```

To get the second column of the first five rows:

```code
listings_df.iloc[0:5, 1]
```

To get the second column of all rows:

```code
listings_df.iloc[:, 1]
```

**We can also index and slice rows and columns by their names:**

To get a single row by it's name in the index:

```code
listings_df.loc['l9995141']
```

To get several rows by their names:

```code
listings_df.loc[['l9995141', 'l12026015', 'l44688136']]
```

> While you can use `:` slicing to specify a start and end names for a
> range, it is more common to specify a list of names.

To get the `name` column of all rows:

```code
listings_df.loc[:, 'name']
```
-->


<!--
## 1d. Selection of Individual Values

Use sorting and indexing on `listing_df` to find:

1. The value in the third column of the fifth row.
2. The `name` of the listing with an `id` of `'l6113'`
3. The `review_scores_rating` of the most reviewed listing.
4. The `latitude` and `longitude` of the least expensive listing.
-->
