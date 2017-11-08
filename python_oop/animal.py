class Animal(object): #parent class called "Animal"
    def __init__(self, name):
        self.name = name
        self.health = 100

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def display_health(self):
        print "{}'s health is: {}HP".format(self.name, self.health)
        return self


class Dog(Animal): 
    """Child class called 'Dog'. Inheriting most init attributes."""
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150
        # return self DO I NEED A SELF RETURN HERE?

    def pet(self):
        self.health += 5
        return self


class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.name = name
        self.health = 170

    def fly(self):
        self.fly -= 10
        return self

    def display_health(self):
        print "I'm a dragon, fool!"
        super(Dragon, self).display_health()
        return self
        
        
    

# animal1 = Animal("Billy")
# animal1.walk().walk().walk().run().run().display_health()
dog1 = Dog("Fido")
dog1.walk().walk().walk().run().run().pet().display_health()
# saphira = Dragon("Saphira")
# saphira.display_health()
# snowy = Dog("Snowy")
# snowy.run().pet().run().fly().display_health()