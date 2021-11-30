##################################
# Name: Kyle Hurd
# File: test_markov_chain.py
#
# Description:
# Test group to ensure set up of the MarkovChain are correct. This test focuses on the
# accurate collection of N-grams as well as just starting N-grams. 
# It also tests two test files to ensure the TextSpecs are correctly calculated for each file.
##################################


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
                stop_characters=STOP_CHARACTERS,
                )

        self.mc_starter = MarkovChain(filenames=['./tests/test_file_starting_ngrams.txt'],
                N=3,
                stop_words=STOP_WORDS,
                stop_characters=STOP_CHARACTERS,
                )

    def test_text_specs(self):
        specs = self.mc.specs
        assert specs.num_chars == 113
        assert specs.num_words == 22
        assert specs.num_unique_words == 16


    def test_starting_specs(self):
        specs = self.mc_starter.specs
        print(specs)
        assert specs.num_chars == 79
        assert specs.num_words == 16
        assert specs.num_unique_words == 13


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
        for expected, actual in zip(expected_output, n_gram_list):
            assert expected == actual

        
    def test_starting_n_grams(self):
        n_gram_list = self.mc_starter.starting_n_grams
        expected_output = [
            ('Here', 'is', 'sentence'),
            ('Is', 'Connor', 'here'),
            ('Here', 'he', 'is!'),
        ]
        assert len(n_gram_list) == len(expected_output)
        for expected, actual in zip(expected_output, n_gram_list):
            assert expected == actual