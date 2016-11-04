import os

os.chdir('D:/Job/2 - 2/2DGP/Project_Battle Arena/SunE_Repository/Battle_Arena/Asset')

from pico2d import *

class Marie:
    STAND_L, WALK_L, BACKWALK_L, RUN_L, DOWN_L, WIN_L, JUMP_L, BACKSTEP_L = 0, 1, 2, 3, 4, 5, 6, 7
    ATTACK00_L, ATTACK01_L, CALL00_L, CALL01_L, ATTACK02_L = 8, 9, 10, 11, 12

    # 프레임 출력함수
    # 키업에서 상태 변화가 아닌
    # 여기서 상태 변화를 넣는것 프레임이 끝날때 상태를 변경.
    def handle_frame_stand(self):
        self.stand_frame = (self.stand_frame + 1) % 10
    def handle_frame_walk(self):
        if self.walk_frame == 7:
            self.walk_frame = (self.walk_frame + 1) % 8
            self.walk_frame = 2
        else:
            self.walk_frame = (self.walk_frame + 1) % 8
        self.x += (self.dir * 18)
        self.run_timer = (self.run_timer + 0.8)
        if self.run_timer >= 2.0:
            self.run_timer = 0.0
    def handle_frame_backwalk(self):
        if self.walk_frame == 11:
            self.backwalk_frame = (self.backwalk_frame + 1) % 12
            self.backwalk_frame = 2
        else:
            self.backwalk_frame = (self.backwalk_frame + 1) % 12
        self.x -= (self.dir * 10)
        self.backstep_timer = (self.backstep_timer + 0.8)
        if self.backstep_timer >= 3.0:
            self.backstep_timer = 0.0
    def handle_frame_run(self):
        self.run_frame = (self.run_frame + 1) % self.run_count
        if self.run_count == 11:
            self.run_count = 9
        self.x += (self.dir * 30)
        if self.run_timer >= 1.0:
            self.run_timer = 0.0
    def handle_frame_jump(self):
        if self.jump_count == 1:
            self.jump_frame = (self.jump_frame - 1)
            self.y -= 20
            if self.R_keydown_jump:
                self.x += self.dir * 15
            elif self.L_keydown_jump:
                self.x -= self.dir * 15
            if self.jump_frame == 0:
                self.jump_count = 0
                if self.R_keydown_jump:
                    self.frame_ = self.WALK_L
                elif self.L_keydown_jump:
                    self.frame_ = self.BACKWALK_L
                else:
                    self.frame_ = self.STAND_L
        else:
            self.jump_frame = (self.jump_frame + 1)
            self.y += 20
            if self.R_keydown_jump:
                self.x += self.dir * 15
            elif self.L_keydown_jump:
                self.x -= self.dir * 15
            if self.jump_frame == 8:
                self.jump_count = 1
    def handle_frame_down(self):
        if self.down_frame == 9:
            self.down_frame = (self.down_frame + 1) % 10
            self.down_frame = 3
        else:
            self.down_frame = (self.down_frame + 1) % 10
    def handle_frame_win(self):
        self.win_frame = (self.win_frame + 1)
        if self.attack00_frame == 7:
            self.frame_ = self.STAND_L
            self.attack00_frame = 0
    def handle_frame_attack00(self):
        self.attack00_frame = (self.attack00_frame + 1)
        if self.attack00_frame == 7:
            self.frame_ = self.STAND_L
            self.attack00_frame = 0
    def handle_frame_attack01(self):
        self.attack01_frame = self.attack01_frame + 1
        self.attack01_tiemr = (self.attack01_tiemr + 0.8)
        if self.attack01_tiemr >= 3.0:
            self.attack01_tiemr = 0.0
        if self.attack01_frame == 10:
            self.frame_ = self.STAND_L
            self.attack01_frame = 0
    def handle_frame_attack02(self):
        self.attack02_frame = self.attack02_frame + 1
        if self.attack01_tiemr >= 1.0:
            self.attack01_tiemr = 0.0
        if self.attack02_frame == 11:
            self.frame_ = self.STAND_L
            self.attack02_frame = 0
    def handle_frame_call00(self):
        self.call00_frame = (self.call00_frame + 1)
        self.call_timer = (self.call_timer + 0.8)
        if self.call_timer >= 3.0:
            self.call_timer = 0.0
        if self.call00_frame == 6:
            self.frame_ = self.STAND_L
            self.call00_frame = 0
    def handle_frame_call01(self):
        self.call01_frame = (self.call01_frame + 1)
        if self.call_timer >= 1.0:
            self.call_timer = 0.0
        if self.call01_frame == 6:
            self.frame_ = self.STAND_L
            self.call01_frame = 0
    def handle_frame_backstep(self):
        self.backstep_frame = (self.backstep_frame + 1)
        self.x -= (self.dir * 20)
        if self.backstep_timer >= 0.8:
            self.backstep_timer = 0.0
        if self.backstep_frame == 5:
            self.frame_ = self.STAND_L
            self.backstep_frame = 0

    # 이미지 출력 함수
    def handle_image_stand(self):
        self.stand_L.clip_draw(self.stand_frame * 121, 0, 121, 250, self.x, self.y)
    def handle_image_walk(self):
        self.walk_L.clip_draw(self.walk_frame * 121, 0, 121, 250, self.x, self.y)
    def handle_image_backwalk(self):
        self.backwalk_L.clip_draw(self.backwalk_frame * 121, 0, 121, 250, self.x, self.y)
    def handle_image_run(self):
        self.run_L.clip_draw(self.run_frame * 190, 0, 190, 250, self.x, self.y)
    def handle_image_down(self):
        self.down_L.clip_draw(self.down_frame * 121, 0, 121, 250, self.x, self.y)
    def handle_image_jump(self):
        self.jump_L.clip_draw(self.jump_frame * 121, 0, 121, 250, self.x, self.y)
    def handle_image_win(self):
        self.win_L.clip_draw(self.win_frame * 121, 0, 121, 250, self.x, self.y)
    def handle_iamge_attack00(self):
        self.attack00_L.clip_draw(self.attack00_frame * 210, 0, 210, 250, self.x, self.y)
    def handle_image_attack01(self):
        self.attack01_L.clip_draw(self.attack01_frame * 600, 0, 600, 320, self.x, self.y)
    def handle_image_attack02(self):
        self.attack02_L.clip_draw(self.attack02_frame * 700, 0, 700, 600, self.x, self.y)
    def handle_image_call00(self):
        self.call00_L.clip_draw(self.call00_frame * 170, 0, 170, 280, self.x, self.y)
    def handle_image_call01(self):
        self.call01_L.clip_draw(self.call01_frame * 180, 0, 180, 280, self.x, self.y)
    def handle_image_backstep(self):
        self.backstep_L.clip_draw(self.backstep_frame * 140, 0, 140, 250, self.x, self.y)

    def handle_event(self, event):
        # KeyDown
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            if self.y == self.default_y:
                if self.backstep_timer >= 1.0:
                    self.frame_ = self.BACKSTEP_L
                else:
                    self.frame_ = self.BACKWALK_L
                self.L_keydown_jump = True
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            if self.y == self.default_y:
                if self.run_timer >= 1.0:
                    self.frame_ = self.RUN_L
                else:
                    self.frame_ = self.WALK_L
                self.R_keydown_jump = True
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
            if self.frame_ in (self.STAND_L, self.RUN_L, self.WALK_L, self.BACKWALK_L):
                self.frame_ = self.JUMP_L
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
                self.frame_ = self.DOWN_L
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_a):
            if self.y == self.default_y:
                if self.attack01_tiemr >= 1.0:
                    self.frame_ = self.ATTACK02_L
                else:
                    self.frame_ = self.ATTACK01_L
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_s):
            if self.y == self.default_y:
                self.frame_ = self.ATTACK00_L
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_d):
            if self.y == self.default_y:
                if self.call_timer >= 1.0:
                    self.frame_ = self.CALL01_L
                else:
                    self.frame_ = self.CALL00_L

        # Key UP
        if (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            if self.frame_ in (self.BACKWALK_L, self.BACKSTEP_L):
                self.frame_ = self.STAND_L
                self.backstep_frame = 0
                self.backwalk_frame = 0
            self.L_keydown_jump = False
        if (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            if self.frame_ in (self.WALK_L, self.RUN_L):
                self.frame_ = self.STAND_L
                self.walk_frame = 0
                self.run_frame = 0
            self.R_keydown_jump = False
        if (event.type, event.key) == (SDL_KEYUP, SDLK_DOWN):
            self.frame_ = self.STAND_L
            self.down_frame = 0

    # 프레임 갱신 핸들
    handle_frame = {
        STAND_L: handle_frame_stand,
        WALK_L: handle_frame_walk,
        BACKWALK_L: handle_frame_backwalk,
        RUN_L: handle_frame_run,
        DOWN_L: handle_frame_down,
        WIN_L: handle_frame_win,
        JUMP_L: handle_frame_jump,
        BACKSTEP_L: handle_frame_backstep,
        CALL00_L: handle_frame_call00,
        CALL01_L: handle_frame_call01,
        ATTACK00_L: handle_frame_attack00,
        ATTACK01_L: handle_frame_attack01,
        ATTACK02_L: handle_frame_attack02
     }

    # 이미지 출력 핸들
    image_handle = {
        STAND_L: handle_image_stand,
        WALK_L: handle_image_walk,
        BACKWALK_L: handle_image_backwalk,
        RUN_L: handle_image_run,
        DOWN_L: handle_image_down,
        WIN_L: handle_image_win,
        JUMP_L: handle_image_jump,
        BACKSTEP_L: handle_image_backstep,
        CALL00_L: handle_image_call00,
        CALL01_L: handle_image_call01,
        ATTACK00_L: handle_iamge_attack00,
        ATTACK01_L: handle_image_attack01,
        ATTACK02_L: handle_image_attack02
    }

    def update(self):
        self.handle_frame[self.frame_](self)

    def __init__(self):
        # 캐릭터 피봇 좌표
        self.x = 320
        self.y = 180
        self.dir = 1

        # 프레임 변수
        self.stand_frame = 0
        self.walk_frame = 0
        self.backwalk_frame = 0
        self.run_frame = 0
        self.jump_frame = 0
        self.down_frame = 0
        self.win_frame = 0
        self.backstep_frame = 0
        self.call00_frame = 0
        self.call01_frame = 0
        self.attack00_frame = 0
        self.attack01_frame = 0
        self.attack02_frame = 0
        self.attack02_yframe = 0

        # 상태 체크
        self.frame_ = self.STAND_L
        self.jump_count = 0
        self.default_y = 180
        self.run_count = 11

        # 키 눌린거 확인
        self.L_keydown_jump  = False
        self.R_keydown_jump = False

        # 더블 입력 함수
        self.attack01_tiemr = 0.0
        self.run_timer = 0.0
        self.call_timer = 0.0
        self.backstep_timer = 0.0

        # 이미지 파일
            # 왼쪽 파일
        self.stand_L = load_image('Marie_Stand_L.png')
        self.walk_L = load_image('Marie_Walking_L.png')
        self.backwalk_L = load_image('Marie_BackWalking_L.png')
        self.run_L = load_image('Marie_Run_L.png')
        self.backstep_L = load_image('Marie_BackStep_L.png')
        self.jump_L = load_image('Marie_Jump_L.png')
        self.down_L = load_image('Marie_Down_L.png')
        self.win_L = load_image('Marie_Wins_L.png')

                # 공격
        self.attack00_L = load_image('Marie_Attack00_L.png')
        self.attack01_L = load_image('Marie_Attack01_L.png')
        self.attack02_L = load_image('Marie_Attack02_L.png')
        self.call00_L = load_image('Marie_Call00_L.png')
        self.call01_L = load_image('Marie_Call01_L.png')

            # 오른쪽 파일
        #self.stand_R = load_image('Marie_Stand_R.png')
        #self.walk_R = load_image('Marie_Walking_R.png')
        #self.backwalk_R = load_image('Marie_BackWalking_R.png')
        #self.run_R = load_image('Marie_Run_R.png')
        #self.backstep_R = load_image('Marie_BackStep_R.png')
        #self.jump_R = load_image('Marie_Jump_R.png')
        #self.down_R = load_image('Marie_Down_R.png')
        #self.win_R = load_image('Marie_Wins_R.png')

                #공격
        #self.attack00_R = load_image('Marie_Attack00_R.png')
        #self.attack01_R = load_image('Marie_Attack01_R.png')
        #self.attack02_R = load_image('Marie_Attack02_R.png')
        #self.call00_R = load_image('Marie_Call00_R.png')
        #self.call01_R = load_image('Marie_Call01_R.png')


    def draw(self):
            self.image_handle[self.frame_](self)
