from game import constants
from game.action import Action
from game.point import Point
from game.audio_service import AudioService
from game.physics_service import PhysicsService

class PlayCodeAction(Action):
    """Find the ball, paddle, and bricks.
    Then use the PhysicsService class to determine if they are colliding.

    If the ball and the paddle are colliding, the ball should bounce. 
    (Update its velocity similar to when it bounced off the walls.)
    If the ball and the paddle collide, you should play a sound.

    If the ball and bricks collide, remove bricks.
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            input_service (InputService): An instance of InputService.
        """
        self._audio_service = AudioService()
        self._physics_service = PhysicsService()


    def play(self, cast):
        mouse = cast["mouse"][0] # there's only one in the cast
        play = cast["play_button"][0]
        if not self._physics_service.is_collision(mouse, play):
            return True
        if self._physics_service.is_collision(mouse, play):
            return False
            
        








    