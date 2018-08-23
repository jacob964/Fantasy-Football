# class for all fantasy football players

class FootballPlayer:
    
    def __init__(self,name):
        self.name = name
    
    # Simple example function to test object method calling
    def give_name(self):
        print("My name is {0}!".format(self.name))

p = Player("Jacob")
p.give_name()












# Class variables
# Name: Name of the football player (First, Last Name)
