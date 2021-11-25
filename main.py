##################################
# Name: Kyle Hurd
# File: main.py
#
# Description: 
# The main file that showcases how to use use the MarkovChain.
##################################

import sys

import constants
from MarkovChain import MarkovChain


NUM_SENTENCES = 20
N = 3

def format_results(title, file):
    mc = MarkovChain(filenames=file if isinstance(file, list) else [file],
                N=N,
                stop_characters=constants.STOP_CHARACTERS,
                stop_words=constants.STOP_WORDS
                )
    print(title)
    for _ in range(NUM_SENTENCES):
        print('-', mc.generate_sentence())
    print()


def main():

    global N
    args = sys.argv
    for arg in args:
        if 'N' in arg:
            try:
                N=int(arg[1])
            except Exception:
                print('Unable to determine N-value. Make sure in format: N<num>')

    book_titles = [
            'From Hunger Games\n',
            'From Kant\n',
            'From Twilight\n',
            ]

    files_for_books = [
            constants.HUNGER_GAMES_FILENAME,
            constants.CRITIQUE_OF_PURE_REASON_FILENAME,
            constants.TWILIGHT,
            ]
   
    for title, file in zip(book_titles, files_for_books):
        format_results(title, file)

    format_results('From Hunger Games, Kant, and Twilight\n', files_for_books)
    return


if __name__ == '__main__':
    main()
