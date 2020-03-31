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
