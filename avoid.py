from pico2d import *
import random

pad_w = 900
pad_h = 600
back1_x = 450
back2_x = 1350

# Game object class here
def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
class Back1:
    def __init__(self):
        self.image = load_image('back.png')
    def update(self):
        self.image = load_image('back.png')
    def draw(self):
        self.image.draw(back1_x,300)
class Back2:
    def __init__(self):
        self.image = load_image('back2.png')
    def update(self):
        self.image = load_image('back2.png')
    def draw(self):
        self.image.draw(back2_x,300)

# initialization code
open_canvas(pad_w,pad_h)

back1 = Back1()
back2 = Back2()
running = True
# game main loop code
while running:

    handle_events()

    clear_canvas()

    back1.draw()
    back2.draw()

    update_canvas()
    back1_x -= 10
    back2_x -= 10
    if back1_x == -450:
        back1_x = 1350
    if back2_x == -450:
        back2_x = 1350

    delay(0.05)

# finalization code
close_canvas()