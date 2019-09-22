import os

from hangman import Hangman
import actions


def play_game():
    hg = Hangman('beatifull')

    actions._print_rules_info()
    while hg.chances >= 1:
        if not hg.word_found:
            letter = actions._obtain_letter()

            hg.search_letter(letter)
            hg.current_state()
        else:
            break
    
    if hg.chances == 0:
        print('\nGAME OVER!')


if __name__ == '__main__':
   play_game()