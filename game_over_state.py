import game_framework
import avoid
import title_state
from pico2d import *

name = "GameOverState"

image = None
logo_time = 0.0


def enter():
    global image
    image = load_image('gameover.png')

def exit():
    pass

def update(frame_time):
    global logo_time
    if(logo_time >1.0):
        logo_time = 0
        game_framework.push_state(title_state)
    delay(0.05)
    logo_time += 0.05

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




