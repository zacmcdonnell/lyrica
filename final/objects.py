import random
import staticData as data
from player import player


class GameObjects:

    @staticmethod
    def describeObjects():
        print('yeet')
        for k, v in GameObjects.items.items():
            if v.location == player.location:
                print("You see a", k, "here.")

        for k, v in GameObjects.NPCs.items():
            if player.location == v.location:
                # get current NPC and ask the user if they would like to talk to them
                hello = input('Would you like to talk to ' + k + '? ')
                return v.talk(k) if hello.startswith(
                    'y') else print('ill see you later on')

    @staticmethod
    def findObjectLocations():
        for k, v in GameObjects.NPCs.items():
            print(k, "location = ", v.location)

        for k, v in GameObjects.items.items():
            print(k, "location = ", v.location)

        print("player location = ", player.location)

    @staticmethod
    def shuffle():
        print('WOOOOHAAAAA TSUNAMI INCOMING')
        print("you get swept away along with everything else!!")
        # loop through all objects
        for i in GameObjects.items:
            for i in GameObjects.NPCs:  # change thier location property to a random number between 0 and 15
                i.location = random.randint(0, 15)

        # change the players location
        player.location = random.randint(0, 15)
        # display the new location to the user
        return player.describeLocation()


class NPC(GameObjects):
    def __init__(self, location):
        self.location = location

    def talk(self, name):
        # check which NPC to interact with
        if name == "The baker":
            print('Hey dude, Im the baker - wanna free snack?')
            # ask the player if they want a free snack
            ask = input("Yes or No: ").lower()
            print(ask)
            if ask.startswith('y'):
                # if so add 1 to the players health if not at max health
                if player.health < 5:
                    player.health += 1
                    print("health + 1")
                print('your welcome dude come again!!')
            else:
                print('your loss.....')
        elif name == 'fox':
            # choose a random weather forecast from the weatherOptions list
            weather = random.choice(data.weatherOptions)
            # call the shuffle() method if the weather forecast equals tsunami else print the weather
            self.shuffle() if weather == 'tsunami' else print(
                "hey man the weather forcast is", weather)
        else:
            print(
                "whoops couldn't be bothered impelenting that NPC what a drag amiright")


class item(GameObjects):
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


GameObjects.NPCs = {
    'The baker': NPC(6),
    'fox': NPC(random.randint(0, 14)),
    'dolphine': NPC(13)

}

GameObjects.items = {
    'flute': item(6, False),
    'stone': item(5, False)
}
