---
title: PyNoon Plus Lesson 2 - Exercise
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

# PyNoon Plus: Lesson 2 - Exercise

## 1. API Exercises

### 1a. Get address latitude and longitude

The geocoding API used in the tutorial also returns the latitude and
longitude for an address:
[nominatim.org/release-docs/develop/api/Search/#json-with-address-details](https://nominatim.org/release-docs/develop/api/Search/#json-with-address-details)

Extend the code from the tutorial to add the latitude and longitude to
the dictionary returned by `get_address_details`.

### 1b. Reverse geo-coding

There is a reverse geo-coding API that can be used to look up the
address for a given latitude and longitude:
[nominatim.org/release-docs/develop/api/Reverse](https://nominatim.org/release-docs/develop/api/Reverse/)

The AirBnB listings DataFrame you have used in previous lessons
provides the latitude and longitude for each listing.

Your task is to use the reverse geo-coding API to fetch address data
for a small number of listings.

* To avoid hitting rate limits, work with a small sample of listings,
  e.g.: `listings_df = listings_df.sample(n=5)`
* Hint: Use the `.apply()` DataFrame method from
  [PyNoon Data Lesson 4](https://colab.research.google.com/github/pynoon/curriculum/blob/main/lesson_data_4/lesson_data_4_tutorial.ipynb).

### 1c. Try another API

Have a go using a completely different API, such as:

* A weather API: https://open-meteo.com/
* The Google Books API: https://developers.google.com/books
* Auckland Transport's API: https://dev-portal.at.govt.nz/

> Note: Some APIs may require you to register for an API key that must
> be provided with each request.


## 2. Futurecoder

Complete the final lesson on [futurecoder.io](https://futurecoder.io):

1. Tic Tac Toe project

> You can check which lesson you are up to on Futurecoder from the
> `Table of Contents` link at the top of the Futurecoder webpage.
