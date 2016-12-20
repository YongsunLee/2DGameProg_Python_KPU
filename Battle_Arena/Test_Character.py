import os
#os.chdir('D:/Job/2 - 2/2DGP/Project_Battle Arena/SunE_Repository/Battle_Arena/Asset')

from pico2d import *
import game_framework
import Chie
import Marie_test

name = "Test_Character"

class BackGround:
    def __init__(self):
        self.image = load_image('BackGround.png')

    def draw(self):
        self.image.draw(640,360)
    pass

def enter():
    global player
    global frame_time
    global com

    #player = Chie.Chie()
    player = Marie_test.Marie()
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
        else:
            player.handle_event(event)
            pass

current_time = get_time()

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
    player.draw()
    update_canvas()