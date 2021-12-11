from game.actor import Actor
from game.input_service import InputService
from game.output_service import OutputService

class UserArea(Actor):
    def __init__(self, text=""):
        super().__init__()
        self._text = text
        self._input_service = InputService()
        self._output_service = OutputService()


    def add_letter(self, letter):
        """Adds the letter from user to string to display on Buffer.
        
        Args:
            self (Write): An instance of Write.
            string (letter): The letters to add to string.
        """
        self._text += letter
        return self._text

    def remove_last_letter(self):
        self._text = self._text[:-1]


    def get_code(self):
        while not self._input_service.is_enter_pressed():
            code_space = "Enter Python Expression(Hit enter when finished) : "

            if self._input_service.is_backspaced_pressed():
                self.remove_last_letter()
            else:
                letter = self._input_service.get_letter()
                self.add_letter(letter)

            self._output_service.draw_text(410, 30, code_space, False)
            self._output_service.draw_text(410, 50, self._text, False)
            #self._audio_service.play_sound(constants.SOUND_OVER)
            self._output_service.flush_buffer()