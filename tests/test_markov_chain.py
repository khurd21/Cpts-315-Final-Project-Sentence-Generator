
from MarkovChain.MarkovChain import MarkovChain
import unittest

VERBOSITY = 2
STOP_CHARACTERS = '.?!'
STOP_WORDS = ['Dr.', 'Jr.', 'Sr.', 'Mr.', 'Mrs.', 'Ms.', 'Miss.', 'Prof.']


class TestMarkovChain(unittest.TestCase):

    
    def setUp(self):
        self.mc = MarkovChain(filenames=['./tests/test_file.txt'],
                N=3,
                stop_words=STOP_WORDS,
                stop_characters=STOP_CHARACTERS
                )

    def test_text_specs(self):
        specs = self.mc.specs
        assert specs.num_chars == 113
        assert specs.num_words == 22
        assert specs.num_unique_words == 16


    def test_n_gram(self):
        n_gram_list = self.mc.n_grams.keys()
        expected_output = [
                ('This', 'is', 'text'),
                ('is', 'text', 'to'),
                ('text', 'to', 'try'),
                ('to', 'try', 'and'),
                ('try', 'and', 'figure'),
                ('and', 'figure', 'out'),
                ('figure', 'out', 'how'),
                ('out', 'how', 'many'),
                ('how', 'many', 'characters'),
                ('many', 'characters', 'there'),
                ('characters', 'there', 'are'),
                ('there', 'are', 'and'),
                ('are', 'and', 'how'),
                ('and', 'how', 'many'),
                ('how', 'many', 'words'),
                ('many', 'words', 'and'),
                ('words', 'and', 'how'),
                ('how', 'many', 'unique'),
                ]
       
        assert len(n_gram_list) == len(expected_output)
        for itr, key in enumerate(n_gram_list):
            assert key == expected_output[itr]
