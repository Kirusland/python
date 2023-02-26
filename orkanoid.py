
from tkinter import *
import time
import random

class Ball():
    '''Класс мячика'''
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.oval = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.oval, 240, 100)
        self.directions = [-3, -2, -1, 1, 2, 3]
        self.x = random.choice(self.directions)
        self.y = -1

    def draw(self):
        self.canvas.move(self.oval, self.x, self.y)       
        pos = self.canvas.coords(self.oval)
        print(pos)
        if pos[1] <= 0:
            self.y = 1
        if pos[3] >= 400:
            self.y = -1
        if pos[0] <= 0:
            self.x = 1
        if pos[2] >= 500:
            self.x = -1

class Platform():
    '''Класс платформы'''
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.rect = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.rect, 200, 300)
        

#--------------------------------MAIN-----------------------------------
window = Tk()
window.title("Арканоид")
window.resizable(0, 0)
window.wm_attributes("-topmost", 1)
canvas = Canvas(window, width=500, height=400)
canvas.pack()

ball = Ball(canvas, 'blue')
platform = Platform(canvas, 'yellow')

while True:
    ball.draw()
    window.update()
    time.sleep(0.01)
