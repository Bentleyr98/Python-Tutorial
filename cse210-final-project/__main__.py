import os
os.environ['RAYLIB_BIN_PATH'] = r'C:\Coding\cse210-student-solo-checkpoints\07-snake'
from time import sleep
import raylibpy

import random
from game import constants
from game.director import Director
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
from game.run_code import RunCode
from game.get_user_code import GetUserCode
from game.feedback import Feedback

def main():
    output_service = OutputService()
    input_service = InputService()
    audio_service = AudioService()

    # create the cast {key: tag, value: list}
    cast = {}

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


    # Create the script {key: tag, value: list}
    script = {}

    draw_actors_action = DrawActorsAction(output_service)
    run_code = RunCode()
    get_user_code = GetUserCode()
    

    script["input"] = [get_user_code]
    script["update"] = [run_code]
    script["output"] = [draw_actors_action]



    # Start the game
    output_service.open_window("Python Tutorial")

    user_name = UserName()
    cast["user_name"] = []
    user_names = []
    user_name.get_name()
    text = user_name.get_text()
    user_name.set_text(f"Hello {text}")
    user_name.set_position(Point(10, -5))
    user_names.append(user_name)
    cast["user_name"] = user_names

    cast["user_area"] = []
    users_area = []
    user_area = UserArea("Run your code below")
    user_area.set_position(Point(410,-5))
    users_area.append(user_area)
    user_area = UserArea()
    user_area.set_position(Point(150,315))
    users_area.append(user_area)
    cast["user_area"] = users_area

    cast["feedback"] = []
    feedback_text = []
    feedback = Feedback("Your Code: ")
    feedback.set_position(Point(10, 315))
    feedback_text.append(feedback)
    feedback_two = Feedback("The Result: ")
    feedback_two.set_position(Point(10, 440))
    feedback_text.append(feedback_two)
    feedback_three = Feedback()
    feedback_three.set_text("")
    feedback_three.set_position(Point(160, 440))
    feedback_text.append(feedback_three)
    cast["feedback"] = feedback_text



    
    output_service.flush_buffer()
    #audio_service.start_audio()
    #audio_service.play_sound(constants.SOUND_START)
    
    director = Director(cast, script)
    director.start_game()

    #audio_service.stop_audio()

if __name__ == "__main__":
    main()