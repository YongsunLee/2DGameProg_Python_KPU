import os

os.chdir('D:/Job/2 - 2/2DGP/Project_Battle Arena/SunE_Repository/Battle_Arena/Chie')

from pico2d import *

class Marie:
    STAND_L, WALK_L, BACKWALK_L, RUN_L, DOWN_L, WIN_L, JUMP_L = 0, 1, 2, 3, 4, 5, 6
    ATTACK00_L, ATTACK01_L, CALL00_L, CALL01_L = 7, 8, 9, 10

    # 프레임 출력함수
    def frame_handle_stand(self):
        self.stand_frame = (self.stand_frame + 1) % 10
        if self.frame_ != self.STAND_L:
            self.stand_frame = 0
    def frame_handle_walk(self):
        if self.walk_frame == 7:
            self.walk_frame = (self.walk_frame + 1) % 8
            self.walk_frame = 2
        else:
            self.walk_frame = (self.walk_frame + 1) % 8
        self.x += (self.dir * 18)
    def frame_handle_backwalk(self):
        if self.walk_frame == 11:
            self.backwalk_frame = (self.backwalk_frame + 1) % 12
            self.backwalk_frame = 2
        else:
            self.backwalk_frame = (self.backwalk_frame + 1) % 12
        self.x -= (self.dir * 10)
    def frame_handle_run(self):
        self.run_frame = (self.run_frame + 1) % 11
        self.x += (self.dir * 30)
        if self.frame_ != self.RUN_L:
            self.run_frame = 0
    def frame_handle_jump(self):
        count = 0
        if count == 1:
            self.jump_frame = (self.jump_frame - 1)
            self.y -= (self.dir * 20)
            if self.jump_frame == 0:
                count = 0
        else:
            self.jump_frame = (self.jump_frame + 1)
            self.y += (self.dir * 20)
            if self.jump_frame == 9:
                count = 1
    def frame_handle_down(self):
        if self.down_frame == 9:
            self.down_frame = (self.down_frame + 1) % 10
            self.down_frame = 3
        else:
            self.down_frame = (self.down_frame + 1) % 10
    def frame_handle_win(self):
        self.win_frame = (self.win_frame + 1)
        if self.frame_ != self.WIN_L:
            self.win_frame = 0
    def frame_handle_attack00(self):
        self.attack00_frame = (self.attack00_frame + 1) % 7
    def frame_handle_attack01(self):
        self.attack01_frame = (self.attack01_frame + 1) % 10
        if self.frame_ != self.ATTACK01_L:
            self.attack01_frame = 0
    def frame_handle_call00(self):
        if self.call00_frame == 5:
            self.call00_frame = 2
            self.call00_frame = (self.call00_frame + 1) % 6
        else:
            self.call00_frame = (self.call00_frame + 1) % 6
        self.call_timer = (self.call_timer + 0.8)
    def frame_handle_call01(self):
        if self.call01_frame == 5:
            self.call01_frame = 2
            self.call01_frame = (self.call01_frame + 1) % 6
        else:
            self.call01_frame = (self.call01_frame + 1) % 6
        if self.call_timer >= 1.0:
            self.call_timer = 0.0


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
    def handle_image_call00(self):
        self.call00_L.clip_draw(self.call00_frame * 170, 0, 170, 280, self.x, self.y)
    def handle_image_call01(self):
        self.call01_L.clip_draw(self.call01_frame * 180, 0, 180, 280, self.x, self.y)

    # 프레임 갱신 핸들
    frame_handle = {
        STAND_L: frame_handle_stand,
        WALK_L: frame_handle_walk,
        BACKWALK_L: frame_handle_backwalk,
        RUN_L: frame_handle_run,
        DOWN_L: frame_handle_down,
        WIN_L: frame_handle_win,
        JUMP_L: frame_handle_jump,
        CALL00_L: frame_handle_call00,
        CALL01_L: frame_handle_call01,
        ATTACK00_L: frame_handle_attack00,
        ATTACK01_L: frame_handle_attack01
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
        CALL00_L: handle_image_call00,
        CALL01_L: handle_image_call01,
        ATTACK00_L: handle_iamge_attack00,
        ATTACK01_L: handle_image_attack01
    }

    def update(self):
        self.frame_handle[self.frame_](self)

    def __init__(self):
        # 캐릭터 피봇 좌표
        self.x = 820
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
        self.call00_frame = 0
        self.call01_frame = 0
        self.attack00_frame = 0
        self.attack01_frame = 0

        # 상태 체크
        self.frame_ = self.STAND_L
        self.call_timer = 0.0

        # 이미지 파일
            # 왼쪽 파일
        self.stand_L = load_image('Stand_L.png')
        self.walk_L = load_image('Walking_L.png')
        self.backwalk_L = load_image('BackWalking_L.png')
        self.run_L = load_image('Run_L.png')
        self.jump_L = load_image('Jump_L.png')
        self.down_L = load_image('Down_L.png')
        self.win_L = load_image('Wins_L.png')

                # 공격
        self.attack00_L = load_image('Attack00_L.png')
        self.attack01_L = load_image('Attack01_L.png')
        self.call00_L = load_image('Call00_L.png')
        self.call01_L = load_image('Call01_L.png')


            # 오른쪽 파일


    def draw(self):
            self.image_handle[self.frame_](self)
