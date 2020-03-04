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
        global objects
        # create a list and add all the game objects to the list
        objects = []
        # append the objects to the list
        objects.append(item('flute', 6, False))
        # create objects based off the item class and specify atributes such as location and inBackpack
        objects.append(item('stone', 5, False))

        objects.append(NPC('The baker', 6))
        objects.append(NPC('fox', random.randint(0, 14)))
        objects.append(NPC('dolphine', 13))

    # desribe all the objects in the map
    def describeMap(self):
        # loop through all the items in the objects list and print their name and location
        for i in objects:
            print("name = ", i.name, "location = ", i.location)

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
        for i in objects:
            # check what the what atribute of the object is
            if i.what == 'item':
                # find all the items in the object list and call the isItem() methon
                i.isItem()
                # if there is an NPC in the object list call the hello() method
            if i.what == 'NPC':
                i.hello()

    # move all objects and players to a random location
    def shuffle(self):
        print('WOOOOHAAAAA TSUNAMI INCOMING')
        print("you get swept away along with everything else!!")
        # loop through all objects
        for i in objects:
            # change thier location property to a random number between 0 and 15
            i.location = random.randint(0, 15)

        # change the players location
        player1.location = random.randint(0, 15)
        # display the new location to the user
        self.describeLocation()


# define the class, item
class item:
    # define attributes for the item class
    def __init__(self, name, location, inBackpack):
        # attach to self construct for later use in the methods of the class
        self.what = 'item'
        self.name = name
        self.location = location
        self.inBackpack = inBackpack
        self.keywords()

# define isItem Method
    def isItem(self):
        # if the player is at the same location
        if self.location == player1.location:
            print("You see a", self.name, "here.")

    # define get method
    def getItem(self, verb):
        if verb in dropCommands:
            # if the item is in the backpack set it to false and display to user
            if self.inBackpack:
                self.inBackpack = False
                # change location to where the player dropped it
                self.location = player1.location
                print("The", self.name, "has been dropped")
            else:
                print("You can't drop something you don't have!")

        elif verb in collectCommands:
            # if the player location is the same as the item location and the item isn't in the backpack
            if player1.location == self.location and self.inBackpack == False:
                # put the item in the backpack
                self.inBackpack = True
                # display to user
                print("The", self.name, "has been added to your inventory")
            else:
                print("You can't take something thats not there")

    def keywords(self):
        # when an item object is created the function attaches the name to a list for later use
        return itemKeywords.append(self.name)


# create the NPC class
class NPC:
    # define attributes for the NPC class
    def __init__(self, name, location):
        # attach to self construct for later use in the methods of the class
        self.what = 'NPC'
        self.name = name
        self.location = location

    # define hello method - this deals with NPC interation
    def hello(self):
        # check if player is at the same location as NPC
        if player1.location == self.location:
            # get current NPC and ask the user if they would like to talk to them
            hello = input('Would you like to talk to ' + self.name + '? ')
            self.talk(self.name) if hello.startswith(
                'y') else print('ill see you later on')

    # define talk function - this handles NPC interaction
    def talk(self, name):
        # check which NPC to interact with
        if self.name == "The baker":
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
        elif self.name == 'fox':
            # choose a random weather forecast from the weatherOptions list
            weather = random.choice(weatherOptions)
            # call the shuffle() method if the weather forecast equals tsunami else print the weather
            gameMap().shuffle() if weather == 'tsunami' else print(
                "hey man the weather forcast is", weather)
        else:
            print("whoops couldn't be bothered impelenting that NPC what a drag amiright")

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

        # loop through the userInput array
        for i in userInput:
            # check if the item is a verb or noun
            if self.goWhere(i) or i in itemKeywords:
                # only use the first noun and verb else extra nouns or verbs are ignored
                noun = i if noun == None else print('extra nouns are ignored')

            elif i in verbs:
                verb = i if verb == None else print('extra verbs are ignored')
            else:
                # if a word is entered that the program doesn't understand
                print('I dont understand that word..')
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
                # set the stamina
                player1.setStamina()

                # check if the user wanted to move
                if verb in moveCommands and self.goWhere(noun):
                    player1.movePlayer()
                # check if the user wanted to drop or take an item
                for i in objects:
                    if i.name == noun:
                        i.getItem(verb)

    def goWhere(self, direction):
        global restriction, amountMoved
        # set a count
        count = 0
        # loop through the moveKeywords dictionary keys
        for i in moveKeywords:
            # check if the direction is in the current key's value
            if direction in moveKeywords.get(i):
                # assign restriction to the corresponding list element based off the looping order
                restriction = restrictionList[count]
                # assign amountMoved to the corresponding list element based off the looping order
                amountMoved = amountMovedList[count]
                return True
            # add one to the count
            count += 1


# program entry point
if __name__ == '__main__':
    # assign the game class to the master variable
    master = Game()
    # call the mainGame()
    master.MainGame()
