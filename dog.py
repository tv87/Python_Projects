# Tej Vyas
# CS 100 - 006
# Homework 11, April 16, 2020

# Problem 1
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

        # Problem 2
        self.tricks = []
        
    # Problem 3
    def teach(self, trickName):
        self.tricks.append(trickName)
        print(self.name + " knows " + trickName)

    # Problem 4
    def knows(self, trickName):
        if trickName in self.tricks:
            print("Yes, " + self.name + " knows " + trickName)
            return True
        else:
            print("No, " + self.name + " doesn't know " + trickName)
            return False

    # Problem 5
    species = "Canis familiaris"

    
