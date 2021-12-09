#Take input from user to personalize, then set user input as an actor.
from game.actor import Actor
from game.input_service import InputService
from game.output_service import OutputService
import raylibpy


class UserName(Actor):
    
    def __init__(self):
        super().__init__()
        self._user_input = ""
        self._text = (f"Hello {self._user_input}")
        self._input_service = InputService()
        self._output_service = OutputService()

    def add_letter(self, letter):
        """Adds the letter from user to string to display on Buffer.
        
        Args:
            self (Write): An instance of Write.
            string (letter): The letters to add to string.
        """
        self._user_input += letter
        return self._user_input

    
    def remove_last_letter(self):
        self._user_input = self._user_input.rstrip(self._user_input[:-1])


    def get_name(self):
        while not self._input_service.is_enter_pressed():
            self._output_service.clear_screen()
            raylibpy.clear_background(raylibpy.WHITE)
            name_space = "Enter Name: "
            if self._input_service.is_backspaced_pressed():
                self.remove_last_letter()
            else:
                letter = self._input_service.get_letter()
                self.add_letter(letter)
            
            name = (f"{name_space} {self._user_input}")
            self._output_service.draw_text(245, 250, name, True )

            #self._audio_service.play_sound(constants.SOUND_OVER)
            self._output_service.flush_buffer()
            self._output_service.clear_screen()
        raylibpy.clear_background(raylibpy.WHITE)
        self._output_service.flush_buffer()