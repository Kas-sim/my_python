from tkinter import *
import random


GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"



class snake:
    pass

class food:
    pass

def next_turn():
    pass

def change_direction():
    pass

def check_collisions():
    pass

def game_over():
    pass



window = Tk()
window.title("Snake Game by MQ")
window.resizable(False, False)

score = 0
direction = "down"

label = Label(window, text="Score: {}".format(score), font=("Roboto", 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, width=GAME_WIDTH, height=GAME_HEIGHT)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
window_screenwidth = window.winfo_screenwidth()
window_screenheight = window.winfo_screenheight()

x = int((window_screenwidth/2) - (window_width/2))
y = int((window_screenheight/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")


window.mainloop()