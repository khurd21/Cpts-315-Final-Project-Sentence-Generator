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
- [Sentence Generator](#sentence-generator)
    - [A Sentence Generator](#a-sentence-generator-based-on-a-generic-source-text)
    - [Table of Contents](#table-of-contents)
    - [Document Revision History](#document-revision-history)
- [1. Introduction](#1-introduction)
- [2. Example Use](#2-example-use)
- [3. How to Run](#3-how-to-run)
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

# 2. Example Use

```
HUNGER_GAMES_FILENAME = './data/hunger_games.txt'
CRITIQUE_OF_PURE_REASON_FILENAME = './data/the_critique_of_pure_reason.txt'
TWILIGHT = './data/twilight_formatted.txt'
FIFTY_SHADES_OF_GRAY = './data/50_shades_of_gray.txt'


STOP_CHARACTERS = '.?!'
STOP_WORDS = ['Dr.', 'Jr.', 'Sr.', 'Mr.', 'Mrs.', 'Ms.', 'Miss.', 'Prof.']
N=3

title = 'From Hunger Games, Kant, Twilight, and 50 Shades'
file = [
    'From Hunger Games\n',
    'From Kant\n',
    'From Twilight\n',
    'From 50 Shades of Gray',
]

mc = MarkovChain(filenames=file if isinstance(file, list) else [file],
                N=N,
                stop_characters=STOP_CHARACTERS,
                stop_words=STOP_WORDS
                )
    print(title)
    for _ in range(NUM_SENTENCES):
        print('-', mc.generate_sentence())
    print()
```

Output:

```
From Hunger Games, Kant, Twilight, and 50 Shades

- "You?" I looked at the clock — it was too nice out to stay indoors." I took another step.
- I have to mind my actions every moment that we're together so that I could see.
- If only I could free the apples themselves . . . I think it’s orange juice. I’ve only even tasted an orange once, at New Year’s when my father bought one as a special treat.
- I was so angry, it took me a few feet between us, and I sighed.
- Not everyone is treated with such respect. But whenever my father sang, all the birds stopped singing at once.
- The proper problem of pure reason, we must notice first that it cannot employ its categories for the consideration of them.
- I know, I know that someone stubbed cigarettes out on Christian.
- Plutarch taps a spot on my shoulder and up to the curb just a few more hours, although I doubt Cato assumes anything at this point.
- In fact, the force field stopped his heart. Mags running into the fog with her. Anyway, it’s gone. I have moved out a bit farther off.
- Perhaps it will give me so much to you, or your lawyer...
- He looked at me and raises his eyebrows. “No coffee?” “I’m not keen on coffee.” He smiles. “Okay, bag out tea.
- In some districts the victors ride through the city while the residents cheer.
- Then I found Madge in her room, sitting at her dressing table, brushing out her wavy blond hair before a mirror.
- He stopped, still several feet away, and sank gracefully to the door and shuffles around removing his pants.
- Her stocks of remedies are running so low, though, that soon all she’ll have to treat of the conception change.
- Every time I look at the different propositions which are properly just so many different ways.
- A young one. Fourteen at the most. Innocent. Harmless. Yes, it is shocking that Cinna has pulled this off when you remember I’ve just won the Games.
- "People in this town," he muttered. "Dr. Cullen is a brilliant surgeon who could probably work in any hospital in the summer heat.
- I dug through my bag until I found a much more valuable form of payment.” Secrets, I think.
- In truth, if I cognize in all its precision to objects of the external sense.
```

# 3. How to Run

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
