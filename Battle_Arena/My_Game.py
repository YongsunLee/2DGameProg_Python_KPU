import os

os.chdir('D:/Job/2 - 2/2DGP/Project_Battle Arena/SunE_Repository/Battle_Arena/Asset')

import game_framework
from pico2d import *

import test_select

open_canvas(1280,720,sync=True)
game_framework.run(test_select)
close_canvas()