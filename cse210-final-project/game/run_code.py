from game.action import Action
import io, sys
from game.audio_service import AudioService
from game import constants

class RunCode(Action):
    def __init__(self) -> None:
        super().__init__()
        self._audio_service = AudioService()

    def execute(self, cast):
        old_stdout = sys.stdout 
        new_stdout = io.StringIO()  
        sys.stdout = new_stdout 

        
        user_code = cast["user_area"][1]
        code = user_code.get_text()
        try:
           exec(code)
           feedback = cast["feedback"][2]
           
           result = sys.stdout.getvalue().strip()
           sys.stdout = old_stdout
           feedback.set_text(result)
           self._audio_service.play_sound(constants.SOUND_CORRECT)

            
        except:
            bad = ("Something wrong with the code. Please try again.")
            feedback = cast["feedback"][2]
            feedback.set_text(bad)
            self._audio_service.play_sound(constants.SOUND_INCORRECT)