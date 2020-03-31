import random
import os
# import static data to delcutter main file

import staticData as data
from player import player
from items import item
from npcs import NPC
from movement import movement
from gameMap import gameMap


# define the Game class
class Game:
    # define attributes for the NPC class
    def __init__(self):
        self.gamePlaying = True
        self.start()

    def start(self):
        # intialise the game and display welcome screen
        os.system('cls')
        # ask for the player name
        player.createPlayer()
        player.name = input('What is your name Adventurer? ')
        os.system('cls')
        print("-----------------WELCOME, TO THE FOREST OF LYRICA----------------- \n")
        print("  Your challenge is the defeat the dragon and claim your victory   \n")
        print("  ------------------------INSTRUCTIONS:------------------------\n")
        print('    Control your charater by using sentances such as "go north"\n')
        # create the player object
        # create the game objects and describe the location
        gameMap.describeLocation()

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
            if movement.goWhere(i, False) or i in gameMap.items.keys():
                # only use the first noun and verb else extra nouns or verbs are ignored
                noun = i if noun == None else print('extra nouns are ignored')
                # print('noun = ', noun)

            elif i in data.verbs:
                verb = i if verb == None else print('extra verbs are ignored')
                # print('verb = ', verb)
            elif i in data.joiningWords:
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
            if player.health < 1:
                if input('unlucky mate, try again? ').startswith('y'):
                    Game()
                else:
                    self.gamePlaying = False
            # check what the verbs and nouns were and call appropraite functions
            elif self.handleInput():
                # check if the user wanted to move
                if verb in data.moveCommands and movement.goWhere(noun, False):
                    restriction, amountMoved = movement.goWhere(noun, True)
                    if movement.movePlayer(player, restriction, amountMoved):
                        gameMap.describeLocation()
                    else:
                        # print a random blocked message if player location in restrictions
                        print(data.blockedMessages[random.randint(0, 8)])

                # check if the user wanted to drop or take an item
                for k, v in gameMap.items.items():
                    if k == noun:
                        item.getItem(v, verb, k)


# program entry point
if __name__ == '__main__':
    # assign the game class to the master variable
    master = Game()
    # call the mainGame()
    master.MainGame()
