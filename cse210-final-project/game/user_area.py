#Practice area for user to type their code. 
from game.actor import Actor
from game.input_service import InputService
from game.output_service import OutputService

class UserArea(Actor):
    def __init__(self, text=None):
        super().__init__()
        self._text = text
        self._user_input = ""
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

    def get_user_input(self):
        return self._user_input


    def get_code(self):
        while not self._input_service.is_enter_pressed():
            # self._output_service.clear_screen()
            # raylibpy.clear_background(raylibpy.WHITE)
            # name_space = "Enter Name: "
            if self._input_service.is_backspaced_pressed():
                self.remove_last_letter()
            else:
                letter = self._input_service.get_letter()
                self.add_letter(letter)
            
            # name = (f"{name_space} {self._user_input}")
            self._output_service.draw_text(245, 250, self._user_input, True )

            #self._audio_service.play_sound(constants.SOUND_OVER)
            self._output_service.flush_buffer()
        #     self._output_service.clear_screen()
        # raylibpy.clear_background(raylibpy.WHITE)
        self._output_service.flush_buffer()

    def exec_code(self):
        code = self._user_input
        exec(code)