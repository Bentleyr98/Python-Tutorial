from game.action import Action
from game.user_area import UserArea

class GetUserCode(Action):
    def __init__(self, cast) -> None:
        super().__init__()
        self._user_area = UserArea(cast)



    def execute(self, cast):
        user_area = cast["user_area"][1]
        user_area.get_code()