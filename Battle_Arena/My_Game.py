import os

os.chdir('D:/Job/2 - 2/2DGP/Project_Battle Arena/SunE_Repository/Battle_Arena/Asset')

import game_framework
from pico2d import *

import logo_state

open_canvas(1280,720)
game_framework.run(logo_state)
close_canvas()