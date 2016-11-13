from pico2d import *
import random

import game_framework

name = "MainState"

enemy1_width = 74
enemy1_height = 100

class Back1:
    def __init__(self):
        self.image = load_image('back.png')
        self.back1_x = 450      #first 배경 x좌표위치

    def update(self):
        self.back1_x -= 10
        if self.back1_x <= -450:
            self.back1_x = 1350

    def draw(self):
        self.image.draw(self.back1_x,300)

class Back2:
    def __init__(self):
        self.image = load_image('back2.png')
        self.back2_x = 1350     #Second 배경 x좌표위치

    def update(self):
        self.back2_x -= 10
        if self.back2_x <= -450:
            self.back2_x = 1350

    def draw(self):
        self.image.draw(self.back2_x,300)

class Weapone:
    def __init__(self):
        self.xx = 0
        self.yy = 0
        self.state = False

class Miko:
    def __init__(self):
        self.x = 50
        self.y = 300
        self.count = 0
        self.weap = [Weapone() for i in range(50)]
        self.frame = 0    # 미코 프레임
        self.framea = 0   # 무기 프레임
        self.righton = False
        self.lefton = False
        self.upon = False
        self.downon = False
        self.state = False  # 캐릭터 a입력시 이미지 변경
        self.image = load_image('miko.png')
        self.ani = load_image('mikoattack.png')
        self.weapone1 = load_image('weapone1.png')

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                miko.righton = True
            elif event.key == SDLK_LEFT:
                miko.lefton = True
            elif event.key == SDLK_UP:
                miko.upon = True
            elif event.key == SDLK_DOWN:
                miko.downon = True
            elif event.key == SDLK_a:
                miko.state = True
                miko.weap[miko.count].state = True
                miko.weap[miko.count].xx = miko.x + 30
                miko.weap[miko.count].yy = miko.y
                miko.count += 1
                if (miko.count >= 50):
                    miko.count = 0
        if event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                miko.righton = False
            elif event.key == SDLK_LEFT:
                miko.lefton = False
            elif event.key == SDLK_UP:
                miko.upon = False
            elif event.key == SDLK_DOWN:
                miko.downon = False
            elif event.key == SDLK_a:
                miko.state = False
                miko.weap[miko.count].state = False

    def update(self):
        self.frame += 5
        self.framea += 4
        if self.righton == True and self.x <860:
            self.x += 10
        if self.lefton == True and self.x > 40:
            self.x -= 10
        if self.upon == True and self.y < 560:
            self.y += 10
        if self.downon == True and self.y > 30:
            self.y -= 10
        for i in range(50):
            if self.weap[i].state == True:
                self.weap[i].xx += 20

    def draw(self):
        if self.state == True:
            self.ani.clip_draw((self.frame%4) * 105, 0 , 80, 70, self.x, self.y)
        if self.state == False:
            self.image.draw(self.x,self.y)
        for i in range(50):
            if self.weap[i].state == True:
                self.weapone1.clip_draw((self.framea % 5) * 35, 0, 25, 40, self.weap[i].xx, self.weap[i].yy)

class Enemy1:
    def __init__(self):
        self.image = load_image('enemy1.png')
        self.frame = 0
        self.x, self.y = random.randint(1000,2000), random.randint(60,570)

    def update(self):
        self.frame += 5
        self.x -= 5
        if self.x <=0:
            self.x = random.randint(900,1500)
            self.y = random.randint(80,570)

    def draw(self):
        self.image.clip_draw((self.frame%3) * 69,0,74,100,self.x,self.y)


def handle_events():
    global running,x,y,miko
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            miko.handle_event(event)

def enter():
    global back1,back2,miko,enemy1,team
    back1 = Back1()
    back2 = Back2()
    miko = Miko()
    enemy1 = Enemy1()
    team = [Enemy1() for i in range(9)]

def exit():
    global back1, back2, miko, enemy1, team
    del(back1)
    del(back2)
    del(miko)
    del(enemy1)
    del(team)

def update():
    back1.update()
    back2.update()
    miko.update()
    for enemy1 in team:
        enemy1.update()

def draw():
    clear_canvas()
    back1.draw()
    back2.draw()
    miko.draw()
    for enemy1 in team:
        enemy1.draw()
    update_canvas()
    delay(0.02)