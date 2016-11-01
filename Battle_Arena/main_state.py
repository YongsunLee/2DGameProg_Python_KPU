import os
os.chdir('D:/Job/2 - 2/2DGP/Project_Battle Arena/SunE_Repository/Battle_Arena/Asset')

from pico2d import *

import game_framework
import title_state
import Marie

name = "MainState"

class BackGround:
    def __init__(self):
        self.image = load_image('BackGround.png')

    def draw(self):
        self.image.draw(640,360)
    pass


def enter():
    global player
    global background

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


def update():
    player.update()
    delay(0.04)
    pass


def draw():
    clear_canvas()
    background.draw()
    player.draw()
    update_canvas()





