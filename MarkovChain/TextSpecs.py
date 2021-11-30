##################################
# Name: Kyle Hurd
# File: TextSpecs.py
#
# Description:
# TextSpecs is a simple accumulator designed for the MarkovChain class
# to display information regarding the read text that includes how many
# characters, words, and unique words exist in the file.
##################################


from dataclasses import dataclass
from colorama import Fore, Style


@dataclass
class TextSpecs:
    num_chars: int = 0
    num_words: int = 0
    num_unique_words: int = 0

    
    def _populate(self, num_chars: int, num_words: int, num_unique_words: int):
        self.num_chars += num_chars
        self.num_words += num_words
        self.num_unique_words += num_unique_words


    def clear(self):
        self.num_chars = 0
        self.num_words = 0
        self.num_unique_words = 0


    def display_specs(self):
        print(f'{Style.BRIGHT}{Fore.LIGHTGREEN_EX}{"#" * 18}' \
              f'{"#" * (len(str(self.num_unique_words)) + 1)}{Style.RESET_ALL}')
        
        print(f'{Style.BRIGHT}num chars: {Style.RESET_ALL}{self.num_chars}{Style.RESET_ALL} ')
        print(f'{Style.BRIGHT}num words: {Style.RESET_ALL}{self.num_words}{Style.RESET_ALL} ')
        print(f'{Style.BRIGHT}num unique words: {Style.RESET_ALL}{self.num_unique_words}{Style.RESET_ALL} ')
        
        print(f'{Style.BRIGHT}{Fore.LIGHTGREEN_EX}{"#" * 18}' \
              f'{"#" * (len(str(self.num_unique_words)) + 1)}{Style.RESET_ALL}')

    
    def __repr__(self):
        return f'<TextSpecs num_chars: {self.num_chars} num_words: {self.num_words} num_unique_words: {self.num_unique_words}'
