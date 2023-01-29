from tkinter import *
import time  #importing time for animation

def greeting():
    print("Добро пожаловать")
def good_night():
    print("Споки ноки, пупсик")
    
window = Tk() #creating a window
canvas = Canvas(window, width = 500, height = 500) #creating canvas
canvas.pack()
canvas.create_line(0,0,500,500) #creating line'''
blue_rect = canvas.create_rectangle(250,250,500,500, fill = "blue") #creating blue square
red_rect = canvas.create_rectangle(20,20,250,250, fill = "red")  #creating red square
a = 10
while a>0:
    canvas.move(red_rect,23,0)
    a = a-1
    window.update()
    time.sleep(0.1)
'''my_button = Button(window, text = "Привет", command = greeting)
my_button.pack()
sleep_button = Button(window, text = "Пора баиньки", command = good_night)
sleep_button.pack()'''
