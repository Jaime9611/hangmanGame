import os

from hangman import Hangman


def play_game():
    hg = Hangman('beatifull')

    _print_rules_info()
    while hg.chances >= 1:
        letter = _obtain_letter()

        hg.search_letter(letter)
        hg.current_state()      
    
    if hg.chances == 0:
        print('\nGAME OVER!')


def _print_rules_info():
    print('*' * 80)
    print('*'*34 + 'HANGMAN GAME' + '*'*34)
    print('\nInsert a letter and try to guess the word.')
    print('You have 5 chances to guess the world.\n')


def _obtain_letter():  
    while True:
        letter = input('Insert the letter: ')

        if  letter.isalpha() and len(letter) == 1:
            break
        else:
            print('Invalid input. Try again.\n')
        
    return letter


if __name__ == '__main__':
   play_game()