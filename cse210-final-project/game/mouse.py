from game.actor import Actor
from game.input_service import InputService
from game.output_service import OutputService
from game import constants


class Mouse(Actor):
    
    def __init__(self):
        super().__init__()
        self._image = constants.MOUSE
        self.set_width(constants.DEFAULT_BLOCK_SIZE)
        self.set_height(constants.DEFAULT_BLOCK_SIZE)



    def return_image(self):
        return self._image