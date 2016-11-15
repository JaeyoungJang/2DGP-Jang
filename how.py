import game_framework
import title_state
import avoid
from pico2d import *

name = "How"

image = None

def enter():
    global image
    image = load_image('how.png')

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
    global x,y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)

        if event.type == SDL_MOUSEMOTION:
            x,y = event.x, 600 - event.y
        if event.type == SDL_MOUSEBUTTONDOWN and event.button ==  SDL_BUTTON_LEFT:
            if 720< x and x <840 and 480<y and y<540:
                game_framework.change_state(avoid)
            if 720< x and x <840 and 40<y and y<90:
                game_framework.change_state(title_state)

def pause():
    pass

def resume():
    pass