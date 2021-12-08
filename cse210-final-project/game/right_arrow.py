#actor for right arrow
from game.button import Button
from game import constants

class RightArrow(Button):
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Ball): an instance of Ball.
        """
        super().__init__()
        self._image = constants.RIGHT_ARROW
        self.set_width(constants.BUTTON_WIDTH)
        self.set_height(constants.BUTTON_HEIGHT)
       

    def get_image(self):
        """
        Returns image of actor
        """
        return self._image