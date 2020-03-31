import staticData as data
from items import item
from npcs import NPC
from player import player
import random


class gameMap:
    # define the create objects function

    items = {
        'flute': item(6, False),
        'stone': item(5, False)
    }
    NPCs = {
        'The baker': NPC(6),
        'fox': NPC(random.randint(0, 14)),
        'dolphine': NPC(13)

    }

    @staticmethod
    def describeMap():
        # loop through all the items in the objects list and print their name and location
        for k, v in gameMap.NPCs.items():
            print(k, "location = ", v.location)

        for k, v in gameMap.items.items():
            print(k, "location = ", v.location)

        print("player location = ", player.location)

    # define the describeLocation method
    @staticmethod
    def describeLocation():
        # display where the player is
        print('------------------------------------------------------')
        print('You have arrived at the',
              data.locationMessage[player.location])
        # display the player's health and stamina
        print('You have', player.health, 'health.')
        print('You have', player.stamina, 'staminer left.')
        # loop through all the objects
        for k, v in gameMap.items.items():
            if v.location == player.location:
                print("You see a", k, "here.")

        for k, v in gameMap.NPCs.items():
            if player.location == v.location:
                # get current NPC and ask the user if they would like to talk to them
                hello = input('Would you like to talk to ' + k + '? ')
                v.talk(k) if hello.startswith(
                    'y') else print('ill see you later on')

    # move all objects and players to a random location
    @staticmethod
    def shuffle():
        print('WOOOOHAAAAA TSUNAMI INCOMING')
        print("you get swept away along with everything else!!")
        # loop through all objects
        for i in gameMap.items:
            for i in gameMap.NPCs:  # change thier location property to a random number between 0 and 15
                i.location = random.randint(0, 15)

        # change the players location
        player.location = random.randint(0, 15)
        # display the new location to the user
        gameMap.describeLocation()
