#main.py
#Main function
#Jay Yunas
#17th December, 2018

from words import *
from hangman import *
from hangmanui import HangmanUI
import config

def main():
    """Main Function"""
    #always start a new game
    while True:
        #initialize dictionary
        word = randWord(config.minWordLength, config.maxWordLength + 1)
        #initialize game
        game = HangmanUI(EvilHangman(word) if config.evil else Hangman(word))
        #play game
        game.play()
        #if player doesn't want to play again, break while loop
        if not game.playAgain():
            break
    #end game
    print("Thank you for playing! Have a good one.")

main()
