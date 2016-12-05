import game_framework
import title_state
from pico2d import *

name = "Loding kpu"

image = None
logo_time = 0.0
pad_w = 900
pad_h = 600

def enter():
    global image
    open_canvas(pad_w, pad_h)
    image = load_image('kpu_credit.png')

def exit():
    global image
    del(image)
    close_canvas()

def update(frame_time):
    global logo_time
    if(logo_time >1.0):
        logo_time = 0
        game_framework.push_state(title_state)
    delay(0.05)
    logo_time += 0.1

def draw(frame_time):
    global image
    clear_canvas()
    image.draw(450, 300)
    update_canvas()

def handle_events(frame_time):
    events = get_events()
    pass

def pause():
    pass

def resume():
    pass




