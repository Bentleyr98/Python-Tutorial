import os

MAX_X = 800
MAX_Y = 600
FRAME_RATE = 30

BIG_FONT_SIZE = 25
DEFAULT_FONT_SIZE = 12
DEFAULT_TEXT_OFFSET = 10

PATH = os.path.dirname(os.path.abspath(__file__))
LIBRARY = open(PATH + "/tutorial.txt").read().splitlines()

LEFT_ARROW = os.path.join(os.getcwd(), "./cse210-final-project/assets/left_arrow.png")
RIGHT_ARROW = os.path.join(os.getcwd(), "./cse210-final-project/assets/right_arrow.png")
TRASH = os.path.join(os.getcwd(), "./cse210-final-project/assets/trash.png")
PLAY_BUTTON = os.path.join(os.getcwd(), "./cse210-final-project/assets/play_button.png")
MOUSE = os.path.join(os.getcwd(), "./cse210-final-project/assets/mouse.png")
PYTHON = os.path.join(os.getcwd(), "./cse210-final-project/assets/python.png")

SOUND_CORRECT = os.path.join(os.getcwd(), "./cse210-final-project/assets/correct_sound.wav")
SOUND_INCORRECT = os.path.join(os.getcwd(), "./cse210-final-project/assets/lost.wav")
SOUND_START = os.path.join(os.getcwd(), "./cse210-final-project/assets/intro_sound.wav")

BUTTON_WIDTH = 20
BUTTON_HEIGHT = 20

MOUSE_SPEED = 7
DEFAULT_BLOCK_SIZE = 15
