##################################
# Name: Kyle Hurd
# File: MarkovChain.py
#
# Description:
# MarkovChain is a class used to suggest / generate new sentences based on
# a given text(s). The files are given in a list as multiple texts can be used.
##################################
import sys
from .TextSpecs import TextSpecs

import random
from colorama import Fore, Style
from functools import reduce


FULL_QUOTE = '"'
HALF_QUOTE = "'"
VERBOSITY  = '--verbosity' in sys.argv


class MarkovChain:


    def __init__(self, filenames, N, stop_characters=None, stop_words=None):
        self.initial_words = []
        self.n_grams = {}
        self.starting_n_grams = []
        self.filenames = filenames
        self.stop_characters = stop_characters
        self.stop_words = stop_words
        self.N = N
        self.specs = TextSpecs()
        self.build_chain()


    def generate_sentence(self):
        
        length_sentence = random.randint(4, 15)  
        seed = random.choice(self.starting_n_grams)
        
        
        output = [x for x in seed]
        is_quote = reduce(lambda base, word: (word[0] == FULL_QUOTE) or base, output, False)
    
        for _ in range(length_sentence):
            word, seed = self._generate_word(seed, is_quote)
            output.append(word)
            
        self._end_sentence(output, seed, is_quote)
        return ' '.join(output)


    def display_specs(self):
            print(f'{Style.BRIGHT}Files:{Style.RESET_ALL}')
            for filename in self.filenames:
                print(f'{Style.BRIGHT}{Fore.LIGHTRED_EX}-{Style.RESET_ALL} {filename}')
            self.specs.display_specs()


    def build_chain(self):
        self.starting_n_grams = []
        self.initial_words = []
        self.n_grams = {}
        self._init_words()
        self._create_ngram_dict()
        self._create_starting_ngrams_list()
  

    def _init_words(self):

        for filename in self.filenames:
            with open(filename, 'r') as f:
                chars = f.read()
                words = chars.split()
                unique_words = set(words)
                self.specs._populate(len(chars), len(words), len(unique_words))
                self.initial_words.extend(words)

        if VERBOSITY:
            self.display_specs()
            print(f'\n{Style.BRIGHT}Preview of the Text:{Style.RESET_ALL}')
            for i in range(50):
                print(f'{Fore.LIGHTGREEN_EX}{self.initial_words[i]}{Style.RESET_ALL}', end=' ')
            print()
            print()
    

    def _create_ngram_dict(self):
        n_grams = zip(*[self.initial_words[i:] for i in range(self.N + 1)])
        for n_gram in n_grams:
            key = n_gram[:self.N]
            next_word = n_gram[-1]
            self.n_grams[key] = self.n_grams.get(key, []) + [next_word]
        
        if VERBOSITY:

            print(f'\n{Style.BRIGHT}Preview of N-Grams:{Style.RESET_ALL}')
            for i, key in enumerate(self.n_grams.keys()):
                if i == 5:
                    break
                print(f'{Style.BRIGHT}- {Style.RESET_ALL}{Fore.LIGHTGREEN_EX}{key}{Style.RESET_ALL}')
            
            n_gram_vals = list(self.n_grams.values())
            print(f'\n{Style.BRIGHT}Preview of the N-Gram Entries:{Style.RESET_ALL}')
            for n_gram in n_gram_vals[:5]:
                print(f'{Style.BRIGHT}- {Style.RESET_ALL}', end='')
                for gram in n_gram:
                    print(f'{Fore.LIGHTGREEN_EX}{gram}{Style.RESET_ALL}', end=' ')
                print()
                
            n_gram_new = list(filter(lambda x: len(x) > 1, n_gram_vals))
            for entries in n_gram_new[:5]:
                print(f'{Style.BRIGHT}- {Style.RESET_ALL}', end='')
                for entry in entries:
                    print(f'{Fore.LIGHTGREEN_EX}{entry}{Style.RESET_ALL}', end=' ')
                print()


    def _create_starting_ngrams_list(self):

        is_valid        = lambda g: g[0] not in self.stop_words \
                            and (g[1][0].isupper() or g[1][0] in [FULL_QUOTE, HALF_QUOTE])
        in_stop_chars   = lambda g: g[0][-1] in self.stop_characters

        n_grams = zip(*[self.initial_words[i:] for i in range(self.N + 1)])
        for n_gram in n_grams:
            if in_stop_chars(n_gram) and is_valid(n_gram):
                self.starting_n_grams.append(n_gram[1:])

        if VERBOSITY:

            print(f'\n{Style.BRIGHT}Preview of the N-Gram Starters:{Style.RESET_ALL}')
            for n_gram in self.starting_n_grams[:10]:
                print(f'{Style.BRIGHT}- {Style.RESET_ALL}{Fore.LIGHTGREEN_EX}{n_gram}{Style.RESET_ALL}')
            print()


    def _generate_word(self, seed, is_quote=False):
    
        not_ending_quote = lambda word: word[-1] != FULL_QUOTE
        
        words = self.n_grams[seed]
        words = [word for word in words if not_ending_quote(word)] if not is_quote else words
        word = random.choice(words)
        seed = tuple(list(seed[1:]) + [word])
        
        return word, seed
    

    def _end_sentence(self, output, seed, is_quote=False):
        
        in_stop_characters = lambda word: word[-1] in self.stop_characters
        in_stop_words      = lambda word: word in self.stop_words
        
        while not (end := [word for word in self.n_grams[seed] if in_stop_characters(word) and not in_stop_words(word)]):
            word, seed = self._generate_word(seed, is_quote)
            is_quote |= word[0] == FULL_QUOTE  # if quote at beginning, make true.
            is_quote &= word[-1] != FULL_QUOTE # if quote at end, make false.
            output.append(word)
            
        word = random.choice(end)
        n_gram = tuple(list(seed[1:]) + [word])
        output.append(word)
