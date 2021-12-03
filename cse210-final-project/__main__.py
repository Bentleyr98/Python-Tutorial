import os
os.environ['RAYLIB_BIN_PATH'] = r'C:\Coding\cse210-student-solo-checkpoints\07-snake'
from time import sleep


import random
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.draw_actors_action import DrawActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from game.audio_service import AudioService
from game.user_name import UserName



def main():

    # create the cast {key: tag, value: list}
    cast = {}

    cast[""] = []
   
    

    cast["user_name"] = []
    user_names = []
    user_name = UserName()
    user_name.set_position(Point(50, 60))
    user_names.append(user_name)
    cast["user_name"] = [user_names]


    cast[""] = []
  


    # Create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    audio_service = AudioService()

    draw_actors_action = DrawActorsAction(output_service)


    script["input"] = []
    script["update"] = []
    script["output"] = [draw_actors_action]



    # Start the game
    output_service.open_window("Python Tutorial");
    #output_service.draw_box(0,0,50,50)

    output_service.flush_buffer()
    #audio_service.start_audio()
    #audio_service.play_sound(constants.SOUND_START)
    
    director = Director(cast, script)
    director.start_game()

    #audio_service.stop_audio()

if __name__ == "__main__":
    main()