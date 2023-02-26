from tkinter import *
import time
class Ball():
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.oval = canvas.create_oval(10,10,25,25,fill = color)
        self.canvas.move(self.oval, 240,100)
        self.x = 0
        self.y = -1    
    def draw(self):
        self.canvas.move(self.oval,self.x,self.y)

window = Tk ()
window.title("Арканоид")
window.resizable(0,0)
window.wm_attributes ("-topmost",1)
canvas = Canvas (window,width = 500, height = 400)
canvas.pack()
ball = Ball(canvas,"red")
while True:
    ball.draw()
    window.update()
    time.sleep(0.000000000001)
