import os

os.chdir('D:/Job/2 - 2/2DGP/Project_Battle Arena/SunE_Repository/Battle_Arena/Asset')

from pico2d import *
import game_framework

import title_state

name = "LogoState"
image = None
logo_time = 0.0
logo_load = 0.0

def enter():
    global image
    image = load_image('kpu_logo.png')


def exit():
    global image
    del(image)


def update():
    global logo_time
    global logo_load

    image.opacify(logo_load)
    print(logo_load)
    if logo_load < 1.0:
        logo_load += 0.01
    else:
        logo_load = 1.0

    if(logo_time > 1.0):
        logo_time = 0
        #game_framework.quit()
        game_framework.push_state(title_state)
    delay(0.01)
    logo_time += 0.01


def draw():
    global image
    clear_canvas()
    image.draw(640,360)
    update_canvas()




def handle_events():
    events = get_events()
    pass


def pause(): pass


def resume(): pass




