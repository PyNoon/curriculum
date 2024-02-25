---
title: PyNoon Week 8 - Tutorial
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

This week's tutorial will cover retrieving data from web APIs, loading
data from text files, and constructing DataFrames.

## Setup

1. Make a new notebook for this week
2. What's the first thing to do? RENAME IT!
3. Name it `week8.ipynb`

## Making web Requests

Let's import the `requests` library, which provides a simple set of
functions for making web requests.

> Normally we'd have to install `requests` using `pip`, but Colab
> already has it installed.

```code
import requests
```

* Let's use a *geocoding* web API:
  * Given an address string, it will return structured address fields
* We use `requests.get()` to make an HTTP `GET` request, which is the
  standard method for requests to retrieve data.
  * Other methods include `POST` and `PUT`, which are commonly used
    for submitting new data or data updates to an API.
* The URL to use and expected parameters for the API are documented
  at: [nominatim.org/release-docs/develop/api/Overview](https://nominatim.org/release-docs/develop/api/Overview/)

```code
r = requests.get(
    'https://nominatim.openstreetmap.org/search,
    params={
        'q': '221B Baker Street, London',
        'format': 'jsonv2',
        'addressdetails': 1,
    },
)
```

Let's look at the response:

```code
r
```

We can check the status of the response (`200` means the request was
successful):

```code
r.status_code
```

We can look at the data returned by the API:

```code
r.text
```

* The response text is formatted as JSON, a common data format used by
  APIs.
* `requests` can convert the JSON data to a structure of Python
  strings, numbers, lists and dictionaries:

```code
data = r.json()
```

```code
data
```

* We can check that the data is indeed made up of native Python data
  structures like lists, dictionaries, numbers, and strings:

```code
type(data)
```

* And we can access particular parts of the data using list and
  dictionary indexing:

```code
data[0]['address']
```

### Handling Errors

What happens if we change our request to specify an invalid format?

```code
r = requests.get(
    'https://nominatim.openstreetmap.org/search,
    params={
        'q': '221B Baker Street, London',
        'format': 'oops',
        'addressdetails': 1,
    },
)
```

The text is not the JSON we expect:

```code
r.text
```

And the status code of `400` indicates a failure - specifically a "Bad
Request":

```code
r.status_code
```

We can tell requests to raise an **exception** if the response has any
non-successful status code:

```code
r.raise_for_status()
```

* `r.raise_for_status()` **only** raises an exception when the status
  code indicates a failure - if the request succeeds, it effectively
  does nothing.
* If we want our program to continue even when an exception is raised,
  we can use a **try/except** statement to execute some code in the
  case of an exception.
* If any line of code in the `try` clause raises an exception, Python
  will stop executing the `try` block and execute the `except` block
  instead.
* The `as ex` saves the exception itself in a variable called `ex` so
  that we can get more details from it.
  * We can use any variable name we want, but `ex` is conventional.

```code
try:
    r.raise_for_status()
    print('Request succeeded!')
except requests.HTTPError as ex:
    print(f'Failed request: {ex}')
```

* We only want to catch exceptions we expect might happen:
  * Wrap as few lines of code as possible.
  * Only catch the types of exception we are expecting.

## Defining a request function

* Taking what we've learned, let's define a function to provide a
  simple interface for getting the details of an address.
* Note that:
  * We add a `sleep` for 1 second, as the API we are using has
    a rate limit of 1 request per second.
    * We might get an error or be blocked if we make requests faster
      than that.
  * In the case of an error, we return the special value `None`.

```code
from time import sleep

def get_address_details(address):
    """
    Given a loosely-formatted address string, return a dictionary of standard address details.

    If the request fails or no matching addresses are found, return None.
    """
    r = requests.get(
        'https://nominatim.openstreetmap.org/search,
        params={
            'q': address,
            'format': 'jsonv2',
            'addressdetails': 1,
        },
    )
    # Avoid hitting the API rate limit
    sleep(1)

    try:
        r.raise_for_status()
    except requests.HTTPError as ex:
        print(f'Failed request: {ex}')
        return None

    data = r.json()
    # Check for at least one matching address.
    if len(data) == 0:
        return None
    return data[0]['address']

get_address_details('221B Baker Street, London')
```

## Converting a file of addresses to a DataFrame of address details

* Now let's process a text file of addresses to produce a DataFrame of
  address details
* Download `addresses.txt` from:
  [pynoon.github.io/curriculum/week_8/addresses.txt](https://pynoon.github.io/curriculum/week_8/addresses.txt)
* Click the folder icon on the left side of the Colab interface, then
  use the upload button to upload `addresses.txt`

* Now, we can use `open()` to load
* `open()` should be used with a `with` statement so that the file is
  automatically closed when we're finished with it:

```code
with open('addresses.txt') as addresses_file:
    addresses = addresses_file.readlines()
```

`.readlines()` has provided us with a list of strings representing
each line in the file:

```code
addresses
```

We can use a list comprehension to apply our function to each address,
producing a list of corresponding address details:

```code
address_details = [get_address_details(address) for address in addresses]
```

Because of our exception handling in `get_address_details`, we should
remove any `None` values from the list of details:

```code
address_details = [
    address_detail for address_detail in address_details
    if address_detail is not None
]
address_details
```

* `pd.DataFrame` can be used to construct a DataFrame from a list of
  dictionaries like `address_details`.
* Where each dictionary represents the values for each column in a
  given row.

```code
import pandas as pd

address_df = pd.DataFrame(address_details)
address_df
```

## Reflection

* In this tutorial, we:
  * Took a list of addresses in a simple text file.
  * Retrieved more details for each address from an API.
  * And reformatted those details into a DataFrame, which we could
    export to a CSV file, or even an SQL database.
* This kind of data transformation is a common task that Python is
  very helpful for.
