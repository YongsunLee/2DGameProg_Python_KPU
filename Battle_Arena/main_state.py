import os
os.chdir('D:/Job/2 - 2/2DGP/Project_Battle Arena/SunE_Repository/Battle_Arena/Asset')

from pico2d import *

import game_framework
import title_state
import Marie

name = "MainState"

current_time = 0.0

class BackGround:
    def __init__(self):
        self.image = load_image('BackGround.png')

    def draw(self):
        self.image.draw(640,360)
    pass

def enter():
    global player
    global background
    global frame_time

    player = Marie.Marie()
    background = BackGround()
    pass


def exit():
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN ,SDLK_ESCAPE):
                game_framework.change_state(title_state)
        else:
            player.handle_event(event)

def get_frame_time():
    global current_time
    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time

def update():
    global frame_time
    frame_time = get_frame_time()
    handle_events()
    player.update(frame_time)
    pass


def draw():
    clear_canvas()
    background.draw()
    player.draw()
    update_canvas()