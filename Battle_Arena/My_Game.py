import os

os.chdir('D:/Job/2 - 2/2DGP/Project_Battle Arena/SunE_Repository/Battle_Arena/Asset')

import game_framework
from pico2d import *

import title_state

open_canvas(1280,720, sync=True)
game_framework.run(title_state)
close_canvas()