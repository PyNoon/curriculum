---
title: PyNoon Plus Lesson 1 - Exercise
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

# PyNoon Plus: Lesson 1 - Exercise


## 1. AI Exercises

### 1a. Classification Confidence

* AI will not always generate good results - have a look at the label
  assigned to the `When to plant tomatoes` title in the tutorial.
* The classifier we used in the tutorial returns more than just the
  best matching label, it also returns a **score** for each label to
  give us an indication of the classifier's confidence in its
  classification.
* Modify your code from the tutorial to include the score for each
  possible label in columns of `title_df`.
  * **Tip:** You might find it easier to construct `title_details`
    using a `for` loop instead of a list comprehension.
  * **Tip:** Consider using Python's `zip()` function to combine the
    lists of labels and scores returned by the classifier.

### 1b. Try out another AI model

* Try out one or more other models from
  [huggingface.co](https://huggingface.co/models)
* The model page will usually include example code showing you how to
  use
* Some models might require the computational power of GPU (Graphics
  Processing Unit) to run efficiently - fortunately, Google Colab can
  run your code on a computer that has access to a GPU.
  * You'll need to select a runtime with a GPU from the option menu
    next to your RAM and CPU usage in the top-right corner of Colab.
* You might like to try:
  * Generating text with an Instruct-trained (i.e. ChatGPT-like) Large
    Language Model (LLM), such as:
    * [dolly-v2](https://huggingface.co/databricks/dolly-v2-3b)
      * Run `!pip install accelerate` and restart the Colab session
        from the `Runtme` menu first.
    * [llama2](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf)
      * Requires you to accept the license and authenticate with
        HuggingFace from your code
  * Detecting objects in an image with
    [https://huggingface.co/facebook/detr-resnet-50](https://huggingface.co/facebook/detr-resnet-50)
  * Answer questions from a DataFrame with
    [https://huggingface.co/microsoft/tapex-large-finetuned-wtq](https://huggingface.co/microsoft/tapex-large-finetuned-wtq)

### 1c. LangChain

Have a look at the
[LangChain](https://python.langchain.com/docs/get_started/quickstart)
package for more examples of using Python to build applications
powered by generative AI.


## 2. Futurecoder

Complete the final lesson on [futurecoder.io](https://futurecoder.io)
(this is a mini-project, so it might take a bit longer):

1. Boolean operators

> You can check which lesson you are up to on Futurecoder from the
> `Table of Contents` link at the top of the Futurecoder webpage.


## 3. Identify a Personal Python Project to work on

* Do you have a dataset you want to analyse?
  * A spreadsheet from work?
  * Home income/expense data?
  * Something from:
    * https://www.kaggle.com/datasets
    * https://catalogue.data.govt.nz/dataset
* Is there a text or image file processing task you want to automate?
  * Automating a backup of specific files
  * Renaming files and organising them into folders
  * Generating a report from spreadsheets, word documents, or images
* For more inspiration, have a look at:
  * https://automatetheboringstuff.com/#toc

Once you have an idea, start designing your solution, applying what
you learned in the Lunch Talk. Use a simple diagram to:

* Identify inputs and outputs
  * Does your software need to process any data? Where will it come
    from and what format will it be in?
  * What output will your software produce? What format will it be in?
* Plan high-level steps from inputs to outputs
  * Work backwards from the outputs, or forwards from the inputs
  * A step might be an action to take or an *intermediate data
    representation* to produce
* Fill in details
  * Think about what libraries or techniques you will use for each part
  * If necessary, break up major steps into sub-steps
