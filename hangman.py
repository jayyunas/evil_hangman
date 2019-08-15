#hangman.py
#Classes for Evil Hangman
#Jay Yunas
#17th December, 2018

from collections import defaultdict
import config
import words
import random


class Hangman:
    """
    Base Hangman class which can be used to play vanilla Hangman. Once the word
    is chosen, it will never be changed throughout the game.
    """

    def __init__(self, word):
        """New Hangman game with chosen word from dictionary."""
        self.guesses = []

        #create a new set (built into python) that accounts for overlaps
        #to be able to see which guesses were correct
        self.correct = set()

        #initialize a list as an instance variable of all guesses
        #instance variable for the word
        self.word = word

    def guess(self, letter):
        """Taking guesses and checking word"""
        #if the letter is guessed and is in the word then return the letter
        if letter in self.guesses:
            return letter
        #add the guess to a list of "guessed" words
        self.guesses.append(letter)
        #sort list
        self.guesses.sort()
        #if the letter is guessed and is correct, then add it to the correct
        #letters list
        if letter in self.word:
            self.correct.add(letter)
    
    @property
    def visible(self):
        """Returns what the player is allowed to see"""
        #initialize blank string
        s = ""
        #add the letters that are in the word
        for letter in self.word:
            s += letter if letter in self.guesses else '*'
        return s

    @property
    def won(self):
        """Returns value indicating whether the player won"""
        #if the word that the player sees is the same as what they've guessed
        #return that they've won
        return self.word == self.visible

    @property
    def guessesLeft(self):
        """Returns number of guesses remaining"""
        #calculate how many guesses are remaining for this round
        return config.numGuesses - (len(self.guesses) - len(self.correct))

    @property
    def over(self):
        """Returns the state of the game - finished or not"""
        #this is so that there is a "game over" state for the game
        if self.guessesLeft <= 0 or self.won:
            return True
            print("Game Over")

    @property
    def ascii(self):
        """An ASCII art representation of the Hangman."""
        if self.guessesLeft >= 6:
            arr = ["________      ",
                   "|      |      ",
                   "|             ",
                   "|             ",
                   "|             ",
                   "|             "]
        elif self.guessesLeft == 5:
            arr = ["________      ",
                   "|      |      ",
                   "|      0      ",
                   "|             ",
                   "|             ",
                   "|             "]
        elif self.guessesLeft == 4:
            arr = ["________      ",
                   "|      |      ",
                   "|      0      ",
                   "|     /       ",
                   "|             ",
                   "|             "]
        elif self.guessesLeft == 3:
            arr = ["________      ",
                   "|      |      ",
                   "|      0      ",
                   "|     / \     ",
                   "|             ",
                   "|             "]
        elif self.guessesLeft == 2:
            arr = ["________      ",
                   "|      |      ",
                   "|      0      ",
                   "|     /|\     ",
                   "|             ",
                   "|             "]
        elif self.guessesLeft == 1:
            arr = ["________      ",
                   "|      |      ",
                   "|      0      ",
                   "|     /|\     ",
                   "|     /       ",
                   "|             "]
        else:
            arr = ["________      ",
                   "|      |      ",
                   "|      0      ",
                   "|     /|\     ",
                   "|     / \     ",
                   "|             "]
        return '\n'.join(arr)

        

class EvilHangman(Hangman):
    """Evil Hangman class! Algorithmically switches chosen word to a random word
from the dictionary, after which the game continues as normal"""

    def __init__(self, word):
        """Start a new game, but use this class to process guesses"""
        #initialize a new hangman game
        Hangman.__init__(self, word)
        #new words that have the given length
        self.wordBank = words.wordsOfLength(len(word))

    def guess(self, letter):
        """Change the word being guessed by sorting word into the various
groups"""

        #new group
        families = defaultdict(list)
        #loop through words in word bank with given length
        for word in self.wordBank:
            indices = [] #index to sort through word bank
            for i in range(0, len(self.word)): #loop through each letter of the word
                if word[i] == letter:
                    indices.append(i)
            families[tuple(indices)].append(word)
        self.wordBank = max(families.values(), key=lambda fam: len(fam))
        self.word = random.choice(self.wordBank)
        return Hangman.guess(self, letter)
