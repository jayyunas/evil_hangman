#config.py
#for Evil Hangman Program
#Jay Yunas
#17 Dec 2018

"""
Default: dictionary = 'lite-dictionary'
"""
dictionary = 'dictionary'

"""
True to play Evil Hangman
False to play Regular Hangman
Evil Hangman will switch the chosen word, Regular Hangman will not.
Default: evil = True
"""
evil = False

"""
Minimum word length
Default: min_word_length = 2
"""
minWordLength = 2


"""
Maximum word length
Default: max_word_length = 8
"""
maxWordLength = 8

"""
Number of incorrect guesses to allow
Default: num_guesses = 6
"""
numGuesses = 6

"""
Option to "cheat" by revealing the chosen word.
True to reveal the chosen word
False to hide the chosen word
Default: reveal_word = False
"""
revealWord = True


"""
Option to "cheat" by revealing the size of the word bank. (Evil Hangman only)
True to reveal word bank size
False to hide word bank size
Default: reveal_word_bank_size = False
"""
revealWordBankSize = False
