import os

os.chdir('D:/Job/2 - 2/2DGP/Project_Battle Arena/SunE_Repository/Battle_Arena/Chie')

from pico2d import *

class Chie:
    STAND_L, WALK_L, BACKWALK_L, RUN_L, DOWN_L, WIN_L, JUMP_L = 0, 1, 2, 3, 4, 5, 6
    ATTACK00_L, ATTACK01_L, CALL00_L, CALL01_L = 7, 8, 9, 10

    # 프레임 출력함수
    def frame_handle_stand(self):
        pass

    # 이미지 출력 함수
    def handle_image_stand(self):
        pass
    # 프레임 갱신 핸들
    frame_handle = {
     }

    # 이미지 출력 핸들
    image_handle = {
    }

    def update(self):
        self.frame_handle[self.state](self)

    def __init__(self):
        # 캐릭터 피봇 좌표
        self.x = 820
        self.y = 180
        self.dir = 1

        # 프레임 변수

        # 상태 체크
        self.state = self.STAND_L
        self.call_timer = 0.0

        # 이미지 파일
            # 왼쪽 파일
        self.stand_L = load_image('Stand_L.png')

                # 공격

            # 오른쪽 파일


    def draw(self):
            self.image_handle[self.state](self)
