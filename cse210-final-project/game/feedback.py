#Get feedback from terminal, give tips, and return Boolean if the user’s code is correct or not.
from game.actor import Actor
from game.user_area import UserArea

class Feedback(Actor):
    def __init__(self):
        super().__init__()
        self._user_area = UserArea
        self._input = self._user_area.get_user_input()

    def execute(self, cast):
        """Executes the action using the given actors.
        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        raise NotImplementedError("execute not implemented in superclass")