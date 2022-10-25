"""A class/module to represent a classic die"""
from random import randint

class Die:
    def __init__(self, sides):
        self.sides = sides
        
    def roll_die(self):
        roll = randint(1, self.sides)
        return roll
    

sample_die = Die(6)
ten_die = Die(10)
twenty_die = Die(20)

for i in range(11):
    print(sample_die.roll_die())
    print(ten_die.roll_die())
    print(twenty_die.roll_die())
