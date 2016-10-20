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

            # 키 땠을때
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                player.frame_ = player.STAND_L
                player.walk_frame = 0
            elif event.key == SDLK_LEFT:
                player.frame_ = player.STAND_L
                player.backwalk_frame = 0
            elif event.key == SDLK_UP:
                player.frame_ = player.STAND_L
                player.jump_frame = 0
            elif event.key == SDLK_DOWN:
                player.frame_ = player.STAND_L
                player.down_frame = 0
            elif event.key == SDLK_LSHIFT:
                player.frame_ = player.STAND_L
            if event.key == SDLK_a:
                player.frame_ = player.STAND_L
                player.attack01_frame = 0
                player.attack02_frame = 0
            elif event.key == SDLK_s:
                player.frame_ = player.STAND_L
                player.attack00_frame = 0
            elif event.key == SDLK_d:
                player.frame_ = player.STAND_L
                player.call00_frame = 0
                player.call01_frame = 0

        # 눌렀을 때
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_UP:
                player.frame_ = player.JUMP_L
            elif event.key == SDLK_DOWN:
                player.frame_ = player.DOWN_L
            elif event.key == SDLK_RIGHT:
                if player.run_timer >= 1.0:
                    player.frame_ = player.RUN_L
                else:
                    player.frame_ = player.WALK_L
            elif event.key == SDLK_LEFT:
                if player.backstep_timer >= 1.0:
                    player.frame_ = player.BACKSTEP_L
                else:
                    player.frame_ = player.BACKWALK_L
            if event.key == SDLK_a:
                if player.attack01_tiemr >= 1.0:
                    player.frame_ = player.ATTACK02_L
                else:
                    player.frame_ = player.ATTACK01_L
            elif event.key == SDLK_s:
                player.frame_ = player.ATTACK00_L
            elif event.key == SDLK_d:
                if player.call_timer >= 1.0:
                    player.frame_ = player.CALL01_L
                else:
                    player.frame_ = player.CALL00_L
            elif event.key == SDLK_ESCAPE:
                game_framework.change_state(title_state)


def update():
    player.update()
    delay(0.04)
    pass


def draw():
    clear_canvas()
    background.draw()
    player.draw()
    update_canvas()





