import random

from hangman import Hangman
import actions

# File name with the available words
FILE = 'words.txt'

def play_game():
    # Save the list of available words.
    words = actions.obtain_words(FILE)
    
    # Creates a Hangman object with a random word  from words list.
    hg = Hangman(random.choice(words))

    # Prints the instructions and the hidden word length
    actions.print_rules_info()
    hg.print_guessed_letters()
    
    # Loops until the chances are equal to 0.
    while hg.chances >= 1:
        if not hg.word_found:
            letter = actions.obtain_letter()

            hg.search_letter(letter)
            hg.current_state()
        else:
            break
    
    # Runs when the user ends all opportunities.
    # Prints the hidden word
    if hg.chances == 0:
        print('\nGAME OVER!')
        print('The hidden word was:')
        hg.print_hidden_word()


if __name__ == '__main__':
   play_game()