##################################
# Name: Kyle Hurd
# File: main.py
#
# Description: 
# The main file that showcases how to use use the MarkovChain.
# The class MarkovChain is written to set up during the initialization process.
# the filenames takes a list of files, N is the gram size, and of course we can
# supply a string of stop characters and stop words. After initialization, we
# can use the method '.generate_sentence()' to create single sentences or paragraphs.
##################################

import sys

import constants
from MarkovChain import MarkovChain


NUM_SENTENCES = 20
N = 3

def format_sentences(title, file):
    '''A wrapper to generate a MarkovChain instance and generate NUM_SENTENCE amount of sentences.

    Parameters
    ----------
    title : str
        The title for the set of generated sentences.
    file : list[str]
        a list of strings for which the source text is provided.
    '''
    mc = MarkovChain(filenames=file if isinstance(file, list) else [file],
                N=N,
                stop_characters=constants.STOP_CHARACTERS,
                stop_words=constants.STOP_WORDS
                )
    print(title)
    for _ in range(NUM_SENTENCES):
        print('-', mc.generate_sentence())
    print('\n********************************************\n')


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
            'From Twilight\n',
            'From 50 Shades of Gray\n',
            'From Lord of the Rings\n',
            ]

    files_for_books = [
            constants.HUNGER_GAMES_FILENAME,
            constants.TWILIGHT,
            constants.FIFTY_SHADES_OF_GRAY,
            constants.LORD_OF_THE_RINGS,
            ]
   
    for title, file in zip(book_titles, files_for_books):
        format_sentences(title, file)

    format_sentences('From Hunger Games, Twilight, 50 Shades and Lord of the Rings\n', files_for_books)
    return


if __name__ == '__main__':
    main()
