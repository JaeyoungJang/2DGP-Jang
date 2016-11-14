import game_framework
import title_state
from pico2d import *

name = "How"

image = None

def enter():
    global image
    image = load_image('images.png')

def exit():
    pass

def update():
   pass

def draw():
    global image
    clear_canvas()
    image.draw(450, 300)
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)

def pause():
    pass

def resume():
    pass