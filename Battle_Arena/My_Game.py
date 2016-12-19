import platform
import os

# .. 은 상위폴더
# . 은 현재 폴더라는 의미이다.
#if platform.architecture()[0] == '32bit':
#    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x86"
#else:
#     os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x64"

import game_framework
from pico2d import *

import Test_Character

open_canvas(1280,720, sync=True)
game_framework.run(Test_Character)
close_canvas()