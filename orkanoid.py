from tkinter import *
import time
import random
class Ball():
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.oval = canvas.create_oval(10,10,25,25,fill = color)
        self.canvas.move(self.oval,240,100)
        self.directions = [-3,-2,-1,1,2,3]
        self.x = random.choice(self.directions)
        self.y = -1
    def touch_platform(self,ball_pos):
        platoform_pos = self.canvas.coords(self.platform.rect)
        if ball_pos[2] >= platform)pos[0] and ball_pos[0] <= platform_pos[2]:
    def draw(self):
        self.canvas.move(self.oval, self.x, self.y)
        pos = self.canvas.coords(self.oval)
        print(pos)
        if pos[1] <=0:
            self.y = 1
        if pos[3] >= 400:
            self.y = -1
        if pos[2] >=500:
            self.x = -1
        if pos[0] <=0:
            self.x = 1
class Platform():
    def __init__(self,canvas,platform,color):
        self.canvas = canvas
        self.platform = platform
        self.rect = canvas.create_rectangle(0,0,100,10,fill=color)
        self.canvas.move(self.rect,200,300)
        self.x = 0
        self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>',self.turn_right)
    def turn_left(self,event):
        self.x = -2
    def turn_right(self,event):
        self.x = 2
    def draw(self):
        self.canvas.move(self.rect,self.x, 0)
        pos = self.canvas.coords(self.rect)
        if pos[0] <= 0:
            self.x = 0
        if pos[2] >= 500:
            self.x = 0
            
 
window = Tk()
window.title("Nesterov game")
window.resizable(0,0)
window.wm_attributes("-topmost",1)
canvas = Canvas(window, width = 500, height = 400)
canvas.pack()
platform = Platform(canvas,'red')
ball = Ball(canvas,platform,"blue")
while True:
    ball.draw()
    platform.draw()
    window.update()
    time.sleep(0.01)
