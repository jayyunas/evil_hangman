#hangmanInterface.py
#Evil Hangman Interface
#Jay Yunas
#17th December, 2018

import random
import config

class HangmanUI:
    def __init__(self, game):
        self.game = game

    def play(self):
        game = self.game
        while not game.over:
            self.show_info()
            guess = self.request_guess()
            game.guess(guess)
        self.show_endgame()

    def show_info(self):
        """Show information about the current game state."""
        game = self.game
        s = '{0}\nYou used: {1}\nWord: {2}'.format(game.ascii, game.guesses, game.visible)
        if config.revealWord:
            s += '\nChosen Word: {0}'.format(game.word)
        if config.evil and config.revealWordBankSize:
            s += '\nWord Bank: {0} words'.format(len(game.wordBank))
        print(s)

    def request_guess(self):
        """Prompt the user to make a guess."""
        game = self.game
        while True:
            guess = input('Enter a letter: ').lower()
            if len(guess) == 1 and guess.isalpha():
                if guess in game.guesses:
                    print('Already guessed that.')
                else:
                    return guess
            elif len(guess) > 1:
                print('Sorry, only one letter at a time.')
            elif len(guess) == 0:
                print('Empty input not allowed.')
            else:
                print('Letters only.')

    def show_endgame(self):
        """Show information about the end of the game."""
        game = self.game
        print(game.ascii)
        print('The word was: ' + game.word)
        if game.won:
            print('Congratulations!')
        else:
            print('Better luck next time!')

    def playAgain(self):
        """Prompt the user to decide whether to play again."""
        while True:
            choice = input('Again? [y/n] ').lower()
            if choice == 'y' or choice == 'n':
                return choice == 'y'
            print("Didn't get that.")
