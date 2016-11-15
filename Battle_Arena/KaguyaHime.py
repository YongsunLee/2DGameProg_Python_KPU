import os

os.chdir('D:/Job/2 - 2/2DGP/Project_Battle Arena/SunE_Repository/Battle_Arena/Asset')

from pico2d import *

class Kaguya:
    ATTACK01, ATTACK02, ATTACK03, ATTACK04, ATTACK05, ATTACK06 = 1,2,3,4,5,6
    J_ATTACK01, J_ATTACK02 = 7, 8

    #속도
    PIXEL_PER_METER = (250.0 / 1.6)  # 250 pixel 160cm // 1 pixel 1.6cm
    # 걷기
    WALK_SPEED_KMPH = 10.0          # Km / Hour
    WALK_SPEED_PPS = (((WALK_SPEED_KMPH * 1000.0 / 60.0) / 60.0) * PIXEL_PER_METER)

    # 액션 프레임 조절
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 3

    # 프레임 변화 핸들
    # 키업에서 상태 변화가 아닌
    # 여기서 상태 변화를 넣는것 프레임이 끝날때 상태를 변경.
    def handle_frame_attack01(self):
        #self.attack01_frame = (self.attack01_frame + 1) % 9
        self.attack01_frame = int(self.total_frame) % 9
        if self.attack01_frame == 8:
            self.down_check = False
            self.attack01_frame = 0
        pass

    def handle_frame_attack02(self):

        pass

    # 이미지 출력 핸들
    def handle_image_attack01(self):
        if self.dir == 1:
            if self.attack01_frame < 5:
                self.attack01_L.clip_draw(self.attack01_frame * 550, 0, 550, 330, self.x, self.y)
            else:
                self.attack01_L.clip_draw((9-self.attack01_frame) * 550, 0, 550, 330, self.x, self.y)
        else: self.attack01_R.clip_draw(self.attack01_frame* 550, 0, 550, 330, self.x, self.y)
        pass

    def handle_image_attack02(self):
        pass

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_d):
            self.down_check = True
            self.state_ = self.ATTACK01
        pass

    # 프레임 갱신 핸들
    handle_frame = {
        ATTACK01: handle_frame_attack01,
        ATTACK02: handle_frame_attack02
    }

    # 이미지 출력 핸들
    image_handle = {
        ATTACK01: handle_image_attack01,
        ATTACK02: handle_image_attack02
    }

    # 속도 계산 핸들
    def handle_speed(self, frame_time):
        pass

    # 업데이트
    def update(self, frame_time):
        self.handle_speed(frame_time)
        self.handle_frame[self.state_](self)

    def handle_speed(self, frame_time):
        self.total_frame += self.FRAMES_PER_ACTION * self.ACTION_PER_TIME * frame_time
        pass

    # 초기화
    def __init__(self):
        # 캐릭터 피봇 좌표
        self.x = 320
        self.y = 280
        self.dir = 1

        # 프레임
        self.total_frame = 0

        # 프레임 변수
        self.attack01_frame = 0
        self.attack02_frame = 0


        # 상태 체크
        self.state_ = self.ATTACK01
        self.down_check = False

        # 이미지 파일
            # 왼쪽 파일
        self.attack01_L = load_image('Kaguya_attack_01_L.png')
            # 오른쪽 파일
        self.attack01_R = load_image('Kaguya_attack_01_R.png')

    def draw(self):
        if self.down_check:
            self.image_handle[self.state_](self)
            self.draw_bb()

    def get_bb(self):
        if (self.state_ == self.ATTACK01):
            if self.dir == 1:
                return self.x, self.y - (self.attack01_L.h / 2), self.x + (self.attack01_L.w / 5) / 2, self.y + (self.attack01_L.h / 2)
            else:
                return self.x - (self.attack01_L.w / 5) / 2, self.y - (self.attack01_L.h / 2), self.x, self.y + (self.attack01_L.h / 2)
        pass

    def draw_bb(self):
        draw_rectangle(*self.get_bb())