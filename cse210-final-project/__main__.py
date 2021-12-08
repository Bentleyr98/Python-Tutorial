import os
os.environ['RAYLIB_BIN_PATH'] = r'C:\Coding\cse210-student-solo-checkpoints\07-snake'
from time import sleep
import raylibpy

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
from game.instruction import Instruction
from game.play import Play
from game.trash import Trash
from game.left_arrow import LeftArrow
from game.right_arrow import RightArrow
from game.user_area import UserArea


def main():
    output_service = OutputService()
    input_service = InputService()
    audio_service = AudioService()
    user_name = UserName()
    user_area = UserArea()

    def get_name():
        get_user_name =" "
        x = len(get_user_name)
        while x < 20:
            output_service.clear_screen()
            raylibpy.clear_background(raylibpy.WHITE)
            name_space = "Enter Name: "
            letter = input_service.get_letter()
            get_user_name = user_name.add_letter(letter)
            name = (f"{name_space} {get_user_name}")
            print(name)
            output_service.draw_text(245, 250, name, True )
            #self._audio_service.play_sound(constants.SOUND_OVER)
            output_service.flush_buffer()
            output_service.clear_screen()

        raylibpy.clear_background(raylibpy.WHITE)
        output_service.flush_buffer()
           

    # create the cast {key: tag, value: list}
    cast = {}

    cast["user_name"] = []
    user_names = []
    user_name = UserName("Hello Person")
    user_name.set_position(Point(10, -5))
    user_names.append(user_name)
    cast["user_name"] = user_names

    cast["user_area"] = []
    users_area = []
    user_area = UserArea("Run your code below")
    user_area.set_position(Point(410,-5))
    users_area.append(user_area)
    cast["user_area"] = users_area

    cast["instruction"] = []
    text = []
    level_one = []

    for line in constants.LIBRARY:
        text.append(line)
    # print(level_one)

    # level_one.append(text)
    
    instructions = []
    instruction = Instruction(text)
    instruction.set_position(Point(5, 30))
    instructions.append(instruction)
    cast["instruction"] = instructions

    cast["play_button"] = []
    play_buttons = []
    play = Play()
    play.set_position(Point(770, 285))
    play_buttons.append(play)
    cast["play_button"] = play_buttons

    cast["trash"] = []
    trash_cans = []
    trash = Trash()
    trash.set_position(Point(770, 570))
    trash_cans.append(trash)
    cast["trash"] = trash_cans

    cast["right_arrow"] = []
    right_arrows = []
    right_arrow = RightArrow()
    right_arrow.set_position(Point(380,285))
    right_arrows.append(right_arrow)
    cast["right_arrow"] = right_arrows

    cast["left_arrow"] = []
    left_arrows = []
    left_arrow = LeftArrow()
    left_arrow.set_position(Point(10, 285))
    left_arrows.append(left_arrow)
    cast["left_arrow"] = left_arrows


    cast[""] = []
   
    


    # Create the script {key: tag, value: list}
    script = {}


    

    draw_actors_action = DrawActorsAction(output_service)


    script["input"] = []
    script["update"] = []
    script["output"] = [draw_actors_action]



    # Start the game
    output_service.open_window("Python Tutorial")
 
    get_name()
    output_service.flush_buffer()
    #audio_service.start_audio()
    #audio_service.play_sound(constants.SOUND_START)
    
    director = Director(cast, script)
    director.start_game()

    #audio_service.stop_audio()

if __name__ == "__main__":
    main()