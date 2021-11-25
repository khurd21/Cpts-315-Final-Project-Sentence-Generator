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

def main():

    N = 3
    args = sys.argv
    for arg in args:
        if 'N' in arg:
            try:
                N=int(arg[1])
            except Exception:
                print('Unable to determine N-value. Make sure in format: N<num>')
    
    hunger_games_mc = MarkovChain(filenames=[constants.HUNGER_GAMES_FILENAME],
                        N=N,
                        stop_characters=constants.STOP_CHARACTERS,
                        stop_words=constants.STOP_WORDS
                        )

    print('From Hunger Games\n')
    for _ in range(10):
        print('-', hunger_games_mc.generate_sentence())
    
    del hunger_games_mc


    hunger_games_kant_mc = MarkovChain(filenames=[constants.HUNGER_GAMES_FILENAME, constants.CRITIQUE_OF_PURE_REASON_FILENAME],
                                N=N,
                                stop_characters=constants.STOP_CHARACTERS,
                                stop_words=constants.STOP_WORDS
                                )

    print('From Hunger Games and Kant\n')
    for _ in range(10):
        print('-', hunger_games_kant_mc.generate_sentence())


    return


if __name__ == '__main__':
    main()
