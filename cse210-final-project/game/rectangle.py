#Take input from user to personalize, then set user input as an actor.
from game.actor import Actor
from game import constants
from game.output_service import OutputService
import output_service

class Rectangle(Actor):
    
    def __init__(self):
        super().__init__()
        self._text = ""
        self._output_service = OutputService()
        
        
    def draw_rectangle(self):
        pass


    def set_width(self, width):
        self._width = width

    def set_height(self, height):
        self._height = height