from pico2d import *
import random

# 화면 가로,세로
pad_w = 900
pad_h = 600

# Game object class here
def handle_events():
    global running,x,y,miko
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                miko.righton = True
            elif event.key == SDLK_LEFT:
                miko.lefton = True
            elif event.key == SDLK_UP:
                miko.upon = True
            elif event.key == SDLK_DOWN:
                miko.downon = True
            elif event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_a:
                miko.state = True

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

class Back1:
    def __init__(self):
        self.image = load_image('back.png')
        self.back1_x = 450

    def update(self):
        self.back1_x -= 10
        if self.back1_x == -450:
            self.back1_x = 1350

    def draw(self):
        self.image.draw(self.back1_x,300)

class Back2:
    def __init__(self):
        self.image = load_image('back2.png')
        self.back2_x = 1350

    def update(self):
        self.back2_x -= 10
        if self.back2_x <= -450:
            self.back2_x = 1350

    def draw(self):
        self.image.draw(self.back2_x,300)

class Miko:
    def __init__(self):
        self.x = 50
        self.y = 300
        self. frame = 0
        self.righton = False
        self.lefton = False
        self.upon = False
        self.downon = False
        self.state = False
        self.image = load_image('miko.png')
        self.ani = load_image('mikoattack.png')

    def update(self):
        self. frame = self.frame + 5
        if self.righton == True and self.x <860:
            self.x = self.x + 10
        if self.lefton == True and self.x > 40:
            self.x = self.x - 10
        if self.upon == True and self.y < 560:
            self.y = self.y + 10
        if self.downon == True and self.y > 30:
            self.y = self.y - 10

    def draw(self):
        if self.state == True:
            self.ani.clip_draw((self.frame%4) * 105, 0 , 70, 70, self.x, self.y)
        if self.state == False:
            self.image.draw(self.x,self.y)

class Enemy1:
    def __init__(self):
        self.image = load_image('enemy1.png')
        self.frame = 0
        self.x = 1000
        self.y = random.randint(200,550)

    def update(self):
        self.frame = self.frame + 5
        self.x -= 5

    def draw(self):
        self.image.clip_draw((self.frame%3) * 69,0,74,95,self.x,self.y)

# initialization code
open_canvas(pad_w,pad_h)

back1 = Back1()
back2 = Back2()
miko = Miko()
enemy1 = Enemy1()

running = True
# game main loop code
while running:

    handle_events()

    clear_canvas()

    back1.draw()
    back2.draw()
    back1.update()
    back2.update()
    miko.draw()
    miko.update()
    enemy1.draw()
    enemy1.update()

    update_canvas()

    delay(0.05)

# finalization code
close_canvas()