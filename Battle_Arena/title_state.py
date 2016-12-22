import os
os.chdir('D:/Job/2 - 2/2DGP/Project_Battle Arena/SunE_Repository/Battle_Arena/Asset')

from pico2d import *
import game_framework
import select_state

name = "TitleState"
image = None
title_load = 0.0

def enter():
    global image
    image = load_image('title.png')

def exit():
    global image
    del (image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type) == (SDL_KEYDOWN):
                game_framework.change_state(select_state)

def draw():
    clear_canvas()
    image.draw(640,360)
    update_canvas()


def update():
    global title_load


def pause():
    pass


def resume():
    pass






