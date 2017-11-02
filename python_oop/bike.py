class Bike(object):
    def __init__(self, name, price, max_speed):
        self.name = name
        self.price = price
        self.max_speed = max_speed
        self.total_miles = 0
    def displayinfo(self):
        print "The price for {} is ${}. Woah. That's a pretty penny.".format(self.name, self.price)
        print "The max speed for {} is {} Mph!".format(self.name, self.max_speed)
        print "Your total miles ridden on {} is now: {} miles".format(self.name, self.total_miles)
        return self
    def ride(self):
        print "You are now riding! Bike or Die!"
        self.total_miles += 10
        return self
    def reverse(self):
        print "You are now reversing. That won't help fool my dad, Ferris."
        if self.total_miles  < 3:
            self.total_miles = 0
        else:
            self.total_miles -= 3
        return self


bike1 = Bike("bike1", 613, 45)
bike1.ride().ride().ride().reverse()
bike1.displayinfo() 

bike2 = Bike("bike2", 770, 55)
bike2.ride().ride().reverse().reverse().reverse()
bike2.displayinfo()

bike3 = Bike("bike3", 306, 30)
bike3.reverse().reverse().reverse()
bike3.displayinfo()