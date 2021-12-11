from game.action import Action
import io, sys

class RunCode(Action):
    def __init__(self) -> None:
        super().__init__()

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

            
        except:
            bad = ("Something wrong with the code")
            feedback = cast["feedback"][2]
            feedback.set_text(bad)