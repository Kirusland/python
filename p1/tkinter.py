from tkinter import *

def greeting():
    print("Добро пожаловать")
def good_night():
    print("Споки ноки, пупсик")

window = Tk()
canvas = Canvas(window, width = 500, height = 500)
canvas.pack()
canvas.create_line(0,0,500,500)
canvas.create_rectangle(20,20,250,250, fill = "blue")
'''my_button = Button(window, text = "Привет", command = greeting)
my_button.pack()
sleep_button = Button(window, text = "Пора баиньки", command = good_night)
sleep_button.pack()'''
