<center>

# Sentence Generator

## A sentence generator based on a generic source text,
## utilizing Markov Chains and N-Grams

**Prepared by:** `Kyle Hurd`

</center>

---

**Course:** `Cpts 315 - Introduction to Data Mining`

---

## Table of Contents
- [Markov Chain](#markovchain)
    - [A Sentence Generator](#a-sentence-generator-based-on-a-generic-source-text)
    - [Table of Contents](#table-of-contents)
    - [Document Revision History](#document-revision-history)
- [1. Introduction](#1-introduction)
- [2. How to Run](#2-how-to-run)
    - [Optional Keyword Arguments](#optional-keyword-args)

<a name="revision-history"> </a>

## Document Revision History
| Name | Date | Changes | Version |
| ------ | ------ | --------- | --------- |
|Revision 1 | 2021-11-25 | Initial working product | 1.0 |

<br><br>

# 1. Introduction

This program was designed as a final project for `Computer Science 315 - 
Introduction to Data Mining`. The project reads in a long source text and
makes new sentence suggestions based on the text. This word generator is
implemented using Markov Chain and N-Grams. A description of the implementation
with outputs from the functions can be seen within the
[Jupyter-Notebook](MarkovChain.ipynb) on the root page of this project.

# 2. How to Run

The dependencies for this program are found in the [requirements.txt](requirements.txt)
file in the root page of this project. You can manually install these or use the
[setup_venv.sh](setup_venv.sh) script to create a virtual enviromnent with all dependencies
installed.

To run the program you can either run [main.py](main.py) directly or use the
[run_script.sh](run_script.sh) script to run it. The `run_script.sh` will output your
results to a file labeled `output.s`.

## Optional Keyword Args

There are two optional keyword arguments you can pass into the script:  
 - `--verbosity`
 - `N<num>`

 `N<num>` tells the program the length of n-grams to use. For example:  
 ```
 python main.py N3
 ```
 generates sentences based on n-grams of length 3.

 <br>

 `--verbosity` is a mode to display more information regarding the MarkovChain's
 current state and statistics. For example:  

 ```
 python main.py --verbosity
 python main.py --verbosity N3
 ``` 
