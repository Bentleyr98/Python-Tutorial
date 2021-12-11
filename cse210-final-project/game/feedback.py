from game.actor import Actor
from game.user_area import UserArea

class Feedback(Actor):
    def __init__(self, text=""):
        super().__init__()
        self._user_area = UserArea
        self._text = text


















    # def execute(self, cast):
    #     """Executes the action using the given actors.
    #     Args:
    #         cast (dict): The game actors {key: tag, value: list}.
    #     """
    #     raise NotImplementedError("execute not implemented in superclass")