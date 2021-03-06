##################################
# Name: Kyle Hurd
# File: SentenceGenerator.py
#
# Description:
# SentenceGenerator is inherited from MarkovChain and uses the chain to
# build new sentences.
##################################

from .MarkovChain import MarkovChain

import random
from functools import reduce

FULL_QUOTE = '"'
HALF_QUOTE = '"'


class SentenceGenerator(MarkovChain):
    '''Generates sentences or paragraphs based on given source text.

    :param MarkovChain: Inherited class that generates the chain to generate sentences.
    '''

    def __init__(self, filenames, N, stop_characters=None, stop_words=None):
        '''Calls constructor for base class MarkovChain.

        :param filenames: the files to load into the object.
        :type filenames: list[str] | str
        :param N: Size of the n-gram
        :type N: int
        :param stop_characters: characters for which a sentence will end on, defaults to None
        :type stop_characters: str, optional
        :param stop_words: words which may contain a stop character, defaults to None
        :type stop_words: list[str], optional
        '''
        super().__init__(filenames, N, stop_characters=stop_characters, stop_words=stop_words)

    
    def generate_sentence(self, len: int=None):
        '''Generates a sentence based on the supplied source texts.

        :param len: length of the sentence, random length if not supplied, defaults to None
        :type len: int, optional
        :return: The generated sentence.
        :rtype: str
        '''
        
        length_sentence = random.randint(4, 15) if len is None else len
        seed = random.choice(self.starting_n_grams)
        
        
        output = [x for x in seed]
        is_quote = reduce(lambda base, word: (word[0] == FULL_QUOTE) or base, output, False)
    
        for _ in range(length_sentence):
            word, seed = self._generate_word(seed, is_quote)
            output.append(word)
            
        self._end_sentence(output, seed, is_quote)
        return ' '.join(output)

    
    def generate_paragraph(self, len: int=None):
        '''Generates a paragraph based on the supplied source texts.

        :param len: length of the sentence, random length if not supplied, defaults to None
        :type len: int, optional
        :return: The generated sentence.
        :rtype: str
        '''

        num_sentences = random.randint(5,20)
        output = []
        for _ in range(num_sentences):
            output.append(self.generate_sentence())
        return ' '.join(output)


    def _generate_word(self, seed, is_quote=False):
        '''Generates a word based on given seed. Updates seed after generating word.

        :param seed: The key for a specific bucket of words
        :type seed: tuple
        :param is_quote: determine if word to be generated is in the middle of a quote, defaults to False
        :type is_quote: bool, optional
        :return: word, seed
        :rtype: str, tuple
        '''
    
        not_ending_quote = lambda word: word[-1] != FULL_QUOTE
        
        words = self.n_grams[seed]
        words = [word for word in words if not_ending_quote(word)] if not is_quote else words

        # This is needed. If the text is primarily quotes it will make empty list.
        if not words:
            words = self.n_grams[seed]

        word = random.choice(words)
        seed = tuple(list(seed[1:]) + [word])
        
        return word, seed
    

    def _end_sentence(self, output, seed, is_quote=False):
        '''Works toward ending a sentence by finsihing quotes and stopping on a stop character.

        :param output: The list of words already generated
        :type output: list[str]
        :param seed: seed from previous generated word
        :type seed: tuple
        :param is_quote: determine if word to be generated is in the middle of a quote, defaults to False
        :type is_quote: bool, optional
        '''
        
        in_stop_characters = lambda word: word[-1] in self.stop_characters
        in_stop_words      = lambda word: word in self.stop_words
        
        while not ((end := [word for word in self.n_grams[seed] if in_stop_characters(word) and not in_stop_words(word)]) \
                        and not is_quote
                        ):
            word, seed = self._generate_word(seed, is_quote)
            is_quote |= word[0] == FULL_QUOTE  # if quote at beginning, make true.
            is_quote &= word[-1] != FULL_QUOTE # if quote at end, make false.
            output.append(word)
            
        word = random.choice(end)
        output.append(word)