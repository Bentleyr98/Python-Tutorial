from game import constants
from game.action import Action
from game.point import Point


class HandleCollisionsAction(Action):
    """Find the ball, paddle, and bricks.
    Then use the PhysicsService class to determine if they are colliding.

    If the ball and the paddle are colliding, the ball should bounce. 
    (Update its velocity similar to when it bounced off the walls.)
    If the ball and the paddle collide, you should play a sound.

    If the ball and bricks collide, remove bricks.
    """
    def __init__(self, audio_service, physics_service):
        """The class constructor.
        
        Args:
            input_service (InputService): An instance of InputService.
        """
        self._audio_service = audio_service
        self._physics_service = physics_service


    def execute(self, cast):
        """Executes the actions to handle collisions with the ball, paddle, and bricks.
        
        Args:
            cast (dict): The Cast.
        """ 
        trash = cast["trash"][0]
        mouse = cast["mouse"][0] # there's only one in the cast
        feedback = cast["feedback"][2]
        user_code = cast["user_area"][1]


        if self._physics_service.is_collision(mouse, trash):
            feedback.set_text("")
            user_code.set_text("")
            


        

    

      