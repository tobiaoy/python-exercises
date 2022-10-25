class Dog:
    """A simple attempt to model a dog in OOP."""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sit(self):
        print("{name} is now sitting.".format(name=self.name))
    
    def roll_over(self):
        print("{name} rolled over!".format(name=self.name))
        
    