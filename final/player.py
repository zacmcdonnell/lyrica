import random

import staticData as data


class player:

    startingLocations = [5, 6, 9, 10]

    @classmethod
    def createPlayer(cls):
        cls.name = 'joe'
        cls.health = 3
        cls.stamina = 10
        cls.location = random.choice(player.startingLocations)

    @classmethod
    def movePlayer(cls, restriction, amountMoved):
        # if the player location is not in the restrictions
        if cls.location not in restriction:
            # then move the player by the specified amount
            cls.location += amountMoved
            # call the describle location method inside the gameMap class
        else:
            # print a random blocked message if player location in restrictions
            print(data.blockedMessages[random.randint(0, 8)])

    @classmethod
    def describeLocation(cls):
        # display where the player is
        print('------------------------------------------------------')
        print('You have arrived at the',
              data.locationMessage[cls.location])
        # display the player's health and stamina
        print('You have', cls.health, 'health.')
        print('You have', cls.stamina, 'staminer left.')

    # define the stamina method
    @classmethod
    def setStamina(cls):
        # if the stamina has run out display and - health else take away stamina
        if cls.stamina < 1:
            print("You have run out of stamina -1 health")
            cls.stamina = 10
            cls.health -= 1
        else:
            cls.stamina -= 1
