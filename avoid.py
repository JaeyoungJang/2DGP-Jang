from pico2d import *
from time import sleep

import random
import game_framework
import title_state
import game_over_state

name = "MainState"

class Back1:
    image = None
    def __init__(self):
        if Back1.image == None:
            Back1.image = load_image('space_back1.png')
        self.back1_x = 450      #first background, 'x' location

    def update(self,frame_time):
        self.back1_x -= 10
        if self.back1_x <= -450:
            self.back1_x = 1350

    def draw(self):
        self.image.draw(self.back1_x,300)

class Back2:
    image = None
    def __init__(self):
        if Back2.image == None:
            Back2.image = load_image('space_back2.png')
        self.back2_x = 1350     #second background, 'x' location

    def update(self,frame_time):
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

    PIXEL_PER_METER = (13.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4

    miko_image = None
    miko_attack_image = None
    miko_weapone_image = None

    def __init__(self):
        self.x = 50
        self.y = 300
        self.count = 0          #miko weapone count
        self.diecount = 5       #miko hp
        self.weap = [Weapone() for i in range(20)]      #miko weapone
        self.frame = 0    # miko frame
        self.framea = 0   # miko weapone frame
        self.righton = False
        self.lefton = False
        self.upon = False
        self.downon = False
        self.state = False  # enter 'a' key(image change)
        self.attstate = False   # miko weapone state

        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir = 1

        if Miko.miko_image == None:
            Miko.miko_image = load_image('miko.png')
        if Miko.miko_attack_image == None:
            Miko.miko_attack_image = load_image('mikoattack.png')
        if Miko.miko_weapone_image == None:
            Miko.miko_weapone_image = load_image('weapone1.png')

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

    def update(self,frame_time):

        self.frame += int(self.total_frames) % 8
        self.framea += int(self.total_frames) % 5
        self.life_time += frame_time
        distance = miko.RUN_SPEED_PPS * frame_time
        self.total_frames += miko.FRAMES_PER_ACTION * miko.ACTION_PER_TIME * frame_time

        if self.righton == True and self.x <860:
            self.x += (self.dir * distance)
        if self.lefton == True and self.x > 40:
            self.x -= (self.dir * distance)
        if self.upon == True and self.y < 560:
            self.y += (self.dir * distance)
        if self.downon == True and self.y > 30:
            self.y -= (self.dir * distance)
        for i in range(20):
            if self.attstate == True:
                if self.weap[i].state == True:
                    self.weap[i].xx += (self.dir * distance*1.3)

    def draw(self):
        if self.state == True:
            self.miko_attack_image.clip_draw((self.frame%4) * 105, 0 , 80, 70, self.x, self.y)
        if self.state == False:
            self.miko_image.draw(self.x,self.y)
        for i in range(20):
            if self.weap[i].state == True:
                self.miko_weapone_image.clip_draw((self.framea % 5) * 35, 0, 25, 30, self.weap[i].xx, self.weap[i].yy)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x-35,self.y-20,self.x+25,self.y+30

    def draw_aa(self,i):
        draw_rectangle(*self.get_aa(i))

    def get_aa(self,i):
        return self.weap[i].xx-10,self.weap[i].yy-10,self.weap[i].xx-10,self.weap[i].yy+12

class Blue_monster:

    PIXEL_PER_METER = (30.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4

    image = None
    def __init__(self):
        if Blue_monster.image == None:
            Blue_monster.image = load_image('enemy1.png')
        self.frame = random.randint(0,10)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir = 1.0
        self.x, self.y = random.randint(1100, 3000), random.randint(60, 570)

    def update(self,frame_time):
        self.frame += int(self.total_frames) % 2
        self.life_time += frame_time
        distance = miko.RUN_SPEED_PPS * frame_time
        self.total_frames += miko.FRAMES_PER_ACTION * miko.ACTION_PER_TIME * frame_time

        self.x -= (self.dir * distance)
        if self.x <=0:
            self.x = random.randint(900,1500)
            self.y = random.randint(80,570)

    def draw(self):
        self.image.clip_draw((self.frame % 4) * 60, 0, 60, 50, self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 25, self.y - 20, self.x + 15, self.y + 20

class Devil:

    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4

    image = None
    hit_image = None
    def __init__(self):
        if Devil.image == None:
            Devil.image = load_image('enemy2.png')
        if Devil.hit_image == None:
            Devil.hit_image = load_image('enemy2die.png')
        self.frame = random.randint(0,10)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir = 1.15
        self.x, self.y = random.randint(1700, 2500), random.randint(60, 570)
        self.state = False

    def update(self,frame_time):
        self.frame += int(self.total_frames) % 3
        self.framea = int(self.total_frames) % 5
        self.life_time += frame_time
        distance = miko.RUN_SPEED_PPS * frame_time
        self.total_frames += miko.FRAMES_PER_ACTION * miko.ACTION_PER_TIME * frame_time

        self.x -= (self.dir * distance)
        if self.x <=0:
            self.x = random.randint(900,2000)
            self.y = random.randint(80,570)

    def draw(self):
        if self.state == False:
            self.image.clip_draw((self.frame % 3) * 69, 0, 74, 100, self.x, self.y)
        if self.state == True:
            self.hit_image.clip_draw((self.framea % 2)* 65, 0, 74, 100, self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 25, self.y - 30, self.x + 25, self.y + 40

class Boss:

    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 7

    image = None
    def __init__(self):
        if Boss.image == None:
            Boss.image = load_image('boss.png')
        self.frame = 0
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir = 0.5
        self.x, self.y = 1200,300

    def update(self,frame_time):
        self.frame += int(self.total_frames) % 7
        self.life_time += frame_time
        distance = miko.RUN_SPEED_PPS * frame_time
        self.total_frames += miko.FRAMES_PER_ACTION * miko.ACTION_PER_TIME * frame_time

        if score_count >=350:               #score over 350, boss appearance
            self.x -= (self.dir * distance)

        if self.x <=700:
            self.x = 700
            self.y = 300

    def draw(self):
        if(score_count >= 350):
            self.image.clip_draw((self.frame % 7) * 262, 0, 253, 550, self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 100, self.y - 160, self.x + 110, self.y + 210

class Collision_line:       # if miko.weap.x >= 900 , miko.attstate = False
    def __init__(self):
        self.x,self.y =900,300
        Collision_line.image = load_image('line.png')

    def draw(self):
        self.image.draw(self.x,self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 5, self.y - 300, self.x + 5, self.y + 300

def handle_events(frame_time):
    global miko
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        else:
            miko.handle_event(event)

def enter():
    global back1, back2, miko, enemy1, enemy2, enemies1, enemies2, warning_font, score_font, score_count, second_collision, boss, boss1, collision_line, line
    back1 = Back1()
    back2 = Back2()
    miko = Miko()
    enemy1 = Blue_monster()
    enemies1 = [Blue_monster() for i in range(15)]  # blue monster
    enemy2 = Devil()
    enemies2 = [Devil() for i in range(12)]  # devil
    boss = Boss()
    boss1 = [Boss()for i in range(1)] # boss
    collision_line = Collision_line()
    line = [Collision_line() for i in range(1)]
    warning_font = load_font('ENCR10B.TTF', 115)        #warning view
    score_font = load_font('ENCR10B.TTF', 25)           #score view
    score_count = 0             #score
    second_collision = 0        #devil second collision, remove

def exit():
    global back1, back2, enemy1, enemy2, boss
    del(back1)
    del(back2)
    del(enemy1)
    del(enemy2)
    del(boss)

def collide1(a, b):                             #miko body, enemy collision
    left_a, bottom_a,right_a,top_a = a.get_bb()
    left_b, bottom_b,right_b,top_b = b.get_bb()

    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False

    return True

def collide2(a, b, i):                          #miko weapone, enemy collision
    left_a, bottom_a,right_a,top_a = a.get_aa(i)
    left_b, bottom_b,right_b,top_b = b.get_bb()

    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False

    return True

def update(frame_time):
    global score_count,second_collision,die_delay
    back1.update(frame_time)
    back2.update(frame_time)
    miko.update(frame_time)
    for enemy1 in enemies1:
        enemy1.update(frame_time)
    for enemy2 in enemies2:
        enemy2.update(frame_time)
    for boss in boss1:
        boss.update(frame_time)

    for i in range(20):
        for enemy1 in enemies1:
            if collide2(miko, enemy1,i):        #(miko.weap) , (blue monster) collision
                score_count += 10               #score+
                miko.attstate = False
                enemies1.remove(enemy1)
                miko.weap[i].yy = 1000

    for i in range(20):
        for enemy2 in enemies2:                 #(miko.weap) ,(devil)collsion
            if collide2(miko, enemy2,i):
                second_collision += 20          #(devil), remove of second collision
                miko.attstate = False
                enemy2.state = True
                miko.weap[i].yy = 1000
                if second_collision >= 21:      #(devil), remove of second collision
                    #print(second_collision)
                    score_count += 20  # score+
                    second_collision = 0
                    enemies2.remove(enemy2)
                    miko.weap[i].yy = 1000

    for i in range(20):                         #(miko.weap) >=900 collsion
        for collision_line in line:
            if collide2(miko, collision_line, i):
                miko.attstate = False
                miko.weap[i].yy =1000

    for i in range(20):                         #(miko.weap) , (boss) collision
        for boss in boss1:
            if collide2(miko, boss, i):
                second_collision += 20
                miko.attstate = False
                miko.weap[i].yy = 1000
                if second_collision >= 200:
                    score_count += 500
                    second_collision = 0
                    boss1.remove(boss)
                    miko.weap[i].yy = 1000

def draw(frame_time):
    hide_cursor()
    clear_canvas()
    back1.draw()
    back2.draw()
    miko.draw()

    #boss.draw_bb()
    #for i in range(20):
    #    miko.draw_aa(i)
    #miko.draw_bb()
    #for enemy1 in enemies1:
    #    enemy1.draw_bb()
    #for enemy2 in enemies2:
    #    enemy2.draw_bb()
    #collision_line.draw_bb()

    for enemy1 in enemies1:
        enemy1.draw()
    for enemy2 in enemies2:
        enemy2.draw()
    for boss in boss1:
        boss.draw()

    score_font.draw(700,570,'score: '+str(score_count), (255,255,255))

    for enemy1 in enemies1:             #miko, blue monster collision, game over
        if collide1(miko, enemy1):
            warning_font.draw(230, 300, 'WARNING!', (255, 0, 0))
            sleep(0.02)
            miko.diecount -= 1          #miko hp
            #print(miko.diecount)
            if (miko.diecount <= 0):
                game_framework.change_state(game_over_state)

    for enemy2 in enemies2:            #miko, devil collision, game over
        if collide1(miko, enemy2):
            warning_font.draw(230, 300, 'WARNING!', (255, 0, 0))
            sleep(0.01)
            miko.diecount -= 2          #miko hp
            #print(miko.diecount)
            if (miko.diecount <= 0):
                game_framework.change_state(game_over_state)



    update_canvas()
    delay(0.001)