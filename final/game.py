import random
import os
# import static data to delcutter main file
from staticData import *


# create the class player
class player:
    # create the class atributes of the player class
    def __init__(self, name):
        self.name = name
        self.health = 3
        self.stamina = 10
        # set starting location to a middle random location
        self.location = random.choice(startingLocations)

    # define the move player method
    def movePlayer(self):
        # if the player location is not in the restrictions
        if self.location not in restriction:
            # then move the player by the specified amount
            self.location += amountMoved
            # call the describle location method inside the gameMap class
            gameMap().describeLocation()
        else:
            # print a random blocked message if player location in restrictions
            print(blockedMessages[random.randint(0, 8)])

    # define the stamina method
    def setStamina(self):
        # if the stamina has run out display and - health else take away stamina
        if self.stamina < 1:
            print("You have run out of stamina -1 health")
            self.stamina = 10
            self.health -= 1
        else:
            self.stamina -= 1


# create the class, game map
class gameMap:
    # define the create objects function
    def createObjects(self):
        global items, NPCs

        items = {
            'flute': item(6, False),
            'stone': item(5, False)
        }
        NPCs = {
            'The baker': NPC(6),
            'fox': NPC(random.randint(0, 14)),
            'dolphine': NPC(13)

        }
        self.describeMap()

    # desribe all the objects in the map

    def describeMap(self):
        # loop through all the items in the objects list and print their name and location
        for i in items:
            print(i, "location = ", items.get(i).location)
        for i in NPCs:
            print(i, "location = ", NPCs.get(i).location)
        print("player location = ", player1.location)

    # define the describeLocation method

    def describeLocation(self):
        # display where the player is
        print('------------------------------------------------------')
        print('You have arrived at the',
              locationMessage[player1.location])
        # display the player's health and stamina
        print('You have', player1.health, 'health.')
        print('You have', player1.stamina, 'staminer left.')
        # loop through all the objects
        for i in items:
            if items.get(i).location == player1.location:
                print("You see a", i, "here.")

        for i in NPCs:
            if player1.location == NPCs.get(i).location:
                # get current NPC and ask the user if they would like to talk to them
                hello = input('Would you like to talk to ' + i + '? ')
                NPCs.get(i).talk(i) if hello.startswith(
                    'y') else print('ill see you later on')

    # move all objects and players to a random location
    def shuffle(self):
        print('WOOOOHAAAAA TSUNAMI INCOMING')
        print("you get swept away along with everything else!!")
        # loop through all objects
        for i in items:
            for i in NPCs:  # change thier location property to a random number between 0 and 15
                i.location = random.randint(0, 15)

        # change the players location
        player1.location = random.randint(0, 15)
        # display the new location to the user
        self.describeLocation()


# define the class, item
class item:
    # define attributes for the item class
    def __init__(self, location, inBackpack):
        # attach to self construct for later use in the methods of the class
        self.location = location
        self.inBackpack = inBackpack

    # define get method
    def getItem(self, verb, name):
        if verb in dropCommands:
            # if the item is in the backpack set it to false and display to user
            if self.inBackpack:
                self.inBackpack = False
                # change location to where the player dropped it
                self.location = player1.location
                print("The", name, "has been dropped")
            else:
                print("You can't drop something you don't have!")

        elif verb in collectCommands:
            # if the player location is the same as the item location and the item isn't in the backpack
            if player1.location == self.location and self.inBackpack == False:
                # put the item in the backpack
                self.inBackpack = True
                # display to user
                print("The", name, "has been added to your inventory")
            else:
                print("You can't take something thats not there")


# create the NPC class
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
                if player1.health < 5:
                    player1.health += 1
                    print("health + 1")
                print('your welcome dude come again!!')
            else:
                print('your loss.....')
        elif name == 'fox':
            # choose a random weather forecast from the weatherOptions list
            weather = random.choice(weatherOptions)
            # call the shuffle() method if the weather forecast equals tsunami else print the weather
            gameMap().shuffle() if weather == 'tsunami' else print(
                "hey man the weather forcast is", weather)
        else:
            print(
                "whoops couldn't be bothered impelenting that NPC what a drag amiright")

# define the Game class


class Game:
    # define attributes for the NPC class
    def __init__(self):
        self.gamePlaying = True
        self.start()

    def start(self):
        global player1
        # intialise the game and display welcome screen
        os.system('cls')
        # ask for the player name
        characterName = input('What is your name Adventurer? ')
        os.system('cls')
        print("-----------------WELCOME, TO THE FOREST OF LYRICA----------------- \n")
        print("  Your challenge is the defeat the dragon and claim your victory   \n")
        print("  ------------------------INSTRUCTIONS:------------------------\n")
        print('    Control your charater by using sentances such as "go north"\n')
        # create the player object
        player1 = player(characterName)
        # create the game objects and describe the location
        gameMap().createObjects()
        gameMap().describeLocation()

    # handle the user input

    def handleInput(self):
        global verb, noun
        # reset variables
        verb = None
        noun = None
        # ask for user input and split the response into indiviuals strings and store in array
        userInput = input("Enter your next action: ").lower().split()
        os.system('cls')
        # print('UserInput =', userInput)

        # loop through the userInput array
        for i in userInput:
            # print('current word:', i)
            # check if the item is a verb or noun
            if self.goWhere(i) or i in items.keys():
                # only use the first noun and verb else extra nouns or verbs are ignored
                noun = i if noun == None else print('extra nouns are ignored')
                # print('noun = ', noun)

            elif i in verbs:
                verb = i if verb == None else print('extra verbs are ignored')
                # print('verb = ', verb)
            elif i in joiningWords:
                None
            else:
                # if a word is entered that the program doesn't understand
                print("I'm not sure what you mean by", i)
                return False
        # checks that the user entered a verb and a noun
        if noun == None or verb == None:
            print('Please enter both a noun and a verb')
        else:
            return verb, noun

    # define the MainGame method
    def MainGame(self):
        # create a game loop
        while self.gamePlaying:
            # check if the player died
            if player1.health < 1:
                if input('unlucky mate, try again? ').startswith('y'):
                    Game()
                else:
                    self.gamePlaying = False
            # check what the verbs and nouns were and call appropraite functions
            elif self.handleInput():
                # check if the user wanted to move
                if verb in moveCommands and self.goWhere(noun):
                    player1.movePlayer()
                # check if the user wanted to drop or take an item
                for i in items:
                    if i == noun:
                        items.get(i).getItem(verb, i)

    def goWhere(self, direction):
        global restriction, amountMoved
        # set a count
        # loop through the moveKeywords dictionary keys
        for i in movements.values():
            # check if the direction is in the current key's value
            if direction in i.keywords:
                # assign restriction to the corresponding list element based off the looping order
                restriction = i.restrictions
                # assign amountMoved to the corresponding list element based off the looping order
                amountMoved = i.amountMoved
                return True
            # add one to the count


# program entry point
if __name__ == '__main__':
    # assign the game class to the master variable
    master = Game()
    # call the mainGame()
    master.MainGame()
