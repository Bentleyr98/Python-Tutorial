#Take input from user to personalize, then set user input as an actor.
from game.actor import Actor
from game import constants

class UserName(Actor):
    
    def __init__(self):
        super().__init__()
        self._text = "Enter Name: "


    def get_name(self):
        self._text = 'Enter Name: '
        self.set_text(self._text)
