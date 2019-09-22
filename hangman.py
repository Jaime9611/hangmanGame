
class Hangman:

    def __init__(self, hidden_word):
        self.hidden_word = list(hidden_word)
        self.guest_letters = self._hidden_format()
        self.word_found = False 
        self.chances = 5

    def current_state(self):       
        if self.hidden_word == self.guest_letters:
            self._print_current_list()
            print('YOUT GUEST IT !!')
            self.word_found = True
        else:
            self._print_chances_info()
            self._print_current_list()

    def search_letter(self, letter):
        if letter in self.hidden_word:
            self._found(letter)
        else:
            print('Not found.')
            self.chances -= 1

    def _found(self, letter):
        for i,v in enumerate(self.hidden_word):
            if v == letter:
                self.guest_letters[i] = letter

    def _print_current_list(self):
        print('') # print blank line
        for word in self.guest_letters:
            print(word, end=' ')
        print('\n') # print blank line

    def _print_chances_info(self):
        if self.chances == 1:
            msg = f'You have {self.chances} chance left.'
        elif self.chances > 0:
            msg = f'You stil have {self.chances} chances.'
        else:
            msg = f'No more chances.\n'

        print(msg)

    def _hidden_format(self):
        underscores = []
            
        for _ in self.hidden_word:
            underscores.append('_')
        
        return underscores

