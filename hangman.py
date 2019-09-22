
class Hangman:
    """Class to simulate a hangman game"""

    def __init__(self, hidden_word):
        self.hidden_word = list(hidden_word)
        self.guessed_letters = self._hidden_format()
        self.word_found = False 
        self.chances = 10

    def current_state(self):
        """Print the available opportunities and the guessed letters so far"""
        if self.hidden_word == self.guessed_letters:
            self.print_guessed_letters()
            print('YOUT GUEST IT !!')
            self.word_found = True
        else:
            self._print_chances_info()
            self.print_guessed_letters()

    def search_letter(self, letter):
        """Determines if the letter is in the hidden word"""
        if letter in self.hidden_word:
            self._found(letter)
        else:
            print('WRONG!!')
            self.chances -= 1

    def _found(self, letter):
        """
        Change the guessed letter list when the letter
        belongs to the hidden word.
        """
        for i,v in enumerate(self.hidden_word):
            if v == letter:
                self.guessed_letters[i] = letter

    def print_guessed_letters(self):
        """Prints the guessed_letter items"""
        print('') # print blank line
        for word in self.guessed_letters:
            print(word, end=' ')
        print('\n') # print blank line
    
    def print_hidden_word(self):
        """Prints the hidden_word list items"""
        print('') # print blank line
        for word in self.hidden_word:
            print(word, end=' ')
        print('\n') # print blank line

    def _print_chances_info(self):
        """Prints the user remaining chances"""
        if self.chances == 1:
            msg = f'You have {self.chances} chance left.'
        elif self.chances > 0:
            msg = f'You stil have {self.chances} chances.'
        else:
            msg = f'No more chances.\n'

        print(msg)

    def _hidden_format(self):
        """Return a list of '_' with the same length of hidden_word"""
        underscores = []
            
        for _ in self.hidden_word:
            underscores.append('_')
        
        return underscores

