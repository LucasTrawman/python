import random

class Hat:

    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"] # A class variable is the same for every object that you create from that class (this is a class variable)

    @classmethod
    def sort(cls, name): #class method
        print(name, "is in", random.choice(cls.houses))
# the name cls or self actually doesn't matter, when you use classmethod It'll understand that it is a method from the class
# and when you don't use it, it will know that it is a method from the object/instance

Hat.sort("Harry")