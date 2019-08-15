#dictionary.py
#Dictionary Words as Tuples
#Jay Yunas
#17th December, 2018

import random
import collections
import config

#initialize a new dictionary for length
dictLen = collections.defaultdict(list)

#loop through each word in the dictionary, and add to list
for words in open("dictionary.txt"):
    words = words.rstrip('\n')
    dictLen[len(words)].append(words)

def wordsOfLength(length):
    """Return a list of words that have given length"""
    #returns dictionary with words of the given length
    return dictLen[length]

def randWord(hi, lo):
    """Return a random word with the length less than hi and greater than lo"""
    words = []

    #add words with specified length to the list
    for i in range(hi, lo):
        words += wordsOfLength(i)        

    #return a random word from the word bank
    return random.choice(words)
    
