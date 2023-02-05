class Car():
    def __init__(self,make,color,speed):
        self.make = make
        self.color = color
        self.speed = speed

    def description(self):
        print("Марка авто:",self.make,"\nЦвет:", self.color, "\nМакс. скорость:", self.speed)

    def ride(self):
        print(self.color,self.make,"проехала на красный свет")
class NesterovCar(Car):
    def __init__(self,make,color,speed,rider):
        super().__init__(make,color,speed)
        self.rider = rider
    def rider_change(self):
        print("Дмитрий Егоров уволен")
        self.rider = "Виталий Несоров собственной персоной"
        print(self.make, self.color, "за рулём -", self.rider)
        
car1 = Car("BMW", "Black", 250)
car1.description()
car1.ride()
ncar = NesterovCar("McPython", "Blue", 228, "Дмитрий Егоров")
ncar.description()
ncar.rider_change()
