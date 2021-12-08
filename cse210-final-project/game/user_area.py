#Practice area for user to type their code. 
from game.actor import Actor

class UserArea(Actor):
    def __init__(self, text=None):
        super().__init__()
        self._text = text
        self._user_input = ""


    def add_letter(self, letter):
        """Adds the letter from user to string to display on Buffer.
        
        Args:
            self (Write): An instance of Write.
            string (letter): The letters to add to string.
        """
        self._user_input += letter
        return self._user_input

    def get_user_input(self):
        return self._user_input