import sys


def print_rules_info():
    """Print the game instructions"""
    print('*' * 80)
    print('*'*34 + 'HANGMAN GAME' + '*'*34)
    print('\nType a letter and try to guess the word.')
    print('or type "exit" to quit the game.')
    print('You have 10 chances to guess the world.')


def obtain_words(file_name):
    """Create a list with the words in the file"""
    words = []
    with open(file_name) as f:
        for line in f:
            words.append(line.rstrip())

    return words


def obtain_letter():
    """Return a valid input or exit the game.
    Evaluate the letter entered until it receive a valid entry(a letter)
    or the 'exit' word.
    """
    while True:
        letter = input('>> Insert the letter: ')

        if  letter.isalpha():
            if len(letter) == 1:
                break
            elif letter == 'exit':
                sys.exit()
            else:
                print('Type one letter only. Try again.\n')
        else:
            print('Type letters only. Try again.\n')
        
    return letter