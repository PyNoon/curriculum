---
title: PyNoon Week 8
---

### Warm-Up Exercise

* Continue working on your Personal Python Project
* Pair up and review each other's project work
  * Without explaining your code, can they understand what each line
    achieves?
  * What changes would make it easier to read?
  * Do you have any suggestions to DRY out your partner's code?

### Thanks

* To the host for the great venue!
* Our supporting employers
* New Zealand Python User Group (NZPUG) for support

### Administrivia

* Fire escapes
* Toilets
* Cleaning up after ourselves
* WiFi


### Lunch Talk: Web Requests and APIs

* Whenever you visit a web page, your web browser makes a request to a
  **URL**:

<img src="images/url.png">

* Typically, these requests return web page content: Text, images,
  layout, and styling

### Web APIs

<div style="font-size: 0.9em;">

* Some web applications, are designed to provide data to and receive
  data from other applications
  * We call these **Application Programming Interfaces (APIs)**
* Python can make requests to web APIs
* Responses typically contain data formatted as **JSON** or **XML**
* Always check API **terms & conditions**
* Some APIs require you to sign up for an **API key** or otherwise
  identify your account to make requests

</div>

### HTTP Requests & Responses

* Every HTTP request has a **method**:
  <div style="font-size: 0.8em;">
  * `GET` requests fetch data
  * `POST` requests submit data
  </div>
* Every HTTP response has a **status code**:
  <div style="font-size: 0.8em;">
  * `200 OK` - The request succeeded
  * `404 Not Found` - The path couldn't be found
  * `400 Bad Request` - Request parameters were invalid
  * `500 Internal Server Error` - The server couldn't respond properly
  </div>
* The meanings of Methods and status codes are **conventions** - not
  all APIs use them consistently

### Tutorial Objectives

* Retrieving data from web APIs
* Loading data from text files
* Constructing DataFrames

### Independent Work/Homework

1. **Exercise Notebook:**
   * API Exercises
   * See the Exercise Notebook for Week 8 at
     [pynoon.github.io/schedule](https://pynoon.github.io/schedule)
2. **Work through [futurecoder.io](https://futurecoder.io) sections**:
   1. Boolean operators
3. Work on your own Python project
