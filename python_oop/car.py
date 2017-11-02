class Car(object):
    def __init__(self, name, price, speed, fuel, mileage):
        self.name = name
        self.price = price
        self.tax = 0
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
    def display_all(self):
        if self.price > 10000:
            self.tax = "15%"
        else:
            self.tax = "12%"
        print "Here is all the info on the {}: Price: ${}. Tax Rate:{}. Speed: {}Mph. Fuel: {}. Mileage: {}MPG.".format(self.name, self.price, self.tax, self.speed, self.fuel, self.mileage)
        return self

car1 = Car("Toyota", 10000, 90, "Full", 35)
car1.display_all()
car2 = Car("Honda", 10000, 90, "Full", 35)
car2.display_all()
car3 = Car("Audi", 80000, 120, "Full", 25)
car3.display_all()
car4 = Car("Lexus", 80000, 110, "Half", 20)
car4.display_all()
car5 = Car("Kia", 8000, 80, "Near Empty", 28)
car5.display_all()
car6 = Car("Tesla", 100000, 255, "Always Full, Baby!", 330)
car6.display_all()