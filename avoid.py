from pico2d import *
from time import sleep
import random


import game_framework
import title_state

name = "MainState"

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
        self.diecount = 0
        self.weap = [Weapone() for i in range(20)]
        self.frame = 0    # 미코 프레임
        self.framea = 0   # 무기 프레임
        self.righton = False
        self.lefton = False
        self.upon = False
        self.downon = False
        self.state = False  # 캐릭터 a입력시 이미지 변경
        self.attstate = False
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
            elif event.key == SDLK_a and miko.attstate == False:
                miko.state = True
                miko.attstate = True
                miko.weap[miko.count].state = True
                miko.weap[miko.count].xx = miko.x + 30
                miko.weap[miko.count].yy = miko.y
                miko.count += 1
                if (miko.count >= 20):
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
        self.framea += 3
        if self.righton == True and self.x <860:
            self.x += 10
        if self.lefton == True and self.x > 40:
            self.x -= 10
        if self.upon == True and self.y < 560:
            self.y += 10
        if self.downon == True and self.y > 30:
            self.y -= 10
        for i in range(20):
            if self.attstate == True:
                if self.weap[i].state == True:
                    self.weap[i].xx += 15

    def draw(self):
        if self.state == True:
            self.ani.clip_draw((self.frame%4) * 105, 0 , 80, 70, self.x, self.y)
        if self.state == False:
            self.image.draw(self.x,self.y)
        for i in range(20):
            if self.weap[i].state == True:
                self.weapone1.clip_draw((self.framea % 5) * 35, 0, 25, 40, self.weap[i].xx, self.weap[i].yy)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x-40,self.y-20,self.x+30,self.y+30

    def draw_aa(self,i):
        draw_rectangle(*self.get_aa(i))

    def get_aa(self,i):
        return self.weap[i].xx-10,self.weap[i].yy-10,self.weap[i].xx-10,self.weap[i].yy+12

class Enemy1:
    def __init__(self):
        self.image = load_image('enemy1.png')
        self.frame = 0
        self.x, self.y = random.randint(920, 1700), random.randint(60, 570)

    def update(self):
        self.frame += 5
        self.x -= 10
        if self.x <=0:
            self.x = random.randint(900,1500)
            self.y = random.randint(80,570)

    def draw(self):
        self.image.clip_draw((self.frame % 4) * 60, 0, 60, 50, self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 28, self.y - 23, self.x + 18, self.y + 23

class Enemy2:
    def __init__(self):
        self.image = load_image('enemy2.png')
        self.frame = 0
        self.x, self.y = random.randint(1700, 2500), random.randint(60, 570)

    def update(self):
        self.frame += 1
        self.x -= 12
        if self.x <=0:
            self.x = random.randint(900,1500)
            self.y = random.randint(80,570)

    def draw(self):
        self.image.clip_draw((self.frame % 3) * 69, 0, 74, 100, self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 30, self.y - 40, self.x + 30, self.y + 47

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            #game_framework.quit()
            game_framework.change_state(title_state)
        else:
            miko.handle_event(event)

def enter():
    global back1, back2, miko, enemy1, enemy2, team, team2, font
    back1 = Back1()
    back2 = Back2()
    miko = Miko()
    enemy1 = Enemy1()
    enemy2 = Enemy2()
    team = [Enemy1() for i in range(11)]
    team2 = [Enemy2() for i in range(16)]
    font = load_font('ENCR10B.TTF', 115)

def exit():
    global back1, back2, enemy1, enemy2
    del(back1)
    del(back2)
    del(enemy1)
    del(enemy2)

def collide1(a, b):
    left_a, bottom_a,right_a,top_a = a.get_bb()
    left_b, bottom_b,right_b,top_b = b.get_bb()

    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False

    return True

def collide2(a, b, i):
    left_a, bottom_a,right_a,top_a = a.get_aa(i)
    left_b, bottom_b,right_b,top_b = b.get_bb()

    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False

    return True

def update():
    back1.update()
    back2.update()
    miko.update()
    for enemy1 in team:
        enemy1.update()
    for enemy2 in team2:
        enemy2.update()
    for i in range(20):
        for enemy1 in team:
            if collide2(miko, enemy1,i):
                miko.attstate = False
                team.remove(enemy1)
                miko.weap[i].yy = 1000
    for i in range(20):
        for enemy2 in team2:
            if collide2(miko, enemy2,i):
                miko.attstate = False
                team2.remove(enemy2)
                miko.weap[i].yy = 1000

def draw():
    hide_cursor()
    clear_canvas()
    back1.draw()
    back2.draw()
    miko.draw()
    #for i in range(20):
    #    miko.draw_aa(i)
    #miko.draw_bb()
    #for enemy1 in team:
    #    enemy1.draw_bb()
    #for enemy2 in team2:
    #    enemy2.draw_bb()
    for enemy1 in team:
        enemy1.draw()
    for enemy2 in team2:
        enemy2.draw()

    for enemy1 in team:
        if collide1(miko, enemy1):
            font.draw(230, 300, 'WARNING!', (255, 0, 0))
            sleep(0.02)
            miko.diecount += 1
            if (miko.diecount >= 5):
                game_framework.change_state(title_state)

    for enemy2 in team2:
        if collide1(miko, enemy2):
            font.draw(230, 300, 'WARNING!', (255, 0, 0))
            sleep(0.01)
            miko.diecount += 1
            if (miko.diecount >= 3):
                game_framework.change_state(title_state)

    update_canvas()
    delay(0.02)