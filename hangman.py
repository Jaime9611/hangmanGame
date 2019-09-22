
def _hidden_format(hidden_word):
    underscores = []
        
    for _ in hidden_word:
        underscores.append('_')
        
    return underscores


class Hangman:

    def __init__(self, hidden_word):
        self.hidden_word = hidden_word
        self.guest_words = _hidden_format(hidden_word)
        self.chances = 5

    def current_state(self):        
        if self.chances == 1:
            msg = f'You have {self.chances} chance left.\n'
        elif self.chances > 0:
            msg = f'You stil have {self.chances} chances.\n'
        else:
            msg = f'No more chances.'

        print(msg)

    def search_letter(self, letter):
        if letter in self.hidden_word:
            print('Found.')
        else:
            print('Not found.')
            self.chances -= 1

        