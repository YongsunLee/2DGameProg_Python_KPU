import os
os.chdir('D:/Job/2 - 2/2DGP/Project_Battle Arena/SunE_Repository/Battle_Arena/Asset')

from pico2d import *
import game_framework
import Chie
import Marie
import gameover_state
import select_state

name = "Test_Character"

class BackGround:
    def __init__(self):
        self.image = load_image('BackGround.png')

    def draw(self):
        self.image.draw(640,360)
    pass

s_player, s_com = 0 , 0

def enter():
    global data
    global s_player, s_com
    global background
    global player, com
    global frame_time

    f = open('select_data.txt', 'r')
    data = json.load(f)
    f.close()

    if data["s_player"] == 1:
        player = Chie.Chie()
        com = Marie.Marie()
    elif data["s_player"] == 2:
        player = Marie.Marie()
        com = Chie.Chie()

    print(data)

    #player = Chie.Chie()
    #com    = Marie.Marie()
    background = BackGround()

    player.x = 320
    player.y = 180
    com.dir = -1
    pass

def exit():
    pass

def pause():
    pass

def resume():
    pass

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True

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
    com.update(frame_time)
    com.ai_pattern(player)

    if player.x > com.x:
        player.dir = -1
        com.dir = 1
    else:
        player.dir = 1
        com.dir = -1

    if player.HP <= 0:
        game_framework.change_state(gameover_state)
    elif com.HP <= 0:
        game_framework.change_state(gameover_state)

    if collide(player, com):
        player.collision_events(com)
        com.collision_events(player)

def draw():
    clear_canvas()
    background.draw()
    player.draw()
    com.draw()
    update_canvas()


