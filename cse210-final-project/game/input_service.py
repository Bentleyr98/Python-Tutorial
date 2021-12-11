import sys
from game.point import Point
import raylibpy

class InputService:
    """Detects player input. The responsibility of the class of objects is to detect player keypresses and translate them into a point representing a direction (or velocity).
    Stereotype: 
        Service Provider
    Attributes:
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (InputService): An instance of InputService.
        """
        pass
        
    def get_letter(self):
        """Collects the user input into a string.

        Args:
            self (InputService): An instance of InputService.
        
    """
        key_string = ""
        key_int = raylibpy.get_key_pressed()
        if key_int != -1:
            key_string = chr(key_int)
        return key_string


    def is_left_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_LEFT)

    def is_right_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_RIGHT)

    def is_up_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_UP)

    def is_down_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_DOWN)

    def window_should_close(self):
        return raylibpy.window_should_close()

    def is_enter_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_ENTER)

    def is_backspaced_pressed(self):
        return raylibpy.is_key_pressed(raylibpy.KEY_BACKSPACE)