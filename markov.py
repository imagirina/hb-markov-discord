"""Generate Markov text from text files. Check for Markovify."""

import sys
import random
from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    text_file = open(file_path)
    data = text_file.read().replace('\n', ' ')
    text_file.close()    

    return data


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

    >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

    >>> sorted(chains.keys())
    [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

    >>> chains[('hi', 'there')]
    ['mary', 'juanita']

    >>> chains[('there','juanita')]
    [None]
    """

    chains = {}
    key = ()
    string_list = text_string.split()

    for i in range(len(string_list)-2):
        key = (string_list[i], string_list[i+1])
        if key in chains:
            chains[key].append(string_list[i+2])
        else:
            chains[key] = [string_list[i+2]]

    return chains
    

def make_text(chains):
    """Return text from chains."""

    words = []
    
    # Get a random key as the first element for our text output
    current_key = random.choice(list(chains.keys()))
    
    # current_key = list(chains.keys())[0]
    # words.append(current_key[0])

    while current_key in chains.keys():        
        chosen_word = random.choice(chains[current_key])        
        words.append(current_key[0])            
        current_key = (current_key[1], chosen_word)
    
    words.append(current_key[0])
    words.append(current_key[1])
    
    return ' '.join(words)

if __name__ == "__main__":
    input_path = 'green-eggs.txt'
    # input_path = 'gettysburg.txt'

    # Open the file and turn it into one long string
    input_text = open_and_read_file(input_path)

    # Get a Markov chain
    chains = make_chains(input_text)

    # Produce random text
    random_text = make_text(chains)

    print(random_text)
