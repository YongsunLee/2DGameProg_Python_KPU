import os
os.chdir('D:/Job/2 - 2/2DGP/Project_Battle Arena/SunE_Repository/Battle_Arena/Asset')

from pico2d import *
import random

class Chie:
    # 이동 상태
    STAND_L, WALK_L, RUN_L, JUMP_L, DOWN_L, BACKWALK_L, BACKSTEP_L = 1, 2,  3,  4,  5,  6,  7
    STAND_R, WALK_R, RUN_R, JUMP_R, DOWN_R, BACKWALK_R, BACKSTEP_R = 8, 9, 10, 11, 12, 13, 14
    FALL = 15
    # 공격 상태
    SREG_L, SFIST_L, RKICK_L = 16, 17, 18
    SREG_R, SFIST_R, RKICK_R = 19, 20, 21
    # 방어 상태
    GSTAND_L, GDOWN_L = 22, 23
    GSTAND_R, GDOWN_R = 24, 25
    # 피격 상태
    HSTAND_L, HDOWN_L = 26, 27
    HSTAND_R, HDOWN_R = 28, 29
    # 페르소나 호출 상태
    CCOM_L, CPRO_L = 30, 31
    CCOM_R, CPRO_R = 32, 33
    # 승리 상태
    WIN_L = 34
    WIN_R = 35

    # 물리적 속도 지정
    PIXEL_PER_METER = (250.0 / 1.6)  # 250 pixel 160cm // 1 pixel 0.64cm
    GRAVITY = 9.8
    # 걷기
    WALK_SPEED_KMPH = 10.0  # Km / Hour
    WALK_SPEED_PPS = (((WALK_SPEED_KMPH * 1000.0 / 60.0) / 60.0) * PIXEL_PER_METER)
    BACKWALK_SPEED_KMPH = 5.0  # Km / Hour
    BACKWALK_SPEED_PPS = (((BACKWALK_SPEED_KMPH * 1000.0 / 60.0) / 60.0) * PIXEL_PER_METER)
    # 뛰기
    RUN_SPEED_KMPH = 20.0  # Km / Hour
    RUN_SPEED_PPS = (((RUN_SPEED_KMPH * 1000.0 / 60.0) / 60.0) * PIXEL_PER_METER)
    BACKSTEP_SPEED_KMPH = 15.0  # Km / Hour
    BACKSTEP_SPEED_PPS = (((BACKSTEP_SPEED_KMPH * 1000.0 / 60.0) / 60.0) * PIXEL_PER_METER)
    # 점프
    JUMP_SPEED_KMPH = 20.0
    JUMP_SPEED_PPS = (((JUMP_SPEED_KMPH * 1000.0 / 60.0) / 60.0) * PIXEL_PER_METER)

    # 액션 프레임 조절
    TIME_PER_ACTION = 1.0
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 12

    # 속도 계산 핸들____________________________________________________________________
    def handle_speed(self, frame_time):
        global walk_speed, backwalk_speed, run_speed, backstep_speed, jump_speed
        walk_speed     = self.WALK_SPEED_PPS       * frame_time
        backwalk_speed = self.BACKWALK_SPEED_PPS   * frame_time
        run_speed      = self.RUN_SPEED_PPS        * frame_time
        backstep_speed = self.BACKSTEP_SPEED_PPS   * frame_time
        jump_speed     = self.JUMP_SPEED_PPS       * frame_time

        self.key_timer += self.FRAMES_PER_ACTION * self.ACTION_PER_TIME * frame_time
        self.total_frame += self.FRAMES_PER_ACTION * self.ACTION_PER_TIME * frame_time
    #__속도 계산 끝_____________________________________________________________________

    # 프레임 출력함수________________________
    def handle_frame_stand(self):
        self.stand_frame = int(self.total_frame) % 10
    def handle_frame_walk(self):
        if self.key_timer < 3.0:
            self.walk_frame = int(self.total_frame) % 6 + 2
            if self.walk_frame == 5 and self.rand_val != 0:
                self.rand_val = 0
        else:
            self.walk_frame = int(self.total_frame) % 8
            if self.walk_frame == 7 and self.rand_val != 0:
                self.rand_val = 0
        self.x += (self.dir * walk_speed)
        self.key_timer = int(self.key_timer) % 4
    def handle_frame_backwalk(self):
        if self.key_timer > 3.0:
            self.backwalk_frame = int(self.total_frame) % 6 + 2
            if self.backwalk_frame == 5 and self.rand_val != 0:
                self.rand_val = 0
        else:
            self.backwalk_frame = int(self.total_frame) % 8
            if self.backwalk_frame == 7 and self.rand_val != 0:
                self.rand_val = 0
        self.x -= (self.dir * backwalk_speed)
        self.key_timer = int(self.key_timer) % 3
    def handle_frame_run(self):
        if self.key_timer > 3.0:
            self.run_frame = 3
            self.run_frame = int(self.total_frame) % 8
            if self.run_frame == 7 and self.rand_val != 0:
                self.rand_val = 0
        else:
            self.run_frame = int(self.total_frame) % 11
            if self.run_frame == 10 and self.rand_val != 0:
                self.rand_val = 0
        self.x += (self.dir * run_speed)
    def handle_frame_down(self):
        if self.key_timer > 3.0:
            self.down_frame = int(self.total_frame) % 6 + 3
            if self.down_frame == 5 and self.rand_val != 0:
                self.rand_val = 0
        else:
            self.down_frame = int(self.total_frame) % 10
            if self.down_frame == 9 and self.rand_val != 0:
                self.rand_val = 0
    def handle_frame_jump(self):
        self.jump_frame = int(self.total_frame) % 8
        self.y += int(jump_speed)
        if self.jumping_Left_move == True:
            if self.dir == 1: self.x -= (self.dir * walk_speed)
            else:             self.x += (self.dir * walk_speed)
        elif self.jumping_Right_move == True:
            if self.dir == 1: self.x += (self.dir * walk_speed)
            else:             self.x -= (self.dir * walk_speed)
        if self.y >= 340:
            self.state = self.FALL
    def handle_frame_fall(self):
        self.jump_frame = int(self.total_frame) % 16 + 8
        self.y -= int(jump_speed)
        if self.jumping_Left_move:
            if self.dir == 1: self.x -= (self.dir * walk_speed)
            else:             self.x += (self.dir * walk_speed)
        elif self.jumping_Right_move:
            if self.dir == 1: self.x += (self.dir * walk_speed)
            else:             self.x -= (self.dir * walk_speed)
        if self.y <= 180:
            if self.dir == 1:
                if self.jumping_Left_move:
                    self.state = self.BACKWALK_L
                elif self.jumping_Right_move:
                    self.state = self.WALK_L
                else:
                    self.state = self.STAND_L
            elif self.dir == -1:
                if self.jumping_Left_move:
                    self.state = self.WALK_R
                elif self.jumping_Right_move:
                    self.state = self.BACKWALK_L
                else:
                    self.state = self.STAND_R
    def handle_frame_backstep(self):
        self.backstep_frame = int(self.total_frame) % 5
        self.x -= (self.dir * backstep_speed)
        if self.backstep_frame == 4:
            if self.dir == 1:
                self.state = self.STAND_L
            elif self.dir == -1:
                self.state = self.STAND_R
            if self.rand_val != 0:
                self.rand_val = 0
            self.backstep_frame = 0
    def handle_frame_sfist(self):
        self.s_fist_frame = int(self.total_frame) % 5
        if self.s_fist_frame == 4:
            if   self.dir == 1: self.state = self.STAND_L
            else              : self.state = self.STAND_R
        if self.rand_val != 0:
            self.rand_val = 0
    def handle_frame_sreg(self):
        self.s_reg_frame = int(self.total_frame) % 11
        if self.s_reg_frame == 10:
            if   self.dir == 1:
                self.state = self.STAND_L
            else              :
                self.state = self.STAND_R
            if self.rand_val != 0:
                self.rand_val = 0
        self.key_timer = int(self.key_timer) % 4
    def handle_frame_rkick(self):
        self.round_kick_frame = int(self.total_frame) % 9
        if self.round_kick_frame == 8:
            if   self.dir == 1:
                self.state = self.STAND_L
            else              :
                self.state = self.STAND_R
            if self.rand_val != 0:
                self.rand_val = 0
    def handle_frame_gstand(self):
        self.g_stand_frame = int(self.total_frame) % 5
        if self.g_stand_frame == 4:
            if self.dir == 1:
                self.state = self.STAND_L
            else:
                self.state = self.STAND_R
            if self.rand_val != 0:
                self.rand_val = 0
    def handle_frame_gdown(self):
        self.g_down_frame = int(self.total_frame) % 5
        if self.g_down_frame == 4:
            if self.dir == 1:
                self.state = self.DOWN_L
            else:
                self.state = self.DOWN_R
            if self.rand_val != 0:
                self.rand_val = 0
    def handle_frame_hstand(self):
        self.h_stand_frame = int(self.total_frame) % 5
        if self.h_stand_frame == 4:
            if self.dir == 1:
                self.state = self.STAND_L
            else:
                self.state = self.STAND_R
            if self.rand_val != 0:
                self.rand_val = 0
    def handle_frame_hdown(self):
        self.h_down_frame = int(self.total_frame) % 5
        if self.h_down_frame == 4:
            if self.dir == 1:
                self.state = self.STAND_L
            else:
                self.state = self.STAND_R
            if self.rand_val != 0:
                self.rand_val = 0
    def handle_frame_ccom(self):
        self.c_common_frame = int(self.total_frame) % 15
        if self.c_common_frame == 14:
            if self.dir == 1:
                self.state = self.STAND_L
            else:
                self.state = self.STAND_R
            if self.rand_val != 0:
                self.rand_val = 0
        self.key_timer = int(self.key_timer) % 3
    def handle_frame_cpro(self):
        self.c_provoke_frame = int(self.total_frame) % 7
        if self.c_provoke_frame == 6:
            if self.dir == 1:
                self.state = self.STAND_L
            else:
                self.state = self.STAND_R
            if self.rand_val != 0:
                self.rand_val = 0
    def handle_frame_win(self):
        self.win_frame = int(self.total_frame) % 10
        if self.win_frame == 9:
            if self.dir == 1:
                self.state = self.STAND_L
            else:
                self.state = self.STAND_R
    #______________________________________

    # 이미지 출력 함수_____________________
    def handle_image_stand(self):
        if self.dir    == 1:
            self.image_stand_L.clip_draw(self.stand_frame * 148, 0, 148, 250, self.x, self.y)
        elif self.dir == -1:
            self.image_stand_R.clip_draw(self.stand_frame * 148, 0, 148, 250, self.x, self.y)
    def handle_image_walk(self):
        if self.dir   ==  1:
            self.image_walk_L.clip_draw(self.walk_frame * 150, 0, 150, 250, self.x, self.y)
        elif self.dir == -1:
            self.image_walk_R.clip_draw(self.walk_frame * 150, 0, 150, 250, self.x, self.y)
    def handle_image_backwalk(self):
        if self.dir   ==  1:
            self.image_backwalk_L.clip_draw(self.backwalk_frame * 157, 0, 157, 250, self.x, self.y)
        elif self.dir == -1:
            self.image_backwalk_R.clip_draw(self.backwalk_frame * 157, 0, 157, 250, self.x, self.y)
    def handle_image_run(self):
        if self.dir == 1:
            self.image_run_L.clip_draw(self.run_frame * 250, 0, 250, 250, self.x, self.y)
        elif self.dir == -1:
            self.image_run_R.clip_draw(self.run_frame * 250, 0, 250, 250,self.x, self.y)
    def handle_image_down(self):
        if self.dir == 1:
            self.image_down_L.clip_draw(self.down_frame * 125, 0, 125, 250, self.x, self.y)
        elif self.dir == -1:
            self.image_down_R.clip_draw(self.down_frame * 125, 0, 125, 250, self.x, self.y)
    def handle_image_jump(self):
        if self.dir == 1:
            self.image_jump_L.clip_draw(self.jump_frame * 121, 0, 121, 280, self.x, self.y)
        elif self.dir == -1:
            self.image_jump_R.clip_draw(self.jump_frame * 121, 0, 121, 280, self.x, self.y)
    def handle_image_fall(self):
        if self.dir == 1:
            self.image_jump_L.clip_draw((16 - self.jump_frame) * 121, 0, 121, 280, self.x, self.y )
        elif self.dir == -1:
            self.image_jump_R.clip_draw((16 - self.jump_frame) * 121, 0, 121, 280, self.x, self.y)
    def handle_image_backstep(self):
        if self.dir == 1:
            self.image_backstep_L.clip_draw(self.backstep_frame * 160, 0, 160, 250, self.x, self.y)
        elif self.dir == -1:
            self.image_backstep_R.clip_draw(self.backstep_frame * 160, 0, 160, 250, self.x, self.y)
    def handle_image_sfist(self):
        if self.dir == 1:
            self.image_s_fist_L.clip_draw(self.s_fist_frame * 180, 0, 180, 250, self.x, self.y)
        elif self.dir == -1:
            self.image_s_fist_R.clip_draw(self.s_fist_frame * 180, 0, 180, 250, self.x, self.y)
    def handle_image_sreg(self):
        if self.dir == 1:
            self.image_simple_reg_L.clip_draw(self.s_reg_frame * 390, 0, 390, 250, self.x, self.y)
        elif self.dir == -1:
            self.image_simple_reg_R.clip_draw(self.s_reg_frame * 390, 0, 390, 250, self.x, self.y)
    def handle_image_rkick(self):
        self.s_reg_frame = 0
        if self.dir == 1:
            self.image_round_kick_L.clip_draw(self.round_kick_frame * 350, 0, 350, 250, self.x, self.y)
        elif self.dir == -1:
            self.image_round_kick_R.clip_draw(self.round_kick_frame * 350, 0, 350, 250, self.x, self.y)
    def handle_image_gstand(self):
        if self.dir == 1:
            self.image_gard_stand_L.clip_draw(self.g_stand_frame * 180, 0, 180, 250, self.x, self.y)
        elif self.dir == -1:
            self.image_gard_stand_R.clip_draw(self.g_stand_frame * 180, 0, 180, 250, self.x, self.y)
    def handle_image_gdown(self):
        if self.dir == 1:
            self.image_gard_down_L.clip_draw(self.g_down_frame * 121, 0, 121, 250, self.x, self.y)
        elif self.dir == -1:
            self.image_gard_down_R.clip_draw(self.g_down_frame * 121, 0, 121, 250, self.x, self.y)
    def handle_image_hstand(self):
        if self.dir == 1:
            self.image_hit_stand_L.clip_draw(self.h_stand_frame * 200, 0, 200, 250, self.x, self.y)
        elif self.dir == -1:
            self.image_hit_stand_R.clip_draw(self.h_stand_frame * 200, 0, 200, 250, self.x, self.y)
    def handle_image_hdown(self):
        if self.dir == 1:
            self.image_hit_down_L.clip_draw(self.h_down_frame * 200, 0, 200, 250, self.x, self.y)
        elif self.dir == -1:
            self.image_hit_down_R.clip_draw(self.h_down_frame * 200, 0, 200, 250, self.x, self.y)
    def handle_image_ccom(self):
        if self.dir == 1:
            self.image_call_common_L.clip_draw(self.c_common_frame * 200, 0, 200, 280, self.x, self.y)
        elif self.dir == -1:
            self.image_call_common_R.clip_draw(self.c_common_frame * 200, 0, 200, 280, self.x, self.y)
    def handle_image_cpro(self):
        if self.dir == 1:
            self.image_call_provoke_L.clip_draw(self.c_provoke_frame * 200, 0, 200, 280, self.x, self.y)
        elif self.dir == -1:
            self.image_call_provoke_R.clip_draw(self.c_provoke_frame * 200, 0, 200, 280, self.x, self.y)
    def handle_image_win(self):
        if self.dir == 1:
            self.image_win_L.clip_draw(self.win_frame * 350, 0, 350, 280, self.x, self.y)
        elif self.dir == -1:
            self.image_win_R.clip_draw(self.win_frame * 350, 0, 350, 280, self.x, self.y)
    #______________________________________

    # 프레임 갱신 핸들__________________________
    frame_handle = {
        STAND_L    : handle_frame_stand,
        STAND_R    : handle_frame_stand,
        WALK_L     : handle_frame_walk,
        WALK_R     : handle_frame_walk,
        BACKWALK_L : handle_frame_backwalk,
        BACKWALK_R : handle_frame_backwalk,
        RUN_L      : handle_frame_run,
        RUN_R      : handle_frame_run,
        DOWN_L     : handle_frame_down,
        DOWN_R     : handle_frame_down,
        JUMP_L     : handle_frame_jump,
        JUMP_R     : handle_frame_jump,
        BACKSTEP_L : handle_frame_backstep,
        BACKSTEP_R : handle_frame_backstep,
        FALL       : handle_frame_fall,
        SREG_L     : handle_frame_sreg,
        SREG_R     : handle_frame_sreg,
        RKICK_L   : handle_frame_rkick,
        RKICK_R   : handle_frame_rkick,
        SFIST_L   : handle_frame_sfist,
        SFIST_R   : handle_frame_sfist,
        GSTAND_L   : handle_frame_gstand,
        GSTAND_R   : handle_frame_gstand,
        GDOWN_L    : handle_frame_gdown,
        GDOWN_R    : handle_frame_gdown,
        HSTAND_L   : handle_frame_hstand,
        HSTAND_R   : handle_frame_hstand,
        HDOWN_L    : handle_frame_hdown,
        HDOWN_R    : handle_frame_hdown,
        CCOM_L     : handle_frame_ccom,
        CCOM_R     : handle_frame_ccom,
        CPRO_L     : handle_frame_cpro,
        CPRO_R     : handle_frame_cpro,
        WIN_L      : handle_frame_win,
        WIN_R      : handle_frame_win
    }
    #________________________________________________

    # 이미지 출력 핸들_______________________________
    image_handle = {
        STAND_L    : handle_image_stand,
        STAND_R    : handle_image_stand,
        WALK_L     : handle_image_walk,
        WALK_R     : handle_image_walk,
        BACKWALK_L : handle_image_backwalk,
        BACKWALK_R : handle_image_backwalk,
        RUN_L      : handle_image_run,
        RUN_R      : handle_image_run,
        DOWN_L     : handle_image_down,
        DOWN_R     : handle_image_down,
        JUMP_L     : handle_image_jump,
        JUMP_R     : handle_image_jump,
        BACKSTEP_L : handle_image_backstep,
        BACKSTEP_R : handle_image_backstep,
        FALL       : handle_image_fall,
        SREG_L     : handle_image_sreg,
        SREG_R     : handle_image_sreg,
        RKICK_L    : handle_image_rkick,
        RKICK_R    : handle_image_rkick,
        SFIST_L    : handle_image_sfist,
        SFIST_R    : handle_image_sfist,
        GSTAND_L   : handle_image_gstand,
        GSTAND_R   : handle_image_gstand,
        GDOWN_L    : handle_image_gdown,
        GDOWN_R    : handle_image_gdown,
        HSTAND_L   : handle_image_hstand,
        HSTAND_R   : handle_image_hstand,
        HDOWN_L    : handle_image_hdown,
        HDOWN_R    : handle_image_hdown,
        CCOM_L     : handle_image_ccom,
        CCOM_R     : handle_image_ccom,
        CPRO_L     : handle_image_cpro,
        CPRO_R     : handle_image_cpro,
        WIN_L      : handle_image_win,
        WIN_R      : handle_image_win
    }
    #__________________________________________________

    # 키입력 함수________________________________________________________________________________
    def handle_event(self, event):
        # KeyDown_____________________________________________________
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_1):
            if   self.dir ==  1:    self.dir = -1
            elif self.dir == -1:    self.dir = 1
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            if self.y == self.default_yPos:
                if   self.dir ==  1:
                    if self.key_timer < 3.0:
                        self.state = self.BACKSTEP_L
                    else:
                        self.state = self.BACKWALK_L
                elif self.dir == -1:
                    if self.key_timer < 3.0:
                        self.state = self.RUN_R
                    else:
                        self.state = self.WALK_R
            self.jumping_Left_move = True
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            if self.y == self.default_yPos:
                if   self.dir ==  1:
                    if self.key_timer < 4.0:
                        self.state = self.RUN_L
                    else:
                        self.state = self.WALK_L
                elif self.dir == -1:
                    if self.key_timer < 4.0:
                        self.state = self.BACKSTEP_R
                    else:
                        self.state = self.BACKWALK_R
            self.jumping_Right_move = True
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
            if self.y == self.default_yPos:
                if self.dir == 1:
                    self.state = self.DOWN_L
                elif self.dir == -1:
                    self.state = self.DOWN_R
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
            if self.dir == 1:
                self.state = self.JUMP_L
            elif self.dir == -1:
                self.state = self.JUMP_R
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_a):
            if self.y == self.default_yPos:
                if self.dir == 1:
                    self.state = self.SFIST_L
                elif self.dir == -1:
                    self.state = self.SFIST_R
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_s):
            if self.y == self.default_yPos:
                if self.dir == 1:
                    if self.key_timer < 4.0:
                        self.state = self.RKICK_L
                    else:
                        self.state = self.SREG_L
                elif self.dir == -1:
                    if self.key_timer < 4.0:
                        self.state = self.RKICK_R
                    else:
                        self.state = self.SREG_R
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_d):
            if self.dir == 1:
                if self.key_timer < 3.0:
                    self.state = self.CPRO_L
                else:
                    self.state = self.CCOM_L
            elif self.dir == -1:
                if self.key_timer < 3.0:
                    self.state = self.CPRO_R
                else:
                    self.state = self.CCOM_R
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_z):
            if self.dir == 1:
                if self.state == self.STAND_L:
                    self.state = self.GSTAND_L
                elif self.state == self.DOWN_L:
                    self.state = self.GDOWN_L
            else:
                if self.state == self.STAND_R:
                    self.state = self.GSTAND_R
                elif self.state == self.DOWN_R:
                    self.state = self.GDOWN_R
        #_________________________________________________________

        # Key UP__________________________________________________
        if (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            if self.y == self.default_yPos:
                if self.dir == 1:
                    self.state = self.STAND_L
                elif self.dir == -1:
                    self.state = self.STAND_R
            self.jumping_Left_move = False
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            if self.y == self.default_yPos:
                if self.dir == 1:
                    self.state = self.STAND_L
                elif self.dir == -1:
                    self.state = self.STAND_R
            self.jumping_Right_move = False
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_DOWN):
            if self.dir == 1:
                self.state = self.STAND_L
            elif self.dir == -1:
                self.state = self.STAND_R
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_z):
            if self.dir == 1:
                if self.state == self.GSTAND_L:
                    self.state = self.STAND_L
                elif self.state == self.GDOWN_L:
                    self.state = self.DOWN_L
            else:
                if self.state == self.GSTAND_R:
                    self.state = self.STAND_R
                elif self.state == self.GDOWN_R:
                    self.state = self.DOWN_R
        #________________________________________________________
    #__키입력 종료___________________________________________________________________


    # 충돌 처리__________________________________________
    def collision_events(self, enemy):
        # 때렸을 때
        if self.state in (self.SREG_L, self.RKICK_L, self.SFIST_L):
            # 페르소나 호출기회 획득
            if enemy.state in (enemy.STAND_R, enemy.WALK_R, enemy.RUN_R, enemy.BACKSTEP_R, enemy.BACKWALK_R):
                enemy.state = enemy.HSTAND_R
            elif enemy.state == enemy.DOWN_R:
                enemy.state = enemy.HDOWN_R
            if self.summon_count <= 3:
                self.summon_count = self.summon_count + 1
            pass
        # 맞았을 때 ( 스탠딩 모션 )
        elif self.state in (self.STAND_L, self.WALK_L, self.RUN_L, self.BACKSTEP_L, self.BACKWALK_L):
            if enemy.state in (enemy.SREG_R, enemy.RSWING_R, enemy.USWING_R):
                self.state = self.HSTAND_L
                self.HP = self.HP - 10
        elif self.state == self.DOWN_L:
            if enemy.state in (enemy.SREG_R, enemy.RSWING_R, enemy.USWING_R):
                self.state = self.HDOWN_L
                self.HP = self.HP - 10
        # 막았을 때
        elif self.state in (self.GSTAND_L, self.GDOWN_L):
            # 체력감소 조금
            if enemy.state in (enemy.SREG_R, enemy.RSWING_R, enemy.USWING_R):
                self.HP = self.HP - 10

        # 때렸을 때
        if self.state in (self.SREG_R, self.RKICK_R, self.SFIST_R):
            # 페르소나 호출기회 획득
            if enemy.state in (enemy.STAND_L, enemy.WALK_L, enemy.RUN_L, enemy.BACKSTEP_L, enemy.BACKWALK_L):
                enemy.state = enemy.HSTAND_L
            elif enemy.state == enemy.DOWN_L:
                enemy.state = enemy.HDOWN_L
            if self.summon_count <= 3:
                self.summon_count = self.summon_count + 1
            pass
        # 맞았을 때 ( 스탠딩 모션 )
        elif self.state in (self.STAND_R, self.WALK_R, self.RUN_R, self.BACKSTEP_R, self.BACKWALK_R):
            if enemy.state in (enemy.SREG_R, enemy.RSWING_R, enemy.USWING_R):
                self.state = self.HSTAND_R
                self.HP = self.HP - 10
        elif self.state == self.DOWN_R:
            if enemy.state in (enemy.SREG_R, enemy.RSWING_R, enemy.USWING_R):
                self.state = self.HDOWN_R
                self.HP = self.HP - 10
        # 막았을 때
        elif self.state in (self.GSTAND_R, self.GDOWN_R):
            # 체력감소 조금
            if enemy.state in (enemy.SREG_R, enemy.RSWING_R, enemy.USWING_R):
                self.HP = self.HP - 10
    #__충돌처리 종료______________________________________________

    # AI 패턴____________________________________________________________________
    # 일정거리를 준다. (self.x 기준으로)
    # 특정 범위 안에 들어오면 특정 패턴으로 작동
    # 1. 이동 ( 빽, 앞, 앉기, 점프 )
    # 2. 공격 ( 심플, 라운드, 페르소나 콜링- 갯수가 남았을때- )
    # 3. 가드 ( 적이 심하게 가까울때 )
    def ai_pattern(self, player):
        if self.dir == 1:
            if player.x < (self.x + 100):
                if self.rand_val == 0:
                    self.rand_val = random.randint(1,8)
                if   self.rand_val == 1:                                self.state = self.BACKWALK_L
                elif self.rand_val == 2:                                self.state = self.BACKSTEP_L
                elif self.rand_val == 3:                                self.state = self.SREG_L
                elif self.rand_val == 4:                                self.state = self.RKICK_L
                elif self.rand_val == 5 and self.summon_count != 0:    self.state = self.CCOM_L
                elif self.rand_val == 6:                                self.state = self.DOWN_L
                elif self.rand_val == 7:                                self.state = self.GSTAND_L
                elif self.rand_val == 8 and self.state == self.DOWN_L: self.state = self.GDOWN_L
            elif player.x < (self.x + 200):
                if self.rand_val == 0:
                    self.rand_val = random.randint(1,8)
                if self.rand_val == 1:                                  self.state = self.BACKWALK_L
                elif self.rand_val == 2:                                self.state = self.BACKSTEP_L
                elif self.rand_val == 3:                                self.state = self.SREG_L
                elif self.rand_val == 4:                                self.state = self.RKICK_L
                elif self.rand_val == 5 and self.summon_count != 0:     self.state = self.CCOM_L
                elif self.rand_val == 6:                                self.state = self.DOWN_L
                elif self.rand_val == 7:                                self.state = self.WALK_L
                elif self.rand_val == 8:                                self.state = self.RUN_L
            elif player.x < (self.x + 300):
                if self.rand_val == 0:
                    self.rand_val = random.randint(1,8)
                if self.rand_val == 1:                                  self.state = self.BACKWALK_L
                elif self.rand_val == 2:                                self.state = self.BACKSTEP_L
                elif self.rand_val == 3:                                self.state = self.SREG_L
                elif self.rand_val == 4:                                self.state = self.RKICK_L
                elif self.rand_val == 5 and self.summon_count != 0:     self.state = self.CCOM_L
                elif self.rand_val == 6:                                self.state = self.DOWN_L
                elif self.rand_val == 7:                                self.state = self.WALK_L
                elif self.rand_val == 8:                                self.state = self.RUN_L
        # 플레이어의 x 값이 큼
        elif self.dir == -1:
            if player.x > (self.x - 100):
                if self.rand_val == 0:
                    self.rand_val = random.randint(1,8)
                if   self.rand_val == 1:                                self.state = self.BACKWALK_R
                elif self.rand_val == 2:                                self.state = self.BACKSTEP_R
                elif self.rand_val == 3:                                self.state = self.SREG_R
                elif self.rand_val == 4:                                self.state = self.RKICK_R
                elif self.rand_val == 5 and self.summon_count != 0:    self.state = self.CCOM_R
                elif self.rand_val == 6:                                self.state = self.DOWN_R
                elif self.rand_val == 7:                                self.state = self.GSTAND_R
                elif self.rand_val == 8 and self.state == self.DOWN_L: self.state = self.GDOWN_R
            elif player.x > (self.x - 200):
                if self.rand_val == 0:
                    self.rand_val = random.randint(1,8)
                if   self.rand_val == 1:                                  self.state = self.BACKWALK_R
                elif self.rand_val == 2:                                self.state = self.BACKSTEP_R
                elif self.rand_val == 3:                                self.state = self.SREG_R
                elif self.rand_val == 4:                                self.state = self.RKICK_R
                elif self.rand_val == 5 and self.summon_count != 0:     self.state = self.CCOM_R
                elif self.rand_val == 6:                                self.state = self.DOWN_R
                elif self.rand_val == 7:                                self.state = self.WALK_R
                elif self.rand_val == 8:                                self.state = self.RUN_R
            elif player.x > (self.x - 300):
                if self.rand_val == 0:
                    self.rand_val = random.randint(1,8)
                if   self.rand_val == 1:                                  self.state = self.BACKWALK_R
                elif self.rand_val == 2:                                self.state = self.BACKSTEP_R
                elif self.rand_val == 3:                                self.state = self.SREG_R
                elif self.rand_val == 4:                                self.state = self.RKICK_R
                elif self.rand_val == 5 and self.summon_count != 0:     self.state = self.CCOM_R
                elif self.rand_val == 6:                                self.state = self.DOWN_R
                elif self.rand_val == 7:                                self.state = self.WALK_R
                elif self.rand_val == 8:                                self.state = self.RUN_R

    #____________________________________________________________________________

    #__Game Logic_________________________________________
    def update(self, frame_time):
        def clamp(minimum, x, maximum):
            return max(minimum, min(x,maximum))

        self.handle_speed(frame_time)
        self.frame_handle[self.state](self)

        self.x = clamp(80, self.x, 1200)
        self.y = clamp(180, self.y, 595)
    #__update End__________________________________________

    # 초기화 함수___________________________________________________________________
    def __init__(self):
        # 캐릭터 피봇 좌표
        self.x = 820
        self.y = 180
        self.dir = 1
        self.HP = 100
        self.summon_count = 3

        # 프레임 변수__________
        self.run_frame        = 0
        self.walk_frame       = 0
        self.down_frame       = 0
        self.jump_frame       = 0
        self.stand_frame      = 0
        self.total_frame      = 0
        self.g_down_frame     = 0
        self.s_fist_frame     = 0
        self.s_reg_frame      = 0
        self.round_kick_frame = 0
        self.g_stand_frame    = 0
        self.backwalk_frame   = 0
        self.backstep_frame   = 0
        self.h_stand_frame    = 0
        self.h_down_frame     = 0
        self.c_common_frame   = 0
        self.c_provoke_frame  = 0
        self.win_frame        = 0
        #______________________

        # 상태 체크______________
        self.state = self.STAND_L
        self.key_timer = 0
        self.default_yPos = 180
        self.jumping_Left_move = False
        self.jumping_Right_move = False
        self.rand_val = 0
        #________________________

        # 이미지 파일______________________________________________
        # 왼쪽 파일
        self.image_stand_L          = load_image('Chie_Stand_L.png')
        self.image_walk_L           = load_image('Chie_Walk_L.png')
        self.image_backwalk_L       = load_image('Chie_Backwalk_L.png')
        self.image_run_L            = load_image('Chie_Run_L.png')
        self.image_down_L           = load_image('Chie_Down_L.png')
        self.image_jump_L           = load_image('Chie_Jump_L.png')
        self.image_backstep_L       = load_image('Chie_Backstep_L.png')
        self.image_s_fist_L         = load_image('Chie_Simple_Fist_L.png')
        self.image_simple_reg_L     = load_image('Chie_Simple_Reg_L.png')
        self.image_round_kick_L     = load_image('Chie_Round_kick_L.png')
        self.image_gard_stand_L     = load_image('Chie_Gard_Stand_L.png')
        self.image_gard_down_L      = load_image('Chie_Gard_Down_L.png')
        self.image_hit_stand_L      = load_image('Chie_Hit_Stand_L.png')
        self.image_hit_down_L       = load_image('Chie_Hit_Down_L.png')
        self.image_call_common_L    = load_image('Chie_Call_Common_L.png')
        self.image_call_provoke_L   = load_image('Chie_Call_Provoke_L.png')
        self.image_win_L            = load_image('Chie_Wins_L.png')

        # 오른쪽 파일
        self.image_stand_R          = load_image('Chie_Stand_R.png')
        self.image_walk_R           = load_image('Chie_Walk_R.png')
        self.image_backwalk_R       = load_image('Chie_Backwalk_R.png')
        self.image_run_R            = load_image('Chie_Run_R.png')
        self.image_down_R           = load_image('Chie_Down_R.png')
        self.image_jump_R           = load_image('Chie_Jump_R.png')
        self.image_backstep_R       = load_image('Chie_Backstep_R.png')
        self.image_s_fist_R         = load_image('Chie_Simple_Fist_R.png')
        self.image_simple_reg_R     = load_image('Chie_Simple_Reg_R.png')
        self.image_round_kick_R     = load_image('Chie_Round_kick_R.png')
        self.image_gard_stand_R     = load_image('Chie_Gard_Stand_R.png')
        self.image_gard_down_R      = load_image('Chie_Gard_Down_R.png')
        self.image_hit_stand_R      = load_image('Chie_Hit_Stand_R.png')
        self.image_hit_down_R       = load_image('Chie_Hit_Down_R.png')
        self.image_call_common_R    = load_image('Chie_Call_Common_R.png')
        self.image_call_provoke_R   = load_image('Chie_Call_Provoke_R.png')
        self.image_win_R            = load_image('Chie_Wins_R.png')
    #___init End___________________________________________________________________________________

    # 랜더링_______________________________________
    def draw(self):
        self.image_handle[self.state](self)
        self.draw_bb()
        #self.draw_ai_box()
    #draw End______________________________________

    # 충돌 범위_____________________________________________________________________________________________________________________________________________________
    def get_bb(self):
        if self.state == self.STAND_L:
            return self.x, self.y - (self.image_stand_L.h / 2), self.x + (self.image_stand_L.w / 5) / 4, self.y + (self.image_stand_L.h/2)
        elif self.state == self.WALK_L:
            return self.x, self.y - (self.image_walk_L.h / 2), self.x + (self.image_walk_L.w / 5) /4, self.y + (self.image_walk_L.h / 2)
        elif self.state == self.RUN_L:
            return self.x, self.y - (self.image_run_L.h / 2), self.x + (self.image_run_L.w / 5) / 4, self.y + (self.image_run_L.h / 2)
        elif self.state == self.JUMP_L:
            return self.x, self.y - (self.image_jump_L.h / 2), self.x + (self.image_jump_L.w / 5) / 4, self.y + (self.image_jump_L.h / 2)
        elif self.state == self.FALL:
            return self.x - (self.image_jump_L.w / 5) / 4, self.y - (self.image_jump_L.h / 2), self.x + (self.image_jump_L.w / 5) / 4, self.y + (self.image_jump_L.h / 2)
        elif self.state == self.DOWN_L:
            return self.x, self.y - (self.image_down_L.h / 2), self.x + (self.image_down_L.w / 5) / 4, self.y + (self.image_down_L.h / 2)
        elif self.state == self.BACKWALK_L:
            return self.x, self.y - (self.image_backwalk_L.h / 2), self.x + (self.image_backwalk_L.w / 5) / 4, self.y + (self.image_backwalk_L.h / 2)
        elif self.state == self.BACKSTEP_L:
            return self.x, self.y - (self.image_backstep_L.h / 2), self.x + (self.image_backstep_L.w / 5) / 4, self.y + (self.image_backstep_L.h / 2)
        elif self.state == self.SREG_L:
            return self.x, self.y - (self.image_simple_reg_L.h / 2), self.x + (self.image_simple_reg_L.w / 5) / 4, self.y + (self.image_simple_reg_L.h / 2)
        elif self.state == self.RKICK_L:
            return self.x, self.y - (self.image_round_kick_L.h / 2), self.x + (self.image_round_kick_L.w / 5) / 4, self.y + (self.image_round_kick_L.h / 2)
        elif self.state == self.SFIST_L:
            return self.x, self.y - (self.image_s_fist_L.h / 2), self.x + (self.image_s_fist_L.w / 5) / 4, self.y + (self.image_s_fist_L.h / 2)
        elif self.state == self.GSTAND_L:
            return self.x, self.y - (self.image_gard_stand_L.h / 2), self.x + (self.image_gard_stand_L.w / 5) / 4, self.y + (self.image_gard_stand_L.h / 2)
        elif self.state == self.GDOWN_L:
            return self.x, self.y - (self.image_gard_down_L.h / 2), self.x + (self.image_gard_down_L.w / 5) / 4, self.y + (self.image_gard_down_L.h / 2)
        elif self.state == self.HSTAND_L:
            return self.x, self.y - (self.image_hit_stand_L.h / 2), self.x + (self.image_hit_stand_L.w / 5) / 4, self.y + (self.image_hit_stand_L.h / 2)
        elif self.state == self.HDOWN_L:
            return self.x, self.y - (self.image_hit_down_L.h / 2), self.x + (self.image_hit_down_L.w / 5) / 4, self.y + (self.image_hit_down_L.h / 2)
        elif self.state == self.CCOM_L:
            return self.x, self.y - (self.image_call_common_L.h / 2), self.x + (self.image_call_common_L.w / 5) / 4, self.y + (self.image_call_common_L.h / 2)
        elif self.state == self.CPRO_L:
            return self.x, self.y - (self.image_call_provoke_L.h / 2), self.x + (self.image_call_provoke_L.w / 5) / 4, self.y + (self.image_call_provoke_L.h / 2)
        elif self.state == self.WIN_L:
            return self.x, self.y - (self.image_win_L.h / 2), self.x + (self.image_win_L.w / 5) / 4, self.y + (self.image_win_L.h / 2)
        elif self.state == self.STAND_R:
            return self.x - (self.image_stand_R.w / 5) / 4, self.y - (self.image_stand_R.h/2), self.x, self.y + (self.image_stand_R.h / 2)
        elif self.state == self.WALK_R:
            return self.x - (self.image_walk_R.w / 5) /4, self.y - (self.image_walk_R.h / 2), self.x , self.y + (self.image_walk_R.h / 2)
        elif self.state == self.RUN_R:
            return self.x - (self.image_run_R.w / 5) / 4, self.y - (self.image_run_R.h / 2), self.x , self.y + (self.image_run_R.h / 2)
        elif self.state == self.JUMP_R:
            return self.x - (self.image_jump_R.w / 5) / 4, self.y - (self.image_jump_R.h / 2), self.x, self.y + (self.image_jump_R.h / 2)
        elif self.state == self.DOWN_R:
            return self.x - (self.image_down_R.w / 5) / 4, self.y - (self.image_down_R.h / 2), self.x, self.y + (self.image_down_R.h / 2)
        elif self.state == self.BACKWALK_R:
            return self.x - (self.image_backwalk_R.w / 5) / 4, self.y - (self.image_backwalk_R.h / 2), self.x , self.y + (self.image_backwalk_R.h / 2)
        elif self.state == self.BACKSTEP_R:
            return self.x - (self.image_backstep_R.w / 5) / 4, self.y - (self.image_backstep_R.h / 2), self.x , self.y + (self.image_backstep_R.h / 2)
        elif self.state == self.SREG_R:
            return self.x - (self.image_simple_reg_R.w / 5) / 4, self.y - (self.image_simple_reg_R.h / 2), self.x , self.y + (self.image_simple_reg_R.h / 2)
        elif self.state == self.RKICK_R:
            return self.x - (self.image_round_kick_R.w / 5) / 4, self.y - (self.image_round_kick_R.h / 2), self.x, self.y + (self.image_round_kick_R.h / 2)
        elif self.state == self.SFIST_R:
            return self.x - (self.image_s_fist_R.w / 5) / 4, self.y - (self.image_s_fist_R.h / 2), self.x, self.y + (self.image_s_fist_R.h / 2)
        elif self.state == self.GSTAND_R:
            return self.x - (self.image_gard_stand_R.w / 5) / 4, self.y - (self.image_gard_stand_R.h / 2), self.x, self.y + (self.image_gard_stand_R.h / 2)
        elif self.state == self.GDOWN_R:
            return self.x - (self.image_gard_down_R.w / 5) / 4, self.y - (self.image_gard_down_R.h / 2), self.x, self.y + (self.image_gard_down_R.h / 2)
        elif self.state == self.HSTAND_R:
            return self.x - (self.image_hit_stand_R.w / 5) / 4, self.y - (self.image_hit_stand_R.h / 2), self.x , self.y + (self.image_hit_stand_R.h / 2)
        elif self.state == self.HDOWN_R:
            return self.x - (self.image_hit_down_R.w / 5) / 4, self.y - (self.image_hit_down_R.h / 2), self.x, self.y + (self.image_hit_down_R.h / 2)
        elif self.state == self.CCOM_R:
            return self.x - (self.image_call_common_R.w / 5) / 4, self.y - (self.image_call_common_R.h / 2), self.x , self.y + (self.image_call_common_R.h / 2)
        elif self.state == self.CPRO_R:
            return self.x - (self.image_call_provoke_R.w / 5) / 4, self.y - (self.image_call_provoke_R.h / 2), self.x, self.y + (self.image_call_provoke_R.h / 2)
        elif self.state == self.WIN_R:
            return self.x - (self.image_win_R.w / 5) / 4, self.y - (self.image_win_R.h / 2), self.x , self.y + (self.image_win_R.h / 2)
    # __get_bb End_______________________________________________________________________________________________________________________________________________________

    # 충돌 박스 그리기_________________
    def draw_bb(self):
        draw_rectangle(*self.get_bb())
    #___draw_bb_________________________

    def draw_ai_box(self):
        if self.dir == 1:
            draw_rectangle(self.x, self.y - 90, self.x + 300, self.y)
        elif self.dir == -1:
            draw_rectangle(self.x - 300, self.y - 90, self.x, self.y)