#Change game to match the levels. Will update instruction, feedback, user-area to match levels
from game.action import Action

class HandleLevelUps(Action):
    

    def execute(self, cast):
        """Executes the action using the given actors.
        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        raise NotImplementedError("execute not implemented in superclass")