import os
os.chdir('D:/Job/2 - 2/2DGP/Project_Battle Arena/SunE_Repository/Battle_Arena/Asset')

from pico2d import *
import game_framework
import title_state
import Marie
import KaguyaHime

name = "MainState"

class BackGround:
    def __init__(self):
        self.image = load_image('BackGround.png')

    def draw(self):
        self.image.draw(640,360)
    pass

def enter():
    global player, p_persona
    global background
    global frame_time
    global com

    player = Marie.Marie()
    p_persona = KaguyaHime.Kaguya()


    com = Marie.Marie()

    com.x, com.y = 800, 180

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
            p_persona.handle_event(event)

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
    com.update(frame_time)
    p_persona.update(frame_time)
    p_persona.x = player.x
    p_persona.y = player.y + 100

    #delay(0.045)
    pass


def draw():
    clear_canvas()
    background.draw()
    p_persona.draw()
    player.draw()
    com.draw()
    update_canvas()