---
title: PyNoon Plus Lesson 2
---

### Warm-Up Exercise

* Pair up and share your Personal Python Project idea
* What is the goal of your project - how will you know it has succeeded?
* What parts of your project do you think will be the most difficult to implement?
* Can you identify any skills you’ll need to learn to complete your project?
* Is there any data you need to collect for your project?

### Thanks

* To the host for the great venue!
* To our sponsors

### Administrivia

* Fire escapes
* Toilets
* Cleaning up after ourselves
* WiFi


### Lunch Talk: Web APIs

* On the World Wide Web, there are:
  * Applications used by *humans* (i.e. websites)
  * Applications used by *other software*
    * **Application Programming Interfaces (APIs)**
* Python can make *requests* to **web APIs** that:
  * Get data (e.g. get news updates)
  * Post data (e.g. publish a social media update)

### Requests and Responses

<img src="images/request-response.png" style="margin-bottom: 0; width: 80%;">

* **HTTP** is the *protocol* for web communication
* **HTTPS** is the *Secure* version of HTTP

### HTTP Requests

* Every request has a **method**:
  <div style="font-size: 0.8em;">
  * `GET` requests fetch data
  * `POST` requests submit data
  </div>
* Every request is made to a **Uniform Resource Locator (URL)**:

<img src="images/url.png" style="margin-bottom: 0;">


### HTTP Responses

<div style="font-size: 0.9em;">

* Responses for web pages return text, images, etc.
* Responses from APIs return *data* your code can use
  * Typically formatted as **JSON** or **XML**

* Every HTTP response also has a **status code**:
  <div style="font-size: 0.8em;">
  * `200 OK` - The request succeeded
  * `404 Not Found` - The path couldn't be found
  * `400 Bad Request` - Request parameters were invalid
  * `500 Internal Server Error` - The server couldn't respond properly
  </div>

</div>

### Tips for working with web APIs

<div style="font-size: 0.9em;">

* An API should provide **documentation** of:
  * Supported paths and methods for requests
  * Supported parameters for each request
  * The format of data in responses
* Meanings of methods and status codes are **conventions** - not all
  APIs use them consistently
* Always check API **terms & conditions**
* Some APIs require you to sign up for an **API key** or otherwise
  identify your account to make requests
* You can even use Python to make your own web API to service requests
  from other applications!

</div>

### Tutorial Objectives

* Retrieving data from a web API

### Independent Work/Homework

1. **Exercise Notebook:**
   * API Exercises
   * See the Exercise Notebook for PyNoon Plus Lesson 2 at
     [pynoon.github.io/lessons](https://pynoon.github.io/lessons)
2. **Work through the final [futurecoder.io](https://futurecoder.io) section**:
   1. Tic Tac Toe Project
3. Work on your own Python project
