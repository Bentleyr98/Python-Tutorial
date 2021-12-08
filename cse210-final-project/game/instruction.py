#From file, set instruction as an actor. Give text a position, width, height, and color.
from game.actor import Actor
from game import constants

class Instruction(Actor):
    
    def __init__(self, text=[]):
        super().__init__()
        self._list = text
        

           

       
