class Car():
    def __init__(self,make,color,speed):
        self.make = make
        self.color = color
        self.speed = speed

    def description(self):
        print("Марка авто:",self.make,"\nЦвет:", self.color, "\nМакс. скорость:", self.speed)
