---
title: PyNoon Week 9 - Exercise
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

# PyNoon Week 9 - Exercise


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

1. Tic Tac Toe Project

> You can check which lesson you are up to on Futurecoder from the
> `Table of Contents` link at the top of the Futurecoder webpage.
