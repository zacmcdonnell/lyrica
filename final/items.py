import staticData as data
from player import player


class item:
    # define attributes for the item class
    def __init__(self, location, inBackpack):
        # attach to self construct for later use in the methods of the class
        self.location = location
        self.inBackpack = inBackpack

    # define get method
    def getItem(self, verb, name):
        if verb in data.dropCommands:
            # if the item is in the backpack set it to false and display to user
            if self.inBackpack:
                self.inBackpack = False
                # change location to where the player dropped it
                self.location = player.location
                print("The", name, "has been dropped")
            else:
                print("You can't drop something you don't have!")

        elif verb in data.collectCommands:
            # if the player location is the same as the item location and the item isn't in the backpack
            if player.location == self.location and self.inBackpack == False:
                # put the item in the backpack
                self.inBackpack = True
                # display to user
                print("The", name, "has been added to your inventory")
            else:
                print("You can't take something thats not there")
