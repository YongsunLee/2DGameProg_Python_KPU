import os
os.chdir('D:/Job/2 - 2/2DGP/Project_Battle Arena/SunE_Repository/Battle_Arena/Asset')

from pico2d import *
import game_framework
import main_state
import json

name = "SelectState"
image = None
Marie_battle_coin = None
Chie_battle_coin = None
cursor = None

MARIE, CHIE = 1, 2

cursor_x = 770
cursor_y = 560

marie_cutstin_x ,marie_cutstin_y = 280, 510
marie_name_x , marie_name_y = 280, 250

chie_cutstin_x ,chie_cutstin_y = 1040, 450
chie_name_x , chie_name_y = 1040, 190

s_player, s_com = 0, 0

def draw_marie():
    global marie_cutsin, marie_name, marie_cutstin_x, marie_cutstin_y, marie_name_x, marie_name_y
    global s_player, s_com
    marie_cutsin = load_image('Marie_Select.png')
    marie_name = load_image('Name_Marie.png')

    marie_cutsin.draw(marie_cutstin_x, marie_cutstin_y)
    marie_name.draw(marie_name_x, marie_name_y)

def draw_chie():
    global chie_cutsin, chie_name, chie_cutstin_x ,chie_cutstin_y, chie_name_x , chie_name_y
    chie_cutsin = load_image('Chie_Select.png')
    chie_name = load_image('Name_Chie.png')

    chie_cutsin.draw(chie_cutstin_x, chie_cutstin_y)
    chie_name.draw(chie_name_x, chie_name_y)

    pass


def enter():
    global image, Marie_battle_coin, Chie_battle_coin, cursor
    global cursor_x, cursor_y
    image = load_image('Select_BG.png')
    Marie_battle_coin = load_image('Marie_Battle_coin.png')
    Chie_battle_coin = load_image('Chie_battle_coin.png')
    cursor = load_image('select_cursor.png')


def exit():
    global image, Marie_battle_coin, Chie_battle_coin, cursor, chie_cutsin, chie_name
    global marie_cutsin, marie_name

    data = {'s_player' : s_player, 's_com' : s_com}

    f = open('select_data.txt', 'w')
    json.dump(data, f)
    f.close()

    print(s_player)
    print(s_com)

    del (image)
    del (Marie_battle_coin)
    del (Chie_battle_coin)
    del (cursor)
    del (chie_cutsin)
    del (chie_name)
    del (marie_cutsin)
    del (marie_name)

def handle_events():
    global cursor_x, cursor_y, marie_cutstin_x, marie_cutstin_y, marie_name_x, marie_name_y
    global chie_cutstin_x ,chie_cutstin_y, chie_name_x , chie_name_y
    global s_player, s_com
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
                if (cursor_x, cursor_y) >= (680, 360):
                    #커서 좌표값
                    cursor_x , cursor_y = 680, 360
                    # 캐릭터 좌표값
                    # Maire
                    marie_cutstin_x, marie_cutstin_y = 1040, 450
                    marie_name_x, marie_name_y = 1040, 190

                    # Chie
                    chie_cutstin_x, chie_cutstin_y = 280, 510
                    chie_name_x, chie_name_y = 280, 250
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
                if (cursor_x, cursor_y) <= (680, 360):
                    # 커서 좌표값
                    cursor_x , cursor_y = 770, 560
                    # 캐릭터 좌표값
                    # marie
                    marie_cutstin_x, marie_cutstin_y = 280, 510
                    marie_name_x, marie_name_y = 280, 250

                    # chie
                    chie_cutstin_x, chie_cutstin_y = 1040, 450
                    chie_name_x, chie_name_y = 1040, 190

            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                if (cursor_x, cursor_y) == (770, 560):
                    #s_player = marie
                    s_player = MARIE
                    s_com = CHIE
                    pass
                elif (cursor_x, cursor_y) == (680, 360):
                    #s_player = chie
                    s_player = CHIE
                    s_com = MARIE
                    pass
                game_framework.push_state(main_state)
def draw():
    clear_canvas()
    image.draw(640,360)
    Marie_battle_coin.draw(680,560)
    Chie_battle_coin.draw(600,360)
    cursor.draw(cursor_x, cursor_y)
    draw_marie()
    draw_chie()
    update_canvas()


def update():
    pass

def pause():
    pass

def resume():
    pass