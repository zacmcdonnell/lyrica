import random
from player import player
import staticData as data


class NPC:
    # define attributes for the NPC class
    def __init__(self, location):
        # attach to self construct for later use in the methods of the class
        self.location = location

    # define talk function - this handles NPC interaction
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
            gameMap.shuffle() if weather == 'tsunami' else print(
                "hey man the weather forcast is", weather)
        else:
            print(
                "whoops couldn't be bothered impelenting that NPC what a drag amiright")
